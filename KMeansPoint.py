class KMeansPoint:
    position = []
    pointId = -1

    def __init__(self, position, pointId):
        #print("KMeansPoint  ---  init()  ---  id: " + str(pointId) + " | position len: " + str(len(position)))
        #print(position)
        self.position = position
        self.pointId = pointId
    def getPosition(self):
        return self.position
    def getId(self):
        return self.pointId
