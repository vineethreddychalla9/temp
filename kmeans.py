import numpy as np
from sklearn.cluster import KMeans
x1=np.array([[1.713,1.586],[0.180,1.786],[0.353,1.240],[0.940,1.566],[1.486,0.759],[1.266,1.106],[1.540,0.459],[0.459,1.799],[0.773,0.186],[0.906,0.606]])
k_means = KMeans(n_clusters=3,random_state=15)
k_means.fit(x1)
centroid = k_means.cluster_centers_
labels = k_means.labels_
print(centroid)
print(labels)
for i in range(len(x1)):
    print("Cordinate: ",x1[i],"label: ",labels[i])

'''
OUTPUT:
centroids:
[[0.33066667 1.60833333][1.17625 0.5025][1.30633333 1.41933333]]
Labels: [2 0 0 2 1 2 1 0 1 1]
Cordinate: [1.713 1.586] label: 2
Cordinate: [0.18 1.786] label: 0
Cordinate: [0.353 1.24 ] label: 0
Cordinate: [0.94 1.566] label: 2
Cordinate: [1.486 0.759] label: 1
Cordinate: [1.266 1.106] label: 2
Cordinate: [1.54 0.459] label: 1
Cordinate: [0.459 1.799] label: 0
Cordinate: [0.773 0.186] label: 1
Cordinate: [0.906 0.606] label: 1'''