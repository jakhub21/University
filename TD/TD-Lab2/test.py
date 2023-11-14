import math as m
import matplotlib.pyplot as plt
fs = 16
Tc = 1
N = round(Tc * fs)
T = Tc/N
f = 440
x = []
y = []


def xfun(t, fi=2):
    return (1-t)*m.sin(2*m.pi*f*t+fi)*m.cos(4*m.pi*t)



for i in range(0, N):
    x.append(xfun(i/fs))


def DFT(k):
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

tablica = DFT(x)


def Mfun(k):
    return m.sqrt(tablica[k][0]**2 + tablica[k][1]**2)


def MPfun(k):
    return 10 * m.log10(Mfun(k))


def Fkfun(k):
    return k * fs / N


def all(k):
    amplitude = []
    decibel = []
    frequency = []
    for i in range(int((N/2)-1)):
        amplitude.append(Mfun(i))
        decibel.append(MPfun(i))
        frequency.append(Fkfun(i))
    return amplitude, decibel, frequency

amplitude, decibel, frequency = all(y)
plt.plot(frequency, decibel)
plt.savefig("widmo.png")
plt.show()


print(DFT(x))
print(all(y))