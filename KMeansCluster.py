from KMeansPoint import KMeansPoint

class KMeansCluster:
    position = []
    points = []
    clusterId = -1

    def __init__(self, position, clusterId):
        #print("KMeansCluster  ---  init()  ---  init. position.leng:" + str(len(position)))
        #print(position)
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
        #print("KMeansCluster  ---  setPosition()  ---  init. Num points: " + str(len(self.points)))
        positionHasChange = False
        dimentions = []
        for point in self.points:
            #print("KMeansCluster  ---  setPosition()  ---  numDim: " + str(len(point.getPosition())) + " point position:")
            #print(point.getPosition())
            dimIndex = 0
            for dim in point.getPosition():
                #print("dimIndex: " + str(dimIndex) + " | dim:")
                #print(dim)
                if dimIndex >= len(dimentions):
                    #print("- dimIndex > len(dimentions) -")
                    dimentions.append(dim)
                else:
                    #print(" - else -")
                    dimentions[dimIndex] += dim
                dimIndex += 1
        newPosition=[]
        #print(" - building newPosition[] - ")
        for dim in dimentions:
            #print(" - new dim: " + str(dim))
            newPosition.append(dim /len(self.points))
        #print("oldPosition:")
        #print(self.position)
        #print("new position: ")
        #print(newPosition)
        if self.positionHasChange(newPosition):
            #print("POSITION HAS CHANGE")
            positionHasChange = True
        self.position = newPosition
        #print("new position of the cluster:")
        #print(newPosition)
        return positionHasChange

    def isNot(self, otherCluster):
        retValue = True
        if self.getId() == otherCluster.getId():
            retValue = False
        return retValue

    def addPoint(self, point):
        self.points.append(point)

    def removePoint(self, point):
        #print("KMeansCluster ---  removePoint()  ---  init - pointId:" + str(point.getId()))
        for point in self.points:
            #print("KMeansCluster ---  removePoint()  ---  points loop - numPoints: " + str(len(self.points)))
            if point.getId() == point.getId():
                self.points.remove(point)
            else:
                print(" !!!!!!!!!!!!!!!!!!!!  N O T   F O U N D !!!!!!!!!!!!!!!!!")
    def positionHasChange(self, newPosition):
        hasBeenChanged = False
        actualNumDims = len(self.position)
        newNumDims = len(newPosition)
        if actualNumDims == newNumDims:
            index = 0
            while index < actualNumDims:
                if abs(self.position[index] - newPosition[index]) > 0.00000001:
                    hasBeenChanged = True
                index += 1

        else:
            raise Exception("Positions have not same dimentions")
        return hasBeenChanged
