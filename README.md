# py-kMeans
PyKMeans creates a K number of clusters by a given N number of points (or observations).

It uses K-means clustering (https://en.wikipedia.org/wiki/K-means_clustering)

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
cluster = main.getClusterOf([1.1,1.1])

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
```
