from KMeansPoint import KMeansPoint

class KMeansCluster:
    position = []
    points = []
    clusterId = -1

    def __init__(self, position, clusterId):
        self.position = position
        self.clusterId = clusterId
        self.points = []

    def getPoints(self):
        return self.points

    def getId(self):
        return self.clusterId

    def getPosition(self):
        return self.position

    def setPosition(self):
        positionHasChange = False
        dimentions = []
        for point in self.points:
            dimIndex = 0
            for dim in point.getPosition():
                if dimIndex == len(dimentions):
                    print("- append (dimIndex: " + str(dimIndex) + " |  len(dimentions): " + str(len(dimentions)) + ")")
                    dimentions.append(dim)
                else:
                    print("- sum (dimIndex: " + str(dimIndex) + " |  len(dimentions): " + str(len(dimentions)) + ")")
                    dimentions[dimIndex] += dim
                dimIndex += 1
        newPosition=[]
        for dim in dimentions:
            print("Cluster id " + str(self.getId()) + " dimention: " + str(dim) + " | points: " + str(len(self.points)))
            newPosition.append(dim / len(self.points))
        print("old position: " + str(self.position) + "  |  new position: " + str(newPosition))
        if self.positionHasChange(newPosition):
            positionHasChange = True
        self.position = newPosition
        return positionHasChange

    def isNot(self, otherCluster):
        retValue = True
        if self.getId() == otherCluster.getId():
            retValue = False
        return retValue

    def addPoint(self, point):
        self.points.append(point)

    def removePoint(self, pointToRemove):
        founded = False
        for point in self.points:
            if pointToRemove.getId() == point.getId():
                self.points.remove(point)
                founded = True
        if founded is False:
            print(" !!!!!!!!!!!!!!!!!!!!  N O T   F O U N D !!!!!!!!!!!!!!!!!")

    def positionHasChange(self, newPosition):
        hasBeenChanged = False
        actualNumDims = len(self.position)
        newNumDims = len(newPosition)
        if actualNumDims == newNumDims:
            index = 0
            while index < actualNumDims:
                print("old dim " + str(index) + ": " + str(self.position[index]) + "\t|  new dim " + str(index) + ": " + str(newPosition[index]))
                if abs(self.position[index] - newPosition[index]) > 0.0000000001:
                    hasBeenChanged = True
                index += 1

        else:
            raise Exception("Positions have not same dimentions")
        return hasBeenChanged
