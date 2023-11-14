import math as m
import numpy as np
import matplotlib.pyplot as plt



def koderHamminga(liczbaBin, n):
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



