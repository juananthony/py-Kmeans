import matplotlib.pyplot as plt
from PyKMeans import PyKMeans

# create the K-means classifier
main = PyKMeans()

points = [[1,1], [1.2,1.0], [1.3, 1.1], [1.8, 0.7], [1.1, 0.7], [0.8, 0.7], [3,3], [3.1,3.0], [3.0,3.1], [3.2,3.7], [2.9,3.4], [9.7,11], [10,10], [10.5,10.7], [10.2,10.1], [-4,-3], [-4,-4.5], [-3,-4.5], [-3,-3.7]]

main.train(4, points)

pointToClassify = [1.1,1.1]
cluster = main.classify(pointToClassify)

main.getClustersInfo()

print("Point " + str(pointToClassify) + " belongs to cluster: " + str(cluster.getPosition()))

clusters = main.getClustersPositions()

plt.plot(*sum(points, []), marker='o', color='r')
plt.plot(*sum(clusters, []), marker='^', color='g')
plt.show()
