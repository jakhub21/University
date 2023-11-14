import numpy as np
#zad 1
'''x = np.random.randint(100,size=(10,5))
print(np.trace(x))
print(np.diag(x))
print(x)'''
#zad2
'''x = np.random.normal(3,2.5,size= 5)
y = np.random.normal(4,3,size= 5)
print(x*y)'''
#zad3
'''x = np.random.randint(100,size=25)
y = np.random.randint(100,size=25)
x = np.reshape(x,(5,5))
y = np.reshape(y,(5,5))
print(x+y)'''
#zad4
'''x = np.random.randint(100,size=(4,5))
y = np.random.randint(100,size=(5,4))
y = np.transpose(y)
print(x + y)'''
#zad5
'''x = np.random.randint(100,size=(5,5))
y = np.random.randint(100,size=(5,5))
print(x)
print(y)
print(x[3,:]*y[4,:])'''
#zad6
'''x = np.random.normal(10,size=(2,2))
y = np.random.uniform(10,size=(2,2))
print(f"srednia {np.mean(x)} odchylenie standardowe {np.std(x)} wariacja {np.var(x)}")
print(f"srednia {np.mean(y)} odchylenie standardowe {np.std(y)} wariacja {np.var(y)}")'''
#zad7
'''x = np.random.randint(10,size=(2,2))
y = np.random.randint(10,size=(2,2))
print(x)
print(y)
print(x*y)
print(np.dot(x,y))'''
#funkcja dot transonuje macierz y i potem mnozy macierz x * y
#funkcja dot warto uzywac kiedy macierze nie sa kwadratowe i zeby pomnozyc je trzeba je transponowac
#zad8
'''x = np.random.randint(100,size=(5,5))
print(x.strides)
print(np.lib.stride_tricks.as_strided(x, shape=(3,5), strides=x.strides))'''
#zad9
'''a = np.random.randint(100,size=5)
b = np.random.randint(100,size=5)
print(np.vstack((a,b)))
#vstack scala dwa obiekty numpy w macierz
print(np.hstack((a,b)))
#hstack laczy dwa obiekty numpy horyzontalnie'''
#zad10
x = np.arange(0, 24, dtype=np.uint64)
x = x.reshape(4, 6)
print(x)
blok1 = np.lib.stride_tricks.as_strided(x, shape=(2,2,2,3), strides=(96,24,48,8))
print(np.max(blok1[0][0]))
print(np.max(blok1[0][1]))
print(np.max(blok1[1][0]))
print(np.max(blok1[1][1]))

print(x.strides)