import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

plik = pd.read_csv("zoo.csv")

'''zad1'''
def freq(x, prob = True):
    xi = np.unique(x)
    pi = x.value_counts(normalize=prob)
    return xi, pi.to_numpy()


[xi,pi] = freq(plik["type"])
print(xi)
print(pi)

'''zad2'''
def freq2(x, y, prob=True):
    xi = np.unique(x)
    yi = np.unique(y)
    ni = np.zeros((len(xi), len(yi)))
    for i, x_val in enumerate(xi):
        for j, y_val in enumerate(yi):
            if prob:
                ni[i, j] = np.sum((x == x_val) & (y == y_val)) / len(x)
            else:
                ni[i, j] = np.sum((x == x_val) & (y == y_val))

    return xi, yi, ni


[xi,yi,ni] = freq2(plik["type"],plik["hair"])
print(xi,yi,ni,sep='\n')

'''zad3'''
def entropy(x,y=False):

    if y is False:
        xi,pi = freq(x)
        sum = 0
        for i in range(len(pi)):
            if pi[i] > 0:
                sum += pi[i] * np.log2(pi[i])
        return -sum
    else:
        xi,yi,ni = freq2(x,y)
        sum = 0
        for i in range(len(ni)):
            for j in range(len(ni[i])):
                if ni[i][j] > 0:
                    sum += ni[i][j] * np.log2(ni[i][j])
        return -sum



def infogain(x,y):
    return entropy(x) + entropy(y) - entropy(x,y)
names = plik.columns
print(entropy(plik["type"]))
print(infogain(plik["eggs"],plik["milk"]))




