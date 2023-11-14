import math as m
import matplotlib.pyplot as plt
import numpy as np
N = 16
x = []
y = []
fs = 500

for i in range(N):
    x.append(i)

def FFT(x):
    N = len(x)

    if N == 1:
        return x
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = \
            np.exp(-2j * np.pi * np.arange(N) / N)

        X = np.concatenate( \
            [X_even + factor[:int(N / 2)] * X_odd,
             X_even + factor[int(N / 2):] * X_odd])
        return X



print(FFT(x))
