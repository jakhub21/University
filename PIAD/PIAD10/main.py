#Klasteryzacja danych
import numpy as np
import scipy as sp
import pandas as pd
import sklearn
from sklearn import datasets
import sklearn.cluster as cluster
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import jaccard_score
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import warnings
warnings.filterwarnings("ignore")

iris = datasets.load_iris()
X = iris.data
Y_real = iris.target


def find_perm(clusters, Y_real, Y_pred):
    perm = []
    for i in range(clusters):
        idx = Y_pred == i
        new_label = sp.stats.mode(Y_real[idx])[0][0]
        perm.append(new_label)
    return [perm[label] for label in Y_pred]


linkages = ["ward", "complete", "average", "single"]

pca = PCA(n_components=2)
XPCA = pca.fit_transform(X)
for i in range(len(linkages)):
    j = 1
    clustering = cluster.AgglomerativeClustering(n_clusters=3, linkage=linkages[i])
    clustering = clustering.fit(X)
    Y_pred = clustering.labels_
    Y_pred2 = np.array(find_perm(3, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(3, Y_real, Y_pred))
    plt.figure(figsize=(18, 6))

    #Zwyczajne wykresy
    plt.subplot(1, 3, j)
    for k in range(3):
        A = XPCA[Y_real == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')

    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_real)
    plt.title(linkages[i])

    #Wykresy z klasteryzacją
    plt.subplot(1, 3, j)
    for k in range(3):
        A = XPCA[Y_pred2 == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')
    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_pred2)
    plt.title("Klasteryzacja")

    #Wykresy roznic
    plt.subplot(1, 3, j)
    j += 1
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    plt.scatter(XPCA[:, 0], XPCA[:, 1],  c=diff, cmap=cmap)
    plt.title("Różnice")
    plt.savefig("AgglomerativeClustering_2D" + linkages[i] + ".png")
    plt.show()

#indeks Jakkaarda
print("Indeks Jakkaarda")
print("Ward: ", jaccard_score(Y_real, find_perm(3, Y_real, cluster.AgglomerativeClustering(n_clusters=3, linkage="ward").fit(X).labels_), average='macro'))
print("Complete: ", jaccard_score(Y_real, find_perm(3, Y_real, cluster.AgglomerativeClustering(n_clusters=3, linkage="complete").fit(X).labels_), average='macro'))
print("Average: ", jaccard_score(Y_real, find_perm(3, Y_real, cluster.AgglomerativeClustering(n_clusters=3, linkage="average").fit(X).labels_), average='macro'))
print("Single: ", jaccard_score(Y_real, find_perm(3, Y_real, cluster.AgglomerativeClustering(n_clusters=3, linkage="single").fit(X).labels_), average='macro'))

#Wizualizacja 3D
pca2 = PCA(n_components=3)
XPCA2 = pca2.fit_transform(X)
for i in range(len(linkages)):
    j = 0
    clustering = cluster.AgglomerativeClustering(n_clusters=3, linkage=linkages[i])
    clustering = clustering.fit(X)
    Y_pred = clustering.labels_
    Y_pred2 = np.array(find_perm(3, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(3, Y_real, Y_pred))

    fig, ax = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'projection': '3d'})

    #Zwyczajne wykresy
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_real)
    ax[j].set_title("Real")
    j += 1


    #Wykresy z klasteryzacją
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_pred2)
    ax[j].set_title("Klasteryzacja")
    j += 1


    #Wykresy roznic
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2],  c=diff, cmap=cmap)
    ax[j].set_title("Różnice")
    plt.savefig("AgglomerativeClustering_3D" + linkages[i] + ".png")

    # Wykres dendrogramu
    plt.figure(figsize=(10, 7))
    dendrogram(linkage(X, method=linkages[i]))
    plt.title('Dendrogram - ' + linkages[i])
    plt.savefig("AgglomerativeClustering_dendrogram_3D" + linkages[i] + ".png")
    plt.show()

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

#K-means
for i in range(1):
    j = 1
    clustering =  KMeans(n_clusters=3)
    clustering = clustering.fit(X)
    Y_pred = clustering.labels_
    Y_pred2 = np.array(find_perm(3, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(3, Y_real, Y_pred))
    plt.figure(figsize=(18, 6))

    #Zwyczajne wykresy
    plt.subplot(1, 3, j)
    for k in range(3):
        A = XPCA[Y_real == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')

    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_real)
    plt.title("KMeans Real")

    #Wykresy z klasteryzacją
    plt.subplot(1, 3, j)
    for k in range(3):
        A = XPCA[Y_pred2 == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')
    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_pred2)
    plt.title("KMeans Klasteryzacja")

    #Wykresy roznic
    plt.subplot(1, 3, j)
    j += 1
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    plt.scatter(XPCA[:, 0], XPCA[:, 1],  c=diff, cmap=cmap)
    plt.title("KMeans Różnice")
    plt.savefig("KMeans_2D.png")
    plt.show()

for i in range(1):
    j = 0
    clustering = KMeans(n_clusters=3)
    clustering = clustering.fit(X)
    Y_pred = clustering.labels_
    Y_pred2 = np.array(find_perm(3, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(3, Y_real, Y_pred))

    fig, ax = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'projection': '3d'})

    #Zwyczajne wykresy
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_real)
    ax[j].set_title("KMeans Real")
    j += 1


    #Wykresy z klasteryzacją
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_pred2)
    ax[j].set_title("KMeans Klasteryzacja")
    j += 1


    #Wykresy roznic
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2],  c=diff, cmap=cmap)
    ax[j].set_title("KMeans Różnice")
    plt.savefig("KMeans_3D.png")

    # Wykres dendrogramu
    plt.figure(figsize=(10, 7))
    dendrogram(linkage(X, method=linkages[i]))
    plt.title('KMeans Dendrogram - ' + linkages[i])
    plt.savefig("KMeans_dendrogram_3D.png")
    plt.show()

#K-means wladna funkcja
for i in range(1):
    j = 1
    C, Y_pred = ksrodki(XPCA, 3)
    Y_pred = Y_pred.astype(int)
    Y_pred2 = np.array(find_perm(3, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(3, Y_real, Y_pred))
    plt.figure(figsize=(18, 6))

    #Zwyczajne wykresy
    plt.subplot(1, 3, j)
    for k in range(3):
        A = XPCA[Y_real == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')

    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_real)
    plt.title("ksrodki real")

    #Wykresy z klasteryzacją
    plt.subplot(1, 3, j)
    for k in range(3):
        A = XPCA[Y_pred2 == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')
    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_pred2)
    plt.title("ksrodki Klasteryzacja")

    #Wykresy roznic
    plt.subplot(1, 3, j)
    j += 1
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    plt.scatter(XPCA[:, 0], XPCA[:, 1],   c=diff, cmap=cmap)
    plt.title("ksrodki Różnice")
    plt.savefig("ksrodki_2D.png")
    plt.show()

for i in range(1):
    j = 0
    C, Y_pred = ksrodki(XPCA2, 3)
    Y_pred = Y_pred.astype(int)
    Y_pred2 = np.array(find_perm(3, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(3, Y_real, Y_pred))

    fig, ax = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'projection': '3d'})

    #Zwyczajne wykresy
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_real)
    ax[j].set_title("Real")
    j += 1


    #Wykresy z klasteryzacją
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_pred2)
    ax[j].set_title("ksrodki Klasteryzacja")
    j += 1


    #Wykresy roznic
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2],  c=diff, cmap=cmap)
    ax[j].set_title("ksrodki Różnice")
    plt.savefig("ksrodki3D.png")

    # Wykres dendrogramu
    plt.figure(figsize=(10, 7))
    dendrogram(linkage(X, method=linkages[i]))
    plt.title('ksrodki Dendrogram - ' + linkages[i])
    plt.savefig("ksrodki3D_dendrogram.png")
    plt.show()

#GaussianMixture
for i in range(1):
    j = 1
    clustering = GaussianMixture(n_components=3)
    # Y_pred = clustering.fit_predict(X)
    Y_pred2 = np.array(find_perm(3, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(3, Y_real, Y_pred))
    plt.figure(figsize=(18, 6))

    #Zwyczajne wykresy
    plt.subplot(1, 3, j)
    for k in range(3):
        A = XPCA[Y_real == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')

    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_real)
    plt.title("GaussianMixture real")

    #Wykresy z klasteryzacją
    plt.subplot(1, 3, j)
    for k in range(3):
        A = XPCA[Y_pred2 == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')
    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_pred2)
    plt.title("GaussianMixture Klasteryzacja")

    #Wykresy roznic
    plt.subplot(1, 3, j)
    j += 1
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    plt.scatter(XPCA[:, 0], XPCA[:, 1],  c=diff, cmap=cmap)
    plt.title("GaussianMixture Różnice")
    plt.savefig("GaussianMixture_2D.png")
    plt.show()

for i in range(1):
    j = 0
    clustering = GaussianMixture(n_components=3)
    Y_pred = clustering.fit_predict(X)
    Y_pred2 = np.array(find_perm(3, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(3, Y_real, Y_pred))

    fig, ax = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'projection': '3d'})

    #Zwyczajne wykresy
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_real)
    ax[j].set_title("GaussianMixture Real")
    j += 1


    #Wykresy z klasteryzacją
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_pred2)
    ax[j].set_title("GaussianMixture Klasteryzacja")
    j += 1


    #Wykresy roznic
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2],  c=diff, cmap=cmap)
    ax[j].set_title("GaussianMixture Różnice")
    plt.savefig("GaussianMixture3D.png")

    # Wykres dendrogramu
    plt.figure(figsize=(10, 7))
    dendrogram(linkage(X, method=linkages[i]))
    plt.title('GaussianMixture Dendrogram - ' + linkages[i])
    plt.savefig("GaussianMixture3D_dendrogram.png")

    plt.show()

#zoo
zoo = pd.read_csv("zoo.csv")
zoo.replace(False, 0, inplace=True)
zoo.replace(True, 1, inplace=True)
indices, _ = pd.factorize(zoo.iloc[:, -1])
zoo.iloc[:, -1] = indices
X = zoo.iloc[:, 1:-1]
Y_real = zoo.iloc[:, -1]

def find_perm(clusters, Y_real, Y_pred):
    perm = []
    for i in range(clusters):
        idx = Y_pred == i
        new_label = sp.stats.mode(Y_real[idx])[0][0]
        perm.append(new_label)
    return [perm[label] for label in Y_pred]


linkages = ["ward", "complete", "average", "single"]

pca = PCA(n_components=2)
XPCA = pca.fit_transform(X)
for i in range(len(linkages)):
    j = 1
    clustering = cluster.AgglomerativeClustering(n_clusters=7, linkage=linkages[i])
    clustering = clustering.fit(X)
    Y_pred = clustering.labels_
    Y_pred2 = np.array(find_perm(7, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(7, Y_real, Y_pred))
    plt.figure(figsize=(18, 6))

    #Zwyczajne wykresy
    plt.subplot(1, 3, j)
    for k in range(7):
        A = XPCA[Y_real == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')

    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_real)
    plt.title(linkages[i])

    #Wykresy z klasteryzacją
    plt.subplot(1, 3, j)
    for k in range(7):
        A = XPCA[Y_pred2 == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')
    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_pred2)
    plt.title("ZOO_Klasteryzacja")

    #Wykresy roznic
    plt.subplot(1, 3, j)
    j += 1
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    plt.scatter(XPCA[:, 0], XPCA[:, 1],  c=diff, cmap=cmap)
    plt.title("ZOO_Różnice")
    plt.savefig("ZOO_AgglomerativeClustering_2D" + linkages[i] + ".png")
    plt.show()

#indeks Jakkaarda
# print("Indeks Jakkaarda")
# print("Ward: ", jaccard_score(Y_real, find_perm(3, Y_real, cluster.AgglomerativeClustering(n_clusters=3, linkage="ward").fit(X).labels_), average='macro'))
# print("Complete: ", jaccard_score(Y_real, find_perm(3, Y_real, cluster.AgglomerativeClustering(n_clusters=3, linkage="complete").fit(X).labels_), average='macro'))
# print("Average: ", jaccard_score(Y_real, find_perm(3, Y_real, cluster.AgglomerativeClustering(n_clusters=3, linkage="average").fit(X).labels_), average='macro'))
# print("Single: ", jaccard_score(Y_real, find_perm(3, Y_real, cluster.AgglomerativeClustering(n_clusters=3, linkage="single").fit(X).labels_), average='macro'))

#Wizualizacja 3D
pca2 = PCA(n_components=3)
XPCA2 = pca2.fit_transform(X)
for i in range(len(linkages)):
    j = 0
    clustering = cluster.AgglomerativeClustering(n_clusters=7, linkage=linkages[i])
    clustering = clustering.fit(X)
    Y_pred = clustering.labels_
    Y_pred2 = np.array(find_perm(7, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(7, Y_real, Y_pred))

    fig, ax = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'projection': '3d'})

    #Zwyczajne wykresy
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_real)
    ax[j].set_title("ZOO_Real")
    j += 1


    #Wykresy z klasteryzacją
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_pred2)
    ax[j].set_title("ZOO_Klasteryzacja")
    j += 1


    #Wykresy roznic
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2],  c=diff, cmap=cmap)
    ax[j].set_title("ZOO_Różnice")
    plt.savefig("ZOO_AgglomerativeClustering_3D" + linkages[i] + ".png")

    # Wykres dendrogramu
    plt.figure(figsize=(10, 7))
    dendrogram(linkage(X, method=linkages[i]))
    plt.title('ZOO_Dendrogram - ' + linkages[i])
    plt.savefig("ZOO_AgglomerativeClustering_dendrogram_3D" + linkages[i] + ".png")
    plt.show()

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

#K-means
for i in range(1):
    j = 1
    clustering =  KMeans(n_clusters=7)
    clustering = clustering.fit(X)
    Y_pred = clustering.labels_
    Y_pred2 = np.array(find_perm(7, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(7, Y_real, Y_pred))
    plt.figure(figsize=(18, 6))

    #Zwyczajne wykresy
    plt.subplot(1, 3, j)
    for k in range(7):
        A = XPCA[Y_real == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')

    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_real)
    plt.title("ZOO_KMeans Real")

    #Wykresy z klasteryzacją
    plt.subplot(1, 3, j)
    for k in range(7):
        A = XPCA[Y_pred2 == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')
    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_pred2)
    plt.title("ZOO_KMeans Klasteryzacja")

    #Wykresy roznic
    plt.subplot(1, 3, j)
    j += 1
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    plt.scatter(XPCA[:, 0], XPCA[:, 1],  c=diff, cmap=cmap)
    plt.title("ZOO_KMeans Różnice")
    plt.savefig("ZOO_KMeans_2D.png")
    plt.show()

for i in range(1):
    j = 0
    clustering = KMeans(n_clusters=7)
    clustering = clustering.fit(X)
    Y_pred = clustering.labels_
    Y_pred2 = np.array(find_perm(7, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(7, Y_real, Y_pred))

    fig, ax = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'projection': '3d'})

    #Zwyczajne wykresy
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_real)
    ax[j].set_title("ZOO_KMeans Real")
    j += 1


    #Wykresy z klasteryzacją
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_pred2)
    ax[j].set_title("ZOO_KMeans Klasteryzacja")
    j += 1


    #Wykresy roznic
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2],  c=diff, cmap=cmap)
    ax[j].set_title("ZOO_KMeans Różnice")
    plt.savefig("ZOO_KMeans_3D.png")

    # Wykres dendrogramu
    plt.figure(figsize=(10, 7))
    dendrogram(linkage(X, method=linkages[i]))
    plt.title('ZOO_KMeans Dendrogram - ' + linkages[i])
    plt.savefig("ZOO_KMeans_dendrogram_3D.png")
    plt.show()

#K-means wladna funkcja
# for i in range(1):
#     j = 1
#     C, Y_pred = ksrodki(XPCA, 7)
#     Y_pred = Y_pred.astype(int)
#     Y_pred2 = np.array(find_perm(7, Y_real, Y_pred))
#     print(linkages[i])
#     print(find_perm(7, Y_real, Y_pred))
#     plt.figure(figsize=(18, 6))
#
#     #Zwyczajne wykresy
#     plt.subplot(1, 3, j)
#     for k in range(7):
#         A = XPCA[Y_real == k]
#         if len(A) > 2:
#             convex_hull = sp.spatial.ConvexHull(A)
#             for simplex in convex_hull.simplices:
#                 plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
#         else:
#             plt.plot(A[:, 0], A[:, 1], 'k-')
#
#     j += 1
#     plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_real)
#     plt.title("ZOO_ksrodki real")
#
#     #Wykresy z klasteryzacją
#     plt.subplot(1, 3, j)
#     for k in range(7):
#         A = XPCA[Y_pred2 == k]
#         if len(A) > 2:
#             convex_hull = sp.spatial.ConvexHull(A)
#             for simplex in convex_hull.simplices:
#                 plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
#         else:
#             plt.plot(A[:, 0], A[:, 1], 'k-')
#     j += 1
#     plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_pred2)
#     plt.title("ZOO_ksrodki Klasteryzacja")
#
#     #Wykresy roznic
#     plt.subplot(1, 3, j)
#     j += 1
#     diff = np.abs(Y_pred2 - Y_real)
#     cmap = plt.get_cmap('coolwarm')
#     plt.scatter(XPCA[:, 0], XPCA[:, 1],   c=diff, cmap=cmap)
#     plt.title("ZOO_ksrodki Różnice")
#     plt.savefig("ZOO_ksrodki_2D.png")
#     plt.show()
#
# for i in range(1):
#     j = 0
#     C, Y_pred = ksrodki(XPCA2, 3)
#     Y_pred = Y_pred.astype(int)
#     Y_pred2 = np.array(find_perm(3, Y_real, Y_pred))
#     print(linkages[i])
#     print(find_perm(3, Y_real, Y_pred))
#
#     fig, ax = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'projection': '3d'})
#
#     #Zwyczajne wykresy
#     ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_real)
#     ax[j].set_title("ZOO_Real")
#     j += 1
#
#
#     #Wykresy z klasteryzacją
#     ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_pred2)
#     ax[j].set_title("ZOO_ksrodki Klasteryzacja")
#     j += 1
#
#
#     #Wykresy roznic
#     diff = np.abs(Y_pred2 - Y_real)
#     cmap = plt.get_cmap('coolwarm')
#     ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2],  c=diff, cmap=cmap)
#     ax[j].set_title("ZOO_ksrodki Różnice")
#     plt.savefig("ZOO_ksrodki3D.png")
#
#     # Wykres dendrogramu
#     plt.figure(figsize=(10, 7))
#     dendrogram(linkage(X, method=linkages[i]))
#     plt.title('ZOO_ksrodki Dendrogram - ' + linkages[i])
#     plt.savefig("ZOO_ksrodki3D_dendrogram.png")
#     plt.show()

#GaussianMixture
for i in range(1):
    j = 1
    clustering = GaussianMixture(n_components=7)
    Y_pred = clustering.fit_predict(X)
    Y_pred2 = np.array(find_perm(7, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(7, Y_real, Y_pred))
    plt.figure(figsize=(18, 6))

    #Zwyczajne wykresy
    plt.subplot(1, 3, j)
    for k in range(7):
        A = XPCA[Y_real == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')

    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_real)
    plt.title("ZOO_GaussianMixture real")

    #Wykresy z klasteryzacją
    plt.subplot(1, 3, j)
    for k in range(7):
        A = XPCA[Y_pred2 == k]
        if len(A) > 2:
            convex_hull = sp.spatial.ConvexHull(A)
            for simplex in convex_hull.simplices:
                plt.plot(A[simplex, 0], A[simplex, 1], 'k-')
        else:
            plt.plot(A[:, 0], A[:, 1], 'k-')
    j += 1
    plt.scatter(XPCA[:, 0], XPCA[:, 1], c=Y_pred2)
    plt.title("ZOO_GaussianMixture Klasteryzacja")

    #Wykresy roznic
    plt.subplot(1, 3, j)
    j += 1
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    plt.scatter(XPCA[:, 0], XPCA[:, 1],  c=diff, cmap=cmap)
    plt.title("ZOO_GaussianMixture Różnice")
    plt.savefig("ZOO_GaussianMixture_2D.png")
    plt.show()

for i in range(1):
    j = 0
    clustering = GaussianMixture(n_components=7)
    Y_pred = clustering.fit_predict(X)
    Y_pred2 = np.array(find_perm(7, Y_real, Y_pred))
    print(linkages[i])
    print(find_perm(7, Y_real, Y_pred))

    fig, ax = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'projection': '3d'})

    #Zwyczajne wykresy
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_real)
    ax[j].set_title("ZOO_GaussianMixture Real")
    j += 1


    #Wykresy z klasteryzacją
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2], c=Y_pred2)
    ax[j].set_title("ZOO_GaussianMixture Klasteryzacja")
    j += 1


    #Wykresy roznic
    diff = np.abs(Y_pred2 - Y_real)
    cmap = plt.get_cmap('coolwarm')
    ax[j].scatter(XPCA2[:, 0], XPCA2[:, 1], XPCA2[:, 2],  c=diff, cmap=cmap)
    ax[j].set_title("ZOO_GaussianMixture Różnice")
    plt.savefig("ZOO_GaussianMixture3D.png")

    # Wykres dendrogramu
    plt.figure(figsize=(10, 7))
    dendrogram(linkage(X, method=linkages[i]))
    plt.title('ZOO_GaussianMixture Dendrogram - ' + linkages[i])
    plt.savefig("ZOO_GaussianMixture3D_dendrogram.png")

    plt.show()


#Kwantyzacja
img = plt.imread("obraz.jpeg")
height, width, channels = img.shape
image_vectorized = np.reshape(img, (height * width, channels))
print(image_vectorized.shape)

cluster_sizes = [2, 3, 5, 10, 30, 100]
date = pd.DataFrame(columns=['klastry', 'blad'])
for k in cluster_sizes:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(image_vectorized)
    labels = kmeans.labels_
    C = kmeans.cluster_centers_
    img_quant = np.zeros(image_vectorized.shape, dtype=np.uint8)
    for j in range(len(image_vectorized)):
        img_quant[j, :] = C[labels[j], :]

    img_restored = np.reshape(img_quant, (height, width, channels))

    blad = sklearn.metrics.mean_squared_error(img.flatten(), img_restored.flatten())
    date = pd.concat([date, pd.DataFrame([[k, blad]], columns=['klastry', 'blad'])])


    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Original")
    plt.subplot(1, 2, 2)
    plt.imshow(img_restored)
    plt.title("Quantized, k = " + str(k))
    plt.savefig("KMEAN_obraz_k=" + str(k) + ".png")
    plt.show()

print(date)

date2 = pd.DataFrame(columns=['klastry', 'blad'])
for k in cluster_sizes:
    GMM = GaussianMixture(n_components=k)
    GMM.fit(image_vectorized)
    labels = GMM.predict(image_vectorized)
    C = GMM.means_
    img_quant = np.zeros(image_vectorized.shape, dtype=np.uint8)
    for j in range(len(image_vectorized)):
        img_quant[j, :] = C[labels[j], :]

    img_restored = np.reshape(img_quant, (height, width, channels))

    blad = sklearn.metrics.mean_squared_error(img.flatten(), img_restored.flatten())
    date2 = pd.concat([date2, pd.DataFrame([[k, blad]], columns=['klastry', 'blad'])])


    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Original")
    plt.subplot(1, 2, 2)
    plt.imshow(img_restored)
    plt.title("Quantized, k = " + str(k))
    plt.savefig("GMM_obraz_k=" + str(k) + ".png")
    plt.show()

print(date2)
