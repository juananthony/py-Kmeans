
class KMeansClassifier:
    classes = []

    def addGroup(self, group):
        self.groups.append(group)

    def getGroups(self):
        return self.groups

    def test(self, numClasses, dataset):
        
