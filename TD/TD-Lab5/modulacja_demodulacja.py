#kod zrealizowany w wspłpracy z Krystianem Kacprzakiem

import math as m
import matplotlib.pyplot as plt
import numpy as np


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
tekst = ASCIIToBinary("abc") #tekst do przesłania
print(tekst) #tekst w postaci binarnej
dlugosc = len(tekst)  #dlugosc tekstu
Tb = 1 #czas trwania bitu
Tc = Tb*len(tekst) #czas trwania całego ciągu
fn = W * Tb**-1 #częstotliwość nośnej
fn1 = (W + 1)/Tb #częstotliwość nośnej
fn2 = (W + 2)/Tb #częstotliwość nośnej
fs = 2**10 #częstotliwość próbkowania
A1 = 2 #amplituda
A2 = 7 #amplituda
N = round(Tc * fs) #ilość próbek
NoweN = int(N/dlugosc)*10 #ilość próbek
#tablica = list(range(1, N))
tablica = list(range(1, NoweN)) #tablica próbek

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


t = list(range(1, N+1))
ASK = kluczowanie_amplitudy(t,tekst)
PSK = kluczowanie_fazy(t,tekst)
FSK = kluczowanie_czestotliwosci(t,tekst)


def demodulacjaASK(t,ASK):
    xt = []
    pt = []
    ct = []
    sumpt = 0
    for i in range(len(t)):
        xt.append(ASK[i]*m.sin(2*m.pi*fn*(t[i]/fs)))
    for i in range(len(xt)):
        sumpt += xt[i]
        if i % (N / len(tekst)) == 0:
            pt.append(sumpt)
            sumpt = 0
        else:
            pt.append(sumpt)
    h = 2000
    for i in range(len(pt)):
        if pt[i] > h:
            ct.append(1)
        else:
            ct.append(0)
    return xt, pt, ct

def demodulacjaPSK(t,PSK):
    xt = []
    pt = []
    ct = []
    sumpt = 0
    for i in range(len(t)):
        xt.append(PSK[i]*m.sin(2*m.pi*fn*(t[i]/fs)))
    for i in range(len(xt)):
        sumpt += xt[i]
        if i % (N / len(tekst)) == 0:
            pt.append(sumpt)
            sumpt = 0
        else:
            pt.append(sumpt)
    for i in range(len(pt)):
        if pt[i] < 0:
            ct.append(1)
        else:
            ct.append(0)
    return xt, pt, ct

def demodulacjaFSK(t,FSK):
    xt1 = []
    xt2 = []
    pt1 = []
    pt2 = []
    pt = []
    ct = []
    sumpt = 0
    for i in range(len(t)):
        xt1.append(FSK[i]*m.sin(2*m.pi*fn1*(t[i]/fs)))

    for i in range(len(t)):
        xt2.append(FSK[i]*m.sin(2*m.pi*fn2*(t[i]/fs)))

    for i in range(len(xt1)):
        sumpt += xt1[i]
        if i % (N / len(tekst)) == 0:
            pt1.append(sumpt)
            sumpt = 0
        else:
            pt1.append(sumpt)

    for i in range(len(xt2)):
        sumpt += xt2[i]
        if i % (N / len(tekst)) == 0:
            pt2.append(sumpt)
            sumpt = 0
        else:
            pt2.append(sumpt)

    for i in range(len(pt1)):
        pt.append(pt1[i]-pt2[i])

    for i in range(len(pt)):
        if pt[i] < 0:
            ct.append(1)
        else:
            ct.append(0)

    return xt1, xt2, pt1, pt2, ct


def ct_to_bitstream(ct):
    bitstream = []
    tmpBitstream = []
    bit_len = (N / dlugosc)
    for i in range(len(ct)):
        tmpBitstream.append(ct[i])
        if (i+1) % bit_len == 0 and i != 0:
            if np.mean(tmpBitstream) >= 0.2:
                bitstream.append(1)
            else:
                bitstream.append(0)
            tmpBitstream = []
    return bitstream


xt, pt, ct = demodulacjaASK(t, ASK)

plt.plot(t,ASK)
plt.title("zt")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("ask_z.png")
plt.show()
plt.plot(t,xt)
plt.title("xt")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("ask_x.png")
plt.show()
plt.plot(t,pt)
plt.title("pt")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("ask_p.png")
plt.show()
plt.plot(t,ct)
plt.title("ct")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("ask_c.png")
plt.show()

print(ct_to_bitstream(ct))

xt, pt, ct = demodulacjaPSK(t, PSK)

plt.plot(t,PSK)
plt.title("PSK")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("psk_z.png")
plt.show()
plt.plot(t,xt)
plt.title("xt")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("psk_x.png")
plt.show()
plt.plot(t,pt)
plt.title("pt")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("psk_p.png")
plt.show()
plt.plot(t,ct)
plt.title("ct")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("psk_c.png")
plt.show()

print(ct_to_bitstream(ct))

xt1, xt2, pt1, pt2, ct = demodulacjaFSK(t, FSK)

plt.plot(t,FSK)
plt.title("FSK")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("fsk_z.png")
plt.show()
plt.plot(t,xt1)
plt.title("xt1")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("fsk_x1.png")
plt.show()
plt.plot(t,xt2)
plt.title("xt2")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("fsk_x2.png")
plt.show()
plt.plot(t,pt1)
plt.title("pt1")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("fsk_p1.png")
plt.show()
plt.plot(t,pt2)
plt.title("pt2")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("fsk_p2.png")
plt.show()
plt.plot(t,ct)
plt.title("ct")
plt.ylabel("wartosc sygnalu")
plt.xlabel("probki")
plt.savefig("fsk_c.png")
plt.show()

print(ct_to_bitstream(ct))

