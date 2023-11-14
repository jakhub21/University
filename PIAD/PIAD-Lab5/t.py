import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("autos.csv", index_col=0, sep=',')
data = df.iloc[:, [8, 9]]
X = data.values


def distp(X, C):
    d = []
    for i in C:
        for j in X:
            d.append(np.sqrt((j - i) * np.transpose(j - i)))
    return d


def distm(X, C, V):
    d = []
    for i in X:
        for j in C:
            d.append(np.sqrt((i - j) * np.inv(V) * np.transpose(i - j)))
    return d


def ksrodki(X, k):
    clusters = np.zeros(X.shape[0])
    centroids = X[np.random.permutation(X.shape[0])[:k]]
    flag = True
    while flag:
        for i, punkt in enumerate(X):
            min_dist = float('inf')
            for j, centroid in enumerate(centroids):
                d = np.sqrt((centroid[0] - punkt[0]) ** 2 + (centroid[1] - punkt[1]) ** 2)
                if min_dist > d:
                    min_dist = d
                    clusters[i] = j
        new_centroidy = pd.DataFrame(X).groupby(by=clusters).mean().values
        if not np.array_equal(centroids, new_centroidy):
            flag = False
        else:
            centroids = new_centroidy
    return centroids, clusters


def F(C, k):
    jnum = 0
    jden = 0
    for i in range(k):
        ci = C[i]
        for j in range(i + 1, k):
            cj = C[j]
            suma = np.sum(distp(ci, cj))
            jnum += suma
    for i in range(k):
        ci = C[i]
        sr = np.mean(ci, axis=0)
        suma = np.sum(distp(ci, [sr]))
        jden += suma
    return jnum / jden


centr, clust = ksrodki(X, 4)
jakosc_grupowania = F(centr, 4)
print(jakosc_grupowania)

plt.scatter(X[:, 0], X[:, 1], c=clust, marker='o')
plt.scatter(centr[:, 0], centr[:, 1], c='r', marker='v')
plt.savefig('wykres.png')
plt.show()
