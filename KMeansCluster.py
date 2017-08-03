class KMeansCluster:
    position = []
    points = []

    def init(self, position):
        self.position = position

    def addPoint(self, point):
        self.points.append(point)

    def getPoints(self):
        return self.points

    def getPosition(self):
        return self.position

    def setPosition(self):


    def isNot(self, otherCluster):
        retValue = False
        if (self.getPosition() == otherCluster.getPosition()).all():
            retValue = True
        return retValue
