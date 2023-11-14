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


def kluczowanie_amplitudy(t,bn,A1,A2,fn,N):
    tablica1 = []
    n = 0
    szerokosc_bitu = N // len(bn)
    if A1 != A2:
        for i in range(len(t)):
            if bn[n] == '0':
                tablica1.append(A1*m.sin(2*m.pi*fn*t[i]))
            elif bn[n] == '1':
                tablica1.append(A2*m.sin(2*m.pi*fn*t[i]))
            if i != 0 and i % (szerokosc_bitu) == 0:
                n += 1
    return tablica1


def kluczowanie_fazy(t, bn, N, fn):
    tablica2 = []
    n = 0
    for i in range(len(t)):
        if bn[n] == '0':
            tablica2.append(m.sin(2 * m.pi * fn * t[i]))
        elif bn[n] == '1':
            tablica2.append(m.sin(2 * m.pi * fn * t[i] + m.pi))
        if i != 0 and i % (N / len(bn)) == 0:
            n += 1
    return tablica2


def kluczowanie_czestotliwosci(t,bn,N,fn1,fn2):
    tablica3 = []
    n = 0
    for i in range(len(t)):
        if bn[n] == '0':
            tablica3.append(m.sin(2 * m.pi * fn1 * t[i]))
        elif bn[n] == '1':
            tablica3.append(m.sin(2 * m.pi * fn2 * t[i]))
        if i != 0 and i % (N / len(bn)) == 0:
            n += 1
    return tablica3


def demodulacjaASK(t,ASK,N,fn,tekst):
    xt = []
    pt = []
    ct = []
    sumpt = 0
    for i in range(len(t)):
        xt.append(ASK[i]*m.sin(2*m.pi*fn*(t[i])))
    for i in range(len(xt)):
        sumpt += xt[i]
        if i % (N / len(tekst)) == 0:
            pt.append(sumpt)
            sumpt = 0
        else:
            pt.append(sumpt)
    h = np.max(pt)/2
    for i in range(len(pt)):
        if pt[i] > h:
            ct.append(1)
        else:
            ct.append(0)
    return xt, pt, ct


def demodulacjaPSK(t, PSK, N, fn, tekst):
    xt = []
    pt = []
    ct = []
    sumpt = 0
    for i in range(len(t)):
        xt.append(PSK[i]*m.sin(2*m.pi*fn*t[i]))
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


def demodulacjaFSK(t,FSK,N,fn1,fn2,fs,tekst):
    xt1 = []
    xt2 = []
    pt1 = []
    pt2 = []
    pt = []
    ct = []
    sumpt = 0
    for i in range(len(t)):
        xt1.append(FSK[i]*m.sin(2*m.pi*fn1*(t[i])))

    for i in range(len(t)):
        xt2.append(FSK[i]*m.sin(2*m.pi*fn2*(t[i])))

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


def ct_to_bitstream(ct, N, dlugosc):
    bitstream = []
    tmpBitstream = []
    bit_len = (N / dlugosc)
    bit_len = int(bit_len)
    for i in range(len(ct)):
        tmpBitstream.append(ct[i])
        if (i+1) % bit_len == 0 and i != 0:
            if np.mean(tmpBitstream) >= 0.2:
                bitstream.append(1)
            else:
                bitstream.append(0)
            tmpBitstream = []
    return bitstream




