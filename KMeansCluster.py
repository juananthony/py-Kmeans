from KMeansPoint import KMeansPoint

class KMeansCluster:
    position = []
    points = []

    def init(self, position):
        #print("KMeansCluster  ---  init()  ---  init. position.leng:" + str(len(position)))
        #print(position)
        self.position = position

    def getPoints(self):
        return self.points

    def getPosition(self):
        return self.position

    def setPosition(self):
        #print("KMeansCluster  ---  setPosition()")
        positionHasChange = False
        dimentions = []
        for point in self.points:
            dimIndex = 0
            for dim in point.getPosition():
                if dimIndex > len(dimentions):
                    dimentions.append(dim)
                dimIndex += 1
        newPosition=[]
        for dim in dimentions:
            newPosition.append(dim /len(self.points))
        if newPosition != self.position:
            positionHasChange = True
        self.position = newPosition
        print("new position of the cluster:")
        print(newPosition)
        return positionHasChange

    def isNot(self, otherCluster):
        retValue = True
        if self.getPosition() == otherCluster.getPosition():
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
            #else:
                #print(" !!!!!!!!!!!!!!!!!!!!  N O T   F O U N D !!!!!!!!!!!!!!!!!")
