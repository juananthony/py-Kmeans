import random
from KMeansCluster import KMeansCluster
from KMeansPoint import KMeansPoint
from numpy import *

class KMeansClassifier:
    clusters = []

    def addGroup(self, group):
        self.groups.append(group)

    def getGroups(self):
        return self.groups

    def train(self, numClusters, dataset):
        #print("KMeansClassifier ---  train()  --- init - Dataset leng: " + str(len(dataset)))
        # create the cluster objects
        self.createInitClusters(numClusters, dataset)

        # training
        anyClusterHasMoved = True
        while anyClusterHasMoved:
            #print("KMeansClassifier ---  train()  ---  training loop")
            # for each point, find nearest cluster
            for cluster in self.clusters:
                #print("KMeansClassifier ---  train()  ---  cluster loop")
                clusterPoints = cluster.getPoints()
                for point in clusterPoints:
                    #print("KMeansClassifier ---  train()  ---  point loop")
                    closerCluster = self.getCloserCluster(point)
                    if cluster.isNot(closerCluster):
                        closerCluster.addPoint(point)
                        cluster.removePoint(point)
            # for each cluster, establish new position
            for cluster in self.clusters:
                aux = cluster.setPosition()
                print("cluster has been moved: " + str(aux))
                anyClusterHasMoved = anyClusterHasMoved or aux
            print("value of anyClusterHasMoved: " + str(anyClusterHasMoved))

    def classify(self, position):
        #print("KMeansClassifier  ---  classify()")
        point = KMeansPoint()
        point.init(position, 1)
        return self.getCloserCluster(point)

    def createInitClusters(self, numClusters, dataset):
        #print("KMeansClassifier ---  createInitClusters()  ---  init")
        # get all the N random clusters
        randomClusters = random.choice(range(0,len(dataset)), numClusters)
        #print("KMeansClassifier ---  createInitClusters()  ---  numRandomClusters: " + str(len(randomClusters)))
        #print(randomClusters)

        for example in randomClusters:
            randomCluster = KMeansCluster()
            randomCluster.init(dataset[example])
            self.clusters.append(randomCluster)

        #print("KMeansClassifier ---  createInitClusters()  ---  creating point")
        index = 0
        for entry in dataset:
            point = KMeansPoint()
            point.init(entry, index)
            index += 1
            cluster = self.getCloserCluster(point)
            cluster.addPoint(point)

    def getCloserCluster(self, point):
        #print("KMeansClassifier ---  getCloserCluster()  ---  init")
        #print("point")
        #print(point.getPosition())
        minDistance = -1
        closer = KMeansCluster()

        for cluster in self.clusters:
            #print("KMeansClassifier ---  getCloserCluster()  ---  cluster loop")
            #print(cluster.getPosition())
            distance = self.getDistance(point, cluster)
            if (minDistance == -1) or distance < minDistance:
                closer = cluster
                minDistance = distance

        return closer

    def getDistance(self, point, cluster):
        #print("KMeansClassifier ---  getDistance()  ---  init")
        return sqrt(sum(power(subtract(point.getPosition(), cluster.getPosition()), 2)))
