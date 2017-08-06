import matplotlib.pyplot as plt
from PyKMeans import PyKMeans

# create the K-means classifier
main = PyKMeans()

# array of observations
points = [[1,1], [1.2,1.0], [1.3, 1.1], [1.8, 0.7], [1.1, 0.7], [0.8, 0.7], [3,3], [3.1,3.0], [3.0,3.1], [3.2,3.7], [2.9,3.4], [9.7,11], [10,10], [10.5,10.7], [10.2,10.1], [-4,-3], [-4,-4.5], [-3,-4.5], [-3,-3.7]]

# create 4 clusters with points array
main.train(4, points)

# return the cluster that the point [1.1, 1.1] belongs to
cluster = main.classify([1.1,1.1])

# returns a info of the clusters like position and points of them
main.getClustersInfo()

# prints the point and his cluster
print("Point " + str(pointToClassify) + " belongs to cluster: " + str(cluster.getPosition()))

# returns the clusters position
clusters = main.getClustersPositions()

# Shows the observations and clusters in a plot
plt.plot(*sum(points, []), marker='o', color='r')
plt.plot(*sum(clusters, []), marker='^', color='g')
plt.show()
