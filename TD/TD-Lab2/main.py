#Wspolpraca z Krystian Kacprzak
import math as m
import matplotlib.pyplot as plt
fs = 2**8
Tc = 1
N = round(Tc * fs)
T = Tc/N
f = 440
x = []
y = []
z = []
v = []
u = []
b1 = []
b2 = []
b3 = []


def xfun(t, fi=2):
    return (1-t)*m.sin(2*m.pi*f*t+fi)*m.cos(4*m.pi*t)
def yfun(t):
    return m.cos(2*m.sqrt(t*(m.sin(m.pi*(t**2))+2*m.pi)/3))
def zfun(t):
    return yfun(t)*(m.sin(0.2*m.pi*t)*abs(xfun(t)/5))
def vfun(t):
    return m.sqrt(abs(xfun(t)))*m.cos(0.5*yfun(t))+zfun(t)
def ufun(t):
    if 0 <= t < 0.22:
        return (1-7*t)*m.sin(2*m.pi*t*10/(t+0.04))
    elif 0.22 <= t < 0.57:
        return 0.63 * t * m.sin(125 * t) + m.log2(2*t)
    elif 0.57 <= t < 0.97:
        return t**(-0.662)+0.77*m.sin(8*t)
def bfun1(t):
    sum = 0
    for h in range(1,2):
        sum += m.cos(4*m.pi*h*t)/4*h*(m.sin(8*m.pi*h*t)+2)
    return sum
def bfun2(t):
    sum = 0
    for h in range(1,6):
        sum += m.cos(4*m.pi*h*t)/4*h*(m.sin(8*m.pi*h*t)+2)
    return sum
def bfun3(t):
    sum = 0
    for h in range(1,51):
        sum += m.cos(4*m.pi*h*t)/4*h*(m.sin(8*m.pi*h*t)+2)
    return sum


for i in range(0, N):
    x.append(xfun(i/fs))
    y.append(yfun(i/fs))
    z.append(zfun(i/fs))
    v.append(vfun(i/fs))
    #u.append(ufun(i/fs))
    b1.append(bfun1(i/fs))
    b2.append(bfun2(i/fs))
    b3.append(bfun3(i/fs))




def DFT(x):
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
tablicaY = DFT(y)
tablicaZ = DFT(z)
tablicaV = DFT(v)
#tablicaU = DFT(u)
tablicaB1 = DFT(b1)
tablicaB2 = DFT(b2)
tablicaB3 = DFT(b3)



def Mfun(k, tablica):
    return m.sqrt(tablica[k][0]**2 + tablica[k][1]**2)


def MPfun(k, tablica):
    return 10 * m.log10(Mfun(k, tablica))


def Fkfun(k):
    return k * fs / N


def all(tablica):
    amplitude = []
    decibel = []
    frequency = []
    for i in range(int((N/2)-1)):
        amplitude.append(Mfun(i, tablica))
        decibel.append(MPfun(i, tablica))
        frequency.append(Fkfun(i))
    return amplitude, decibel, frequency

print(all(tablica))

amplitude, decibel, frequency = all(tablica)
amplitudeY, decibelY, frequencyY = all(tablicaY)
amplitudeZ, decibelZ, frequencyZ = all(tablicaZ)
amplitudeV, decibelV, frequencyV = all(tablicaV)
#amplitudeU, decibelU, frequencyU = all(tablicaU)
amplitudeB1, decibelB1, frequencyB1 = all(tablicaB1)
amplitudeB2, decibelB2, frequencyB2 = all(tablicaB2)
amplitudeB3, decibelB3, frequencyB3 = all(tablicaB3)
plt.figure()
plt.plot(frequency, decibel)
plt.savefig("x.png")
plt.show()
plt.plot(frequencyY, decibelY)
plt.savefig("y.png")
plt.show()
plt.plot(frequencyZ, decibelZ)
plt.savefig("z.png")
plt.show()
plt.plot(frequencyV, decibelV)
plt.savefig("v.png")
plt.show()
# plt.plot(frequencyU, decibelU)
# plt.savefig("u.png")
# plt.show()
plt.plot(frequencyB1, decibelB1)
plt.savefig("b1.png")
plt.show()
plt.plot(frequencyB2, decibelB2)
plt.savefig("b2.png")
plt.show()
plt.plot(frequencyB3, decibelB3)
plt.savefig("b3.png")
plt.show()



