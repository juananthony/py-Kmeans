from KMeansCluster import KMeansCluster
from KMeansPoint import KMeansPoint
from numpy import *
import random

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
        # create the cluster objects
        self.createInitClusters(numClusters, dataset)
        self.getClustersInfo()
        # training
        anyClusterHasMoved = True
        index = 1
        while anyClusterHasMoved:
            #import pdb; pdb.set_trace()
            # for each point, find nearest cluster
            for cluster in self.clusters:
                clusterPoints = cluster.getPoints()
                for point in clusterPoints:
                    closerCluster = self.getCloserCluster(point)
                    if cluster.isNot(closerCluster):
                        closerCluster.addPoint(point)
                        cluster.removePoint(point)
            # for each cluster, establish new position
            anyClusterHasMoved = False
            for cluster in self.clusters:
                aux = cluster.setPosition()
                anyClusterHasMoved = anyClusterHasMoved or aux
            index += 1
        print("Cluster classified in " + str(index) + " iterations.")

    def classify(self, position):
        #print("KMeansClassifier  ---  classify()")
        point = KMeansPoint(position, 1)
        return self.getCloserCluster(point)

    def createInitClusters(self, numClusters, dataset):
        # get all the N random clusters
        randomClusters = random.sample(xrange(0,len(dataset)), numClusters)

        for example in randomClusters:
            randomCluster = KMeansCluster(dataset[example], example)
            self.clusters.append(randomCluster)


        index = 0
        for entry in dataset:
            point = KMeansPoint(entry, index)
            index += 1
            cluster = self.getCloserCluster(point)
            cluster.addPoint(point)

    def getCloserCluster(self, point):
        minDistance = -1
        closer = "asdf"

        for cluster in self.clusters:
            distance = self.getDistance(point, cluster)
            if (minDistance == -1) or distance < minDistance:
                closer = ""
                closer = cluster
                minDistance = distance

        return closer

    def getDistance(self, point, cluster):
        return sqrt(sum(power(subtract(point.getPosition(), cluster.getPosition()), 2)))

    def getClustersInfo(self):
        print("\n|------- CLUSTER INFO -------|")
        print("Number of clusters: " + str(len(self.clusters)))
        print("Cluster positions")
        index = 0
        while index < len(self.clusters):
            print("\n+ Cluster[" + str(index) + "] with id: " + str(self.clusters[index].clusterId))
            print("\t|- position:\t" + str(self.clusters[index].getPosition()))
            print("\t|- num points:\t" + str(len(self.clusters[index].getPoints())))
            print("\t|- points: ")
            points = self.clusters[index].getPoints()
            for point in points:
                print("\t\tpointId:\t" + str(point.getId()) + "\t|\tposition:\t" + str(point.getPosition()))
            index += 1
        print("\n\n|----------------------------|\n\n\n")

    def getClustersPositions(self):
        clusterPositions = []
        for cluster in self.clusters:
            clusterPositions.append(cluster.getPosition())
        return clusterPositions
