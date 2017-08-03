import random
import KMeansCluster from KMeansCluster
from numpy import *

class KMeansClassifier:
    clusters = []

    def addGroup(self, group):
        self.groups.append(group)

    def getGroups(self):
        return self.groups

    def train(self, numClusters, dataset):
        # create the cluster objects
        self.createInitClusters(self, randomClusters, dataset)

        # training
        anyClusterHasMoved = True
        while anyClusterHasMoved:
            # for each point, find nearest cluster
            for cluster in clusters:
                clusterPoints = cluster.getPoints()
                for point in clusterPoints:
                    closerCluster = self.getCloserCluster(self, point)
                    if cluster.isNot(closerCluster):
                        closerCluster.addPoint(point)
                        cluster.removePoint(point)


    def createInitClusters(self, numClusters, dataset):
        # get all the N random clusters
        randomClusters = random.sample(range(0,len(dataset)), numClusters)

        for example in randomClusters:
            randomCluster = new KMeansCluster()
            randomCluster.init(dataset[example])
            self.cluster.append(randomCluster)

        for point in dataset:
            cluster = self.getCloserCluster(self, point)
            cluster.addPoint(point)

    def getCloserCluster(self, point):
        minDistance = -1
        closer = new KMeansCluster()

        for cluster in clusters:
            distance = self.getDistance(self, point, cluster)
            if (minDistance == -1) || distance < minDistance:
                closer = cluster
                minDistance = distance

        return closer

    def getDistance(self, point, cluster):
        return sqrt(sum(power(point.getPosition - cluster.getPosition(), 2)))
