import math as m
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

fm = 900 # czestotliwosc sygnalu modulujacego
fn = 10000 # czestotliwosc sygnalu nosnego
fs = 2**15 # czestotliwosc probkowania
Tc = 2**-7 # czas trwania sygnalu
N = round(Tc * fs) # liczba probek
T = Tc/N # czas pomiedzy probkami
x = [] # wektor czasu

# sygnaly modulowane amplitudowo
za_a = []
za_b = []
za_c = []
zp_a = []
zp_b = []
zp_c = []
zf_a = []
zf_b = []
zf_c = []


def mfun(t): # sygnal modulujacy
    return m.sin(2*m.pi*fm*t)


def m_amplitudowa(t, ka): # sygnal modulowany amplitudowo
    return (ka * mfun(t) + 1) * m.cos(2*m.pi*fn*t)


def m_fazowa(t, kp): # sygnal modulowany fazowo
    return m.cos(2*m.pi*fn*t + kp * mfun(t))


def m_czestotliwosci(t, kf): # sygnal modulowany czestotliwoscia
    return m.cos(2*m.pi*fn*t+kf/fm*mfun(t))


def DFT(x): # transformata Fouriera
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


def Mfun(k, tablica): # amplituda widma
    return m.sqrt(tablica[k][0]**2 + tablica[k][1]**2)


def MPfun(k, tablica): # moc widma
    return 10 * m.log10(Mfun(k, tablica))


def Fkfun(k): # czestotliwosc widma
    return k * fs / N


def all(tablica): # wszystkie funkcje
    amplitude = []
    decibel = []
    frequency = []
    for i in range(int((N/2)-1)):
        amplitude.append(Mfun(i, tablica)) # amplituda widma
        decibel.append(MPfun(i, tablica)) # moc widma
        frequency.append(Fkfun(i)) # czestotliwosc widma
    return amplitude, decibel, frequency


def szerokosc_pasma_3(tablica, frequency):
    funkcja_interpolacji = np.linspace(frequency[0], frequency[-1], len(frequency)*10)
    widmo_interpolowane = sp.interpolate.interp1d(frequency, tablica)(funkcja_interpolacji)
    maxdB = max(widmo_interpolowane)
    fmin = 0
    fmax = 0
    sredania_3 = maxdB - 3
    for i in range(len(widmo_interpolowane)):
        if widmo_interpolowane[i] >= sredania_3:
            if fmin == 0:
                fmin = funkcja_interpolacji[i]
            fmax = funkcja_interpolacji[i]
    B3dB = fmax - fmin
    return B3dB


def szerokosc_pasma_6(tablica, frequency):
    funkcja_interpolacji = np.linspace(frequency[0], frequency[-1], len(frequency)*10)
    widmo_interpolowane = sp.interpolate.interp1d(frequency, tablica)(funkcja_interpolacji)
    maxdB = max(widmo_interpolowane)
    fmin =0
    fmax = 0
    sredania_6 = maxdB - 6
    for i in range(len(widmo_interpolowane)):
        if widmo_interpolowane[i] >= sredania_6:
            if fmin == 0:
                fmin = funkcja_interpolacji[i]
            fmax = funkcja_interpolacji[i]
    B6dB = fmax - fmin
    return B6dB


def szerokosc_pasma_12(tablica, frequency):
    funkcja_interpolacji = np.linspace(frequency[0], frequency[-1], len(frequency)*10)
    widmo_interpolowane = sp.interpolate.interp1d(frequency, tablica)(funkcja_interpolacji)
    maxdB = max(widmo_interpolowane)
    fmin = 0
    fmax = 0
    sredania_12 = maxdB - 12
    for i in range(len(widmo_interpolowane)):
        if widmo_interpolowane[i] >= sredania_12:
            if fmin == 0:
                fmin = funkcja_interpolacji[i]
            fmax = funkcja_interpolacji[i]
    B12dB = fmax - fmin
    return B12dB


for i in range(N):
    x.append(i)
    za_a.append(m_amplitudowa(i/fs, 0.5))
    za_b.append(m_amplitudowa(i/fs, 5))
    za_c.append(m_amplitudowa(i/fs, 25))
    zp_a.append(m_fazowa(i/fs, 0.25))
    zp_b.append(m_fazowa(i/fs, 1))
    zp_c.append(m_fazowa(i/fs, 8))
    zf_a.append(m_czestotliwosci(i/fs, 0.5))
    zf_b.append(m_czestotliwosci(i/fs, 1))
    zf_c.append(m_czestotliwosci(i/fs, 8))


tablica = DFT(za_a)
tablica1 = DFT(za_b)
tablica2 = DFT(za_c)
tablica3 = DFT(zp_a)
tablica4 = DFT(zp_b)
tablica5 = DFT(zp_c)
tablica6 = DFT(zf_a)
tablica7 = DFT(zf_b)
tablica8 = DFT(zf_c)

amplitude, decibel, frequency = all(tablica)
amplitude1, decibel1, frequency1 = all(tablica1)
amplitude2, decibel2, frequency2 = all(tablica2)
amplitude3, decibel3, frequency3 = all(tablica3)
amplitude4, decibel4, frequency4 = all(tablica4)
amplitude5, decibel5, frequency5 = all(tablica5)
amplitude6, decibel6, frequency6 = all(tablica6)
amplitude7, decibel7, frequency7 = all(tablica7)
amplitude8, decibel8, frequency8 = all(tablica8)

plt.figure()
plt.plot(frequency, decibel)
plt.savefig("za_a.png")
plt.show()
plt.plot(frequency1, decibel1)
plt.savefig("za_b.png")
plt.show()
plt.plot(frequency2, decibel2)
plt.savefig("za_c.png")
plt.show()
plt.plot(frequency3, decibel3)
plt.savefig("zp_a.png")
plt.show()
plt.plot(frequency4, decibel4)
plt.savefig("zp_b.png")
plt.show()
plt.plot(frequency5, decibel5)
plt.savefig("zp_c.png")
plt.show()
plt.plot(frequency6, decibel6)
plt.savefig("zf_a.png")
plt.show()
plt.plot(frequency7, decibel7)
plt.savefig("zf_b.png")
plt.show()
plt.plot(frequency8, decibel8)
plt.savefig("zf_c.png")
plt.show()

print("szerokosc pasma 3 za_a: ", szerokosc_pasma_3(decibel, frequency))
print("szerokosc pasma 6 za_a: ", szerokosc_pasma_6(decibel, frequency))
print("szerokosc pasma 12 za_a: ", szerokosc_pasma_12(decibel, frequency))
print("\n")
print("szerokosc pasma 3 za_b: ", szerokosc_pasma_3(decibel1, frequency1))
print("szerokosc pasma 6 za_b: ", szerokosc_pasma_6(decibel1, frequency1))
print("szerokosc pasma 12 za_b: ", szerokosc_pasma_12(decibel1, frequency1))
print("\n")
print("szerokosc pasma 3 za_c: ", szerokosc_pasma_3(decibel2, frequency2))
print("szerokosc pasma 6 za_c: ", szerokosc_pasma_6(decibel2, frequency2))
print("szerokosc pasma 12 za_c: ", szerokosc_pasma_12(decibel2, frequency2))
print("\n")
print("szerokosc pasma 3 zp_a: ", szerokosc_pasma_3(decibel3, frequency3))
print("szerokosc pasma 6 zp_a: ", szerokosc_pasma_6(decibel3, frequency3))
print("szerokosc pasma 12 zp_a: ", szerokosc_pasma_12(decibel3, frequency3))
print("\n")
print("szerokosc pasma 3 zp_b: ", szerokosc_pasma_3(decibel4, frequency4))
print("szerokosc pasma 6 zp_b: ", szerokosc_pasma_6(decibel4, frequency4))
print("szerokosc pasma 12 zp_b: ", szerokosc_pasma_12(decibel4, frequency4))
print("\n")
print("szerokosc pasma 3 zp_c: ", szerokosc_pasma_3(decibel5, frequency5))
print("szerokosc pasma 6 zp_c: ", szerokosc_pasma_6(decibel5, frequency5))
print("szerokosc pasma 12 zp_c: ", szerokosc_pasma_12(decibel5, frequency5))
print("\n")
print("szerokosc pasma 3 zf_a: ", szerokosc_pasma_3(decibel6, frequency6))
print("szerokosc pasma 6 zf_a: ", szerokosc_pasma_6(decibel6, frequency6))
print("szerokosc pasma 12 zf_a: ", szerokosc_pasma_12(decibel6, frequency6))
print("\n")
print("szerokosc pasma 3 zf_b: ", szerokosc_pasma_3(decibel7, frequency7))
print("szerokosc pasma 6 zf_b: ", szerokosc_pasma_6(decibel7, frequency7))
print("szerokosc pasma 12 zf_b: ", szerokosc_pasma_12(decibel7, frequency7))
print("\n")
print("szerokosc pasma 3 zf_c: ", szerokosc_pasma_3(decibel8, frequency8))
print("szerokosc pasma 6 zf_c: ", szerokosc_pasma_6(decibel8, frequency8))
print("szerokosc pasma 12 zf_c: ", szerokosc_pasma_12(decibel8, frequency8))





