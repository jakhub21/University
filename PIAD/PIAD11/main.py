import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression, Perceptron
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score, roc_auc_score, \
    roc_curve
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier
from sklearn.svm import SVC

# Generowanie przykładowych danych
X, y = make_classification(n_samples=2000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, n_classes=4)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
classifiers = [
    (OneVsOneClassifier(SVC(kernel='linear', probability=True)), "OneVsOne-SVM Linear"),
    (OneVsOneClassifier(SVC(kernel='rbf', probability=True)), "OneVsOne-SVM RBF"),
    (OneVsOneClassifier(LogisticRegression()), "OneVsOne-Logistic Regression"),
    (OneVsOneClassifier(Perceptron()), "OneVsOne-Perceptron"),
    (OneVsRestClassifier(SVC(kernel='linear', probability=True)), "OneVsRest-SVM Linear"),
    (OneVsRestClassifier(SVC(kernel='rbf', probability=True)), "OneVsRest-SVM RBF"),
    (OneVsRestClassifier(LogisticRegression()), "OneVsRest-Logistic Regression"),
    (OneVsRestClassifier(Perceptron()), "OneVsRest-Perceptron")
]
auc_scores = []
list = pd.DataFrame(columns=['Nazwa', 'Accuracy', 'Recall', 'Precision', 'F1', 'AUC'])
for classifier, name in classifiers:
    # Uczenie na zbiorze uczącym
    classifier.fit(X_train, y_train)
    # Predykcja na zbiorze testowym
    y_pred = classifier.predict(X_test)
    plt.figure()
    # Wykres punktowy dla zbioru testowego
    plt.subplot(1, 3, 1)
    # Wykres punktow oczekiwanych
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred)
    plt.title("Oczekiwany")
    # Wykres punktow obliczonych
    plt.subplot(1, 3, 2)
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
    plt.title("Obliczony")
    # Wykres roznic
    plt.subplot(1, 3, 3)
    #oblicznie roznicy pomiedzy wieloma klastrami i wykreslenie ich
    roznica = np.zeros(len(y_test))
    for i in range(len(y_test)):
        if y_test[i] != y_pred[i]:
            roznica[i] = 1
    plt.scatter(X_test[:, 0], X_test[:, 1], c=roznica)
    plt.title("Roznica")
    plt.suptitle(name)
    plt.savefig('wykresy_' + name + '_scatter.png')
    plt.show()

    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='macro')
    precision = precision_score(y_test, y_pred, average='macro')
    f1 = f1_score(y_test, y_pred, average='macro')
    classes = np.unique(y_test)
    auc_scores = []
    for i in range(len(classes)):
        y_test_binary = np.array(y_test == classes[i], dtype=int)
        y_pred_binary = np.array(y_pred == classes[i], dtype=int)
        auc_scores.append(roc_auc_score(y_test_binary, y_pred_binary, multi_class='ovr'))
        fpr, tpr, thresholds = roc_curve(y_test_binary, y_pred_binary, pos_label=1)
        plt.plot(fpr, tpr, label='Klasa %d' % i)
    plt.legend()
    plt.savefig('wykresy_' + name + '_roc.png')
    plt.show()
    auc = np.mean(auc_scores)
    h = 0.02  # krok siatki
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    # Generowanie siatki
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predykcja dla siatki
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure()
    plt.contourf(xx, yy, Z, alpha=0.5)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k')
    plt.savefig('wykresy_' + name + '.png')
    plt.show()

    print("Accuracy: ", accuracy)
    print("Recall: ", recall)
    print("Precision: ", precision)
    print("F1: ", f1)
    print("AUC: ", auc)
    print("Confusion matrix: ")
    print(confusion_matrix(y_test, y_pred))
    print("\n\n")

    cos = pd.DataFrame(data=[{'Nazwa': name,
                        'Accuracy': accuracy,
                        'Recall': recall,
                        'Precision': precision,
                        'F1': f1,
                        'AUC': auc}])

    list = pd.concat((list, cos), ignore_index=True)
    # list = pd.concat([list, pd.DataFrame([[name, accuracy, recall, precision, f1, auc]], columns=['Nazwa', 'Accuracy', 'Recall', 'Precision', 'F1', 'AUC'])], ignore_index=True)

list.set_index('Nazwa', inplace=True)
list.groupby('Nazwa').mean()
list = list.T
print(list)
list.plot.bar(figsize=(10, 5))
plt.legend(loc='lower right')
plt.savefig('bar.png')
plt.show()
