#kod zrealizowany w wspłpracy z Krystianem Kacprzakiem

import math as m
import numpy as np
import matplotlib.pyplot as plt


#Hamming (7,4)
n = 7
k = 4
liczbaBin = [1, 0, 1, 1]


def koderHamminga(liczbaBin):
    koder = np.zeros(n).astype(int)
    koder[2] = liczbaBin[0]
    koder[4] = liczbaBin[1]
    koder[5] = liczbaBin[2]
    koder[6] = liczbaBin[3]
    koder[0] = (koder[2] + koder[4] + koder[6]) % 2
    koder[1] = (koder[2] + koder[5] + koder[6]) % 2
    koder[3] = (koder[4] + koder[5] + koder[6]) % 2
    return koder


def dekoderHamminga(koder):
    x1 = koder[0] ^ ((koder[2] ^ koder[4]) ^ koder[6])
    x2 = koder[1] ^ ((koder[2] ^ koder[5]) ^ koder[6])
    x3 = koder[3] ^ ((koder[4] ^ koder[5]) ^ koder[6])
    Suma = x1 + x2 * 2 + x3 * 4
    if Suma == 0:
        return [koder[2], koder[4], koder[5], koder[6]]
    else:
        koder[Suma - 1] = (koder[Suma - 1] + 1) % 2
        return [koder[2], koder[4], koder[5], koder[6]]


# print(liczbaBin)
# x = koderHamminga(liczbaBin)
# print(x)
# x[5] = not x[5]
# print(x)
# y = dekoderHamminga(x)
# print(y)


def kodHamminga(n,k):
    pass


def decToBin(n):
    bin = np.zeros(m).astype(int)
    i = 0
    while n > 0:
        bin[m-1-i] = n % 2
        n = n // 2
        i += 1
    return bin

# Hamming (15,11)
n = 15
k = 11
m = n-k
I = np.eye(k).astype(int)
Pkodowanie = []
b = [1,0,1,1,0,1,1,1,1,0,0]
wykluczane = []
for i in range(0, m):
    wykluczane.append(2**i)

for i in range(1, n+1):
    if i not in wykluczane:
        Pkodowanie.append(decToBin(i))

Pkodowanie = np.array(Pkodowanie)
Pkodowanie = np.flip(Pkodowanie, axis=1)

print(wykluczane)
# print(Pkodowanie)
# print(I)
G = np.concatenate((Pkodowanie, I),axis=1)
# print(G)

#kodowanie binarne
c = np.dot(b,G) % 2
print(c)

c[2] = not c[2]

I2 = np.identity(m).astype(int)
H = np.concatenate((I2, np.transpose(Pkodowanie)), axis=1)
print(np.transpose(H))
print(c)
s = np.dot(c, np.transpose(H)) % 2
# print(I2)
# print(H)
print(s)
S = 0
for i in range(len(s)):
    S += s[i] * 2**i
if S != 0:
    c[S-1] = np.bitwise_not(c[S-1])

print(c[4:])
print(b)
