from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.metrics import mean_squared_error



def wiPCA(data, n_components):
    mean_vec = np.mean(data, axis=0)
    centered_data = data - mean_vec
    cov_matrix = np.cov(centered_data.T)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    selected_eigenvectors = sorted_eigenvectors[:, :n_components]
    reduced_data = np.dot(centered_data, selected_eigenvectors)
    return reduced_data, selected_eigenvectors, sorted_eigenvalues, mean_vec


#zadanie 1

data = np.random.randn(200, 2)
reduced_data, eigenvectors, eigenvalues, mean_vec = wiPCA(data, 1)
plt.scatter(data[:, 0], data[:, 1])
plt.quiver(mean_vec[0], mean_vec[1], eigenvectors[0, 0], eigenvectors[1, 0], scale=5, color='red')
plt.scatter(reduced_data[:, 0], np.zeros_like(reduced_data[:, 0]), color='green')
plt.savefig('pca.png')
plt.show()

#zadanie 2
iris = load_iris()
data = iris.data
target = iris.target


reduced_data, _, _, _ = wiPCA(data, 2)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
colors = ['red', 'green', 'blue']


for i in range(len(target)):
    ax1.scatter(reduced_data[i, 0], reduced_data[i, 1], color=colors[target[i]])

ax1.set_title('WiPCA Iris')

pca_sklearn = PCA(n_components=2)
reduced_data_sklearn = pca_sklearn.fit_transform(data)

for i in range(len(target)):
    ax2.scatter(reduced_data_sklearn[i, 0], reduced_data_sklearn[i, 1], color=colors[target[i]])

ax2.set_title('sklearn Iris')
plt.tight_layout()
plt.savefig('iris.png')
plt.show()

#zadanie 3

digits = load_digits()
data = digits.data
target = digits.target
reduced_data, _, eigenvalues, _ = wiPCA(data, 2)
explained_variance_ratio = np.cumsum(eigenvalues) / np.sum(eigenvalues)
plt.plot(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio)
plt.savefig('digit1.png')
plt.show()
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=target, cmap='tab10')
plt.colorbar()
plt.title('Digit')
plt.savefig('digit2.png')
plt.show()

minShape = min(data.shape)
err = np.zeros(minShape)
for i in range(minShape):
    ret, ret_vectors, _, ret_mean = wiPCA(digits['data'], i + 1)
    ret_rec = np.dot(ret[:minShape, :], ret_vectors[:minShape, :i + 1].T) + ret_mean
    err[i] = mean_squared_error(digits['data'][:minShape], ret_rec)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(np.arange(minShape), err)
plt.savefig('blad_rekonstrukcji.png')
plt.show()
