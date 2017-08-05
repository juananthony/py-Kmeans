import random
from KMeansCluster import KMeansCluster
from KMeansPoint import KMeansPoint
from numpy import *

class KMeansClassifier:
    clusters = []

    def __init__(self):
        print("construction")
        self.cluster = []

    def addGroup(self, group):
        self.groups.append(group)

    def getGroups(self):
        return self.groups

    def train(self, numClusters, dataset):
        #print("KMeansClassifier ---  train()  --- init - Dataset leng: " + str(len(dataset)))
        # create the cluster objects
        self.createInitClusters(numClusters, dataset)
        self.getClusterInfo()
        # training
        anyClusterHasMoved = True
        while anyClusterHasMoved:
            #import pdb; pdb.set_trace()
            #print("KMeansClassifier ---  train()  ---  training loop")
            # for each point, find nearest cluster
            for cluster in self.clusters:
                #print("KMeansClassifier ---  train()  ---  cluster loop")
                clusterPoints = cluster.getPoints()
                for point in clusterPoints:
                    #print("KMeansClassifier ---  train()  ---  point loop")
                    closerCluster = self.getCloserCluster(point)
                    if cluster.isNot(closerCluster):
                        #print("add point")
                        #print(point.getPosition())
                        closerCluster.addPoint(point)
                        cluster.removePoint(point)
            # for each cluster, establish new position
            anyClusterHasMoved = False
            for cluster in self.clusters:
                aux = cluster.setPosition()
                #print("cluster has been moved: " + str(aux))
                anyClusterHasMoved = anyClusterHasMoved or aux
            #print("value of anyClusterHasMoved: " + str(anyClusterHasMoved))

    def classify(self, position):
        #print("KMeansClassifier  ---  classify()")
        point = KMeansPoint(position, 1)
        return self.getCloserCluster(point)

    def createInitClusters(self, numClusters, dataset):
        #print("KMeansClassifier ---  createInitClusters()  ---  init")
        # get all the N random clusters
        randomClusters = random.choice(range(0,len(dataset)), numClusters)
        #print("KMeansClassifier ---  createInitClusters()  ---  numRandomClusters: " + str(len(randomClusters)))
        #print(randomClusters)

        for example in randomClusters:
            randomCluster = KMeansCluster(dataset[example], example)
            self.clusters.append(randomCluster)

        #print("KMeansClassifier ---  createInitClusters()  ---  creating point")
        index = 0
        for entry in dataset:
            #print("new entry: " + str(entry))
            point = KMeansPoint(entry, index)
            index += 1
            cluster = self.getCloserCluster(point)
            cluster.addPoint(point)

    def getCloserCluster(self, point):
        #print("KMeansClassifier ---  getCloserCluster()  ---  init")
        #print("point")
        #print(point.getPosition())
        minDistance = -1
        closer = "asdf"

        for cluster in self.clusters:
            #print("KMeansClassifier ---  getCloserCluster()  ---  cluster loop")
            #print(cluster.getPosition())
            distance = self.getDistance(point, cluster)
            if (minDistance == -1) or distance < minDistance:
                closer = ""
                closer = cluster
                minDistance = distance

        return closer

    def getDistance(self, point, cluster):
        #print("KMeansClassifier ---  getDistance()  ---  init")
        return sqrt(sum(power(subtract(point.getPosition(), cluster.getPosition()), 2)))

    def getClusterInfo(self):
        print("|------- CLUSTER INFO -------|")
        print("Number of clusters: " + str(len(self.clusters)))
        print("Cluster positions")
        index = 0
        while index < len(self.clusters):
            print("\n+ Cluster[" + str(index) + "]) with id: " + str(self.clusters[index].clusterId))
            print("|- position: ")
            print(self.clusters[index].getPosition())
            print("|- num points: " + str(len(self.clusters[index].getPoints())))
            print("|- points: ")
            points = self.clusters[index].getPoints()
            for point in points:
                print("pointId: " + str(point.getId()) + " | position: " + str(point.getPosition()))
            index += 1
        print("|----------------------------|")
