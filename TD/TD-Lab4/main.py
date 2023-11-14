#kod zrealizowany w współpracy z Krystianem Kacprzakiem

import math as m
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def ASCIIToBinary(tekst):
    arr = []
    for i in tekst:
        i = ord(i)
        tmp = f'{i:b}'.zfill(7)
        tmp = tmp.lstrip('0b')
        tmp = list(tmp)
        arr.extend(tmp)
    return arr


W = 2
tekst = ASCIIToBinary("tekst")
print(tekst)
dlugosc = len(tekst)
Tb = 1
Tc = Tb*len(tekst)
fn = W * Tb**-1
fn1 = (W + 1)/Tb
fn2 = (W + 2)/Tb
fs = 2**16
A1 = 0
A2 = 7
N = round(Tc * fs)
NoweN = int(N/dlugosc)*10
#tablica = list(range(1, N))
tablica = list(range(1, NoweN))




def kluczowanie_amplitudy(t,bn):
    tablica1 = []
    n = 0
    if A1 != A2:
        for i in t:
            if bn[n] == '0':
                tablica1.append(A1*m.sin(2*m.pi*fn*(i/fs)))
            elif bn[n] == '1':
                tablica1.append(A2*m.sin(2*m.pi*fn*(i/fs)))
            if i % (N / len(bn)) == 0:
                n += 1
    return tablica1


def kluczowanie_fazy(t,bn):
    tablica2 = []
    n = 0
    for i in t:
        if bn[n] == '0':
            tablica2.append(m.sin(2 * m.pi * fn * (i/fs)))
        elif bn[n] == '1':
            tablica2.append(m.sin(2 * m.pi * fn * (i/fs) + m.pi))
        if i % (N / len(bn)) == 0:
            n += 1
    return tablica2


def kluczowanie_czestotliwosci(t,bn):
    tablica3 = []
    n = 0
    for i in t:
        if bn[n] == '0':
            tablica3.append(m.sin(2 * m.pi * fn1 * (i/fs)))
        elif bn[n] == '1':
            tablica3.append(m.sin(2 * m.pi * fn2 * (i/fs) ))
        if i % (N / len(bn)) == 0:
            n += 1
    return tablica3


def Mfun(k, tablica): # amplituda widma
    return m.sqrt(tablica[k].real**2 + tablica[k].imag**2)


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

t = list(range(1, N))
tablica1 = kluczowanie_amplitudy(t,tekst)
tablica2 = kluczowanie_fazy(t,tekst)
tablica3 = kluczowanie_czestotliwosci(t,tekst)

plt.plot(t[0:int(NoweN)], tablica1[0:int(NoweN)])
plt.title("kluczowanie amplitudy")
plt.savefig("za.png")
plt.show()
plt.plot(t[0:int(NoweN)], tablica2[0:int(NoweN)])
plt.title("kluczowanie fazy")
plt.savefig("zp.png")
plt.show()
plt.plot(t[0:int(NoweN)], tablica3[0:int(NoweN)])
plt.title("kluczowanie czestotliwosci")
plt.savefig("zf.png")
plt.show()

ZA = np.fft.fft(tablica1)
ZP = np.fft.fft(tablica2)
ZF = np.fft.fft(tablica3)

amplitude, decibel, frequency = all(ZA)
amplitude1, decibel1, frequency1 = all(ZP)
amplitude2, decibel2, frequency2 = all(ZF)


plt.plot(frequency,decibel)
plt.title("ZA")
plt.xscale('log')
plt.ylim(38,70)
plt.savefig("za_widmo.png")
plt.show()
plt.plot(frequency1,decibel1)
plt.title("ZP")
plt.xscale('log')
plt.ylim(40,60)
plt.savefig("zp_widmo.png")
plt.show()
plt.plot(frequency2,decibel2)
plt.title("ZF")
plt.xscale('log')
plt.ylim(30,60)
plt.savefig("zf_widmo.png")
plt.show()



print("szerokosc pasma 3 ASK: ", szerokosc_pasma_3(decibel, frequency))
print("szerokosc pasma 6 ASK: ", szerokosc_pasma_6(decibel, frequency))
print("szerokosc pasma 12 ASK: ", szerokosc_pasma_12(decibel, frequency))
print("\n")
print("szerokosc pasma 3 PSK: ", szerokosc_pasma_3(decibel1, frequency1))
print("szerokosc pasma 6 PSK: ", szerokosc_pasma_6(decibel1, frequency1))
print("szerokosc pasma 12 PSK: ", szerokosc_pasma_12(decibel1, frequency1))
print("\n")
print("szerokosc pasma 3 FSK: ", szerokosc_pasma_3(decibel2, frequency2))
print("szerokosc pasma 6 FSK: ", szerokosc_pasma_6(decibel2, frequency2))
print("szerokosc pasma 12 FSK: ", szerokosc_pasma_12(decibel2, frequency2))