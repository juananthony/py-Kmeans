class PyKMeansPoint:
    position = []
    pointId = -1

    def __init__(self, position, pointId):
        self.position = position
        self.pointId = pointId
    def getPosition(self):
        return self.position
    def getId(self):
        return self.pointId
