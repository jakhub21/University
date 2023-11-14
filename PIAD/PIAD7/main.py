import numpy as np
from scipy.stats import mode
import sklearn.datasets as sk
import sklearn.neighbors as sn
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.model_selection import LeaveOneOut
from scipy.spatial.distance import cdist
# from sklearn.datasets import load_boston
import timeit


class knn():
    def __init__(self, n_neighbours=3, useKDTree = False, classifier = False):
        self.n_neighbours = n_neighbours
        self.useKDTree = useKDTree
        self.classifier = classifier

    def fit(self, X, y):
        self.X = X
        self.y = y
        if self.useKDTree:
            self.tree = sn.KDTree(X)
        else:
            self.tree = None

    def predict(self, X):
        lenght = np.zeros(len(X))
        if self.useKDTree:
            _, idx = self.tree.query(X, k=self.n_neighbours)
            for i in range(len(X)):
                tmp = self.y[idx[i]]
                if self.classifier:
                    lenght[i] = mode(tmp,keepdims=True)[0]
                else:
                    lenght[i] = np.mean(tmp)
            return lenght
        else:
            tmp_sum = cdist(X, self.X)
            for i in range(len(X)):
                idx = np.argsort(tmp_sum[i, :])[:self.n_neighbours]
                tmp = self.y[idx]
                if self.classifier:
                    lenght[i] = mode(tmp,keepdims=True)[0]
                else:
                    lenght[i] = np.min(tmp)
            return lenght

    def score(self, X, y):
        tmp = self.predict(X)
        if self.classifier:
            return (np.sum(tmp == y) / len(y))*100
        else:
            return np.sqrt(np.sum((tmp - y) ** 2) / len(y))


X, y = sk.make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_repeated=0, random_state=3)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

kNN = knn(classifier=True)
kNN.fit(X, y)
print(kNN.score(X, y))

h = 0.02
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

Z = kNN.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure()
plt.contour(xx, yy, Z)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title('Klasyfikator kNN')
plt.savefig('knn.png')
plt.show()

#iris
data = load_iris()
X = data.data
Y = data.target

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
kNN = knn(classifier=True)
kNN.fit(X_pca, Y)

h = 0.02
x_min, x_max = X_pca[:, 0].min() - 1, X_pca[:, 0].max() + 1
y_min, y_max = X_pca[:, 1].min() - 1, X_pca[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

grid_points = np.c_[xx.ravel(), yy.ravel()]
original_space_points = pca.inverse_transform(grid_points)
Z = kNN.predict(grid_points)
Z = Z.reshape(xx.shape)

plt.figure()
plt.contour(xx, yy, Z)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=Y)
plt.title('Iris')
plt.savefig('iris.png')
plt.show()

#leave one out
k_values = [1, 3, 5, 7, 9]
results = []
loo = LeaveOneOut()
for k in k_values:
    errors = []
    for train_index, test_index in loo.split(X):
        X_train, X_test = X[train_index], X[test_index]
        Y_train, Y_test = Y[train_index], Y[test_index]
        kNN = knn()
        kNN.fit(X_train, Y_train)
        score = kNN.score(X_test, Y_test)
        errors.append(1 - score)
    mean_error = np.mean(errors)
    results.append(mean_error)

for i in range(len(k_values)):
    print(f"{k_values[i]:^11} | {results[i]:^11.4f}")

kNN_basic = knn(3, False, True)
kNN_basic.fit(X, Y)
kNN_kdtree = knn(3, True, True)
kNN_kdtree.fit(X, Y)


def time(model, X):
    start_time = timeit.default_timer()
    model.predict(X)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return execution_time

execution_time_basic = time(kNN_basic, X)
print("Czas wykonania dla wersji podstawowej: {:.6f} sekundy".format(execution_time_basic))
execution_time_kdtree = time(kNN_kdtree, X)
print("Czas wykonania dla wersji z kD-Drzewem: {:.6f} sekundy".format(execution_time_kdtree))

#regresja
X = np.random.rand(500, 1) * 100
y = 3*X + 100 * np.random.rand(500, 1) - 50
kNN = knn(10, True)
kNN.fit(X, y)
tmp = np.linspace(0, 100, 500)
y_pred = kNN.predict(tmp.reshape(-1, 1))
plt.scatter(X, y)
plt.plot(tmp, y_pred, 'r-')
plt.title('Regresja')
plt.savefig('regresja.png')
plt.show()
print(f"Błąd popełniany przez model: {kNN.score(X, y)}")


#boston
# boston = load_boston()
# X = boston.data
# y = boston.target
#
# print("Opis zbioru danych Boston:")
# print(boston.DESCR)