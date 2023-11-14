#Wspolpraca z Krystian Kacprzak
import math as m
import matplotlib.pyplot as plt
import numpy as np
import time as t
N = 2**8
x = []
y = []
fs = 500

for i in range(N):
    x.append(i)


start = t.time()
def Xfun(k):
    ImRe = []
    for k in range(N):
        sumRe = 0
        sumIm = 0
        for n in range(N):
            sumRe += x[n] * m.cos((-2 * m.pi * n * k)/N)
            sumIm += x[n] * m.sin((-2 * m.pi * n * k)/N)
        sum = (sumRe, sumIm)
        ImRe.append(sum)
    return ImRe
end = t.time()


start1 = t.time()
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
end1 = t.time()


print(FFT(x))
print(Xfun(x))
print(end - start)
print(end1 - start1)