import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("autos.csv", index_col=0, sep=',')
data = df.iloc[:, [8, 9]]
X = data.values


def ksrodki(X, k):
    n_samples = X.shape[0]
    clusters = np.zeros(n_samples)
    centroids = X[np.random.permutation(n_samples)[:k]]
    converged = False
    while not converged:
        for i in range(n_samples):
            distances = np.sqrt(np.sum((X[i] - centroids) ** 2, axis=1))
            clusters[i] = np.argmin(distances)
        new_centroids = pd.DataFrame(X).groupby(by=clusters).mean().values
        if np.allclose(centroids, new_centroids):
            converged = True
        else:
            centroids = new_centroids
    return centroids, clusters


def distp(X, C):
    tablica = []
    for i in C:
        for j in X:
            tablica.append(np.linalg.norm(j - i))
    return tablica


def distm(X, C, V):
    tablica = []
    V_inv = np.linalg.inv(V)
    for i in X:
        for j in C:
            tablica.append(np.sqrt(np.dot(np.dot((i - j), V_inv), (i - j).T)))
    return tablica


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


C, CX = ksrodki(X, 4)
grupowania = F(C, 4)
print(grupowania)

plt.scatter(X[:, 0], X[:, 1], c=CX, marker='o')
plt.scatter(C[:, 0], C[:, 1], c='r', marker='v')
plt.savefig('wykres.png')
plt.show()