from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from PyKMeans import PyKMeans
import numpy as np

# create the K-means classifier
main = PyKMeans()

# array of observations
points = [[1, 1, 1.1], [1.2, 1.0, 0.8], [1.3, 1.1, 0.5], [1.8, 0.7, 1.3], [1.3, 0.7, 0.9], [0.8, 0.7, 1.7], [3.1, 3, 2.7], [3.1,3.0,2.6], [3.2,2.7,3.9], [3.2,3.7,2.2], [2.9,3.4,3.3]]

# create 4 clusters with points array
main.train(2, points)

# return the cluster that the point [1.1, 1.1] belongs to
otherObservation = [2.2, 1.6, 3.1]
cluster = main.getClusterOf(otherObservation)

# returns a info of the clusters like position and points of them
main.getClustersInfo()

# prints the point and his cluster
print("Point " + str(otherObservation) + " belongs to cluster: " + str(cluster.getPosition()))

# returns the clusters position
clusters = np.array(main.getClustersPositions())

# Shows the observations and clusters in a plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
pointsArray = np.array(points)
pointsX = pointsArray[:,0].tolist()
pointsY = pointsArray[:,0].tolist()
pointsZ = pointsArray[:,0].tolist()
clusterX = clusters[:,0].tolist()
clusterY = clusters[:,1].tolist()
clusterZ = clusters[:,2].tolist()
ax.scatter(pointsX, pointsY, pointsZ, c='r', marker='o')
ax.scatter(clusterX, clusterY, clusterZ, c='g', marker='^')
plt.show()
