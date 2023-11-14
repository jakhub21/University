import math as m
import matplotlib.pyplot as plt
fm = 10
fn = 100
fs = 250
Tc = 0.1
N = round(Tc * fs)
T = Tc/N
x = []
y = []

def mfun(t):
    return m.sin(2*m.pi*fm*t)


def m_amplitudowa(t, ka):
    return (ka * mfun(t) + 1) * m.cos(2*m.pi*fn*t)


def m_fazowa(t, kp):
    return m.cos(2*m.pi*fn*t + kp * mfun(t))


def m_czestotliwosci(t, kf):
    return m.cos(2*m.pi*fn*t+kf/fm*mfun(t))

for i in range(N):
    x.append(i/fs)
    y.append(m_fazowa(i/fs, 0.5))

