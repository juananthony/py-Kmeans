# py-kMeans
PyKMeans creates a K number of clusters by a given N number of points (or observations).

It uses K-means clustering (https://en.wikipedia.org/wiki/K-means_clustering).

## Components
PyKMeans has 3 different classes

### PyKMeans
PyKMeans is the main class. It has to create the clusters, iterates and assign the points to a cluster.

### PyKMeansCluster
PyKMeansCluster is the class which has the cluster operations as set the new position of the cluster in a step, remove or add points to the cluster.

### PyKMeansPoint
PyKMeansPoint is a simple class which contains the relative information of an observation.

## How to use it.
Copy the files into your project and import the main class like this:
```python
from PyKMeans import PyKMeans
```

After that you can create a PyKMeans object:
```python
main = PyKMeans()
```

Then, you can train the K-means clustering:
```python
main.train(<NUMBER_OF_CLUSTERS>, <OBSERVATIONS_ARRAY>)
```

When it finished clustering, you can get the position of these clusters:
```python
main.getClustersPositions()
```

Or get the cluster that belongs other observation:
```python
cluster = main.getClusterOf([1.1,1.1])
```

You can print all information of the clusters using:
```python
main.getClustersInfo()
```

## Examples
### Example 1
This example creates a PyKMeans object and train it with an array of observations called points, and show the clusters and the points in a plot. After that, using the clusters, it returns the clusters in which a given observation belongs to.
```python
import matplotlib.pyplot as plt
from PyKMeans import PyKMeans

# create the K-means classifier
main = PyKMeans()

# array of observations
points = [[1,1], [1.2,1.0], [1.3, 1.1], [1.8, 0.7], [1.1, 0.7], [0.8, 0.7], [3,3], [3.1,3.0], [3.0,3.1], [3.2,3.7], [2.9,3.4], [9.7,11], [10,10], [10.5,10.7], [10.2,10.1], [-4,-3], [-4,-4.5], [-3,-4.5], [-3,-3.7]]

# create 4 clusters with points array
main.train(4, points)

# return the cluster that the point [1.1, 1.1] belongs to
otherObservation = [1.1, 1.1]
cluster = main.getClusterOf(otherObservation)

# returns a info of the clusters like position and points of them
main.getClustersInfo()

# prints the point and his cluster
print("Point " + str(otherObservation) + " belongs to cluster: " + str(cluster.getPosition()))

# returns the clusters position
clusters = main.getClustersPositions()

# Shows the observations and clusters in a plot
plt.plot(*sum(points, []), marker='o', color='r')
plt.plot(*sum(clusters, []), marker='^', color='g')
plt.show()
```

### Example 2
This examples is similar to the previous one. But, this uses a new dimention in the observations. With a given 11 observations in 3 dimentions, that creates 2 clusters and show them in a plot.

```python
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
```
