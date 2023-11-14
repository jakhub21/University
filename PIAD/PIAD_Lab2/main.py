import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import sklearn
# x = pd.DataFrame({"data":["2020-03-01","2020-03-02","2020-03-03","2020-03-04","2020-03-05"],
#                   "A":np.random.normal(3,2.5,size= 5),
#                   "B":np.random.normal(3,2.5,size= 5),
#                   "C":np.random.normal(3,2.5,size= 5)})
# x = x.set_index("data")
# print(x)

# y = pd.DataFrame({"id":np.arange(1,21),
#                   "A":np.random.randint(0,100,size= 20),
#                   "B":np.random.randint(0,100,size= 20),
#                   "C":np.random.randint(0,100,size= 20)})
# y = y.set_index("id")
#print(y)
#print(y[0:3])
#print(y[17:20])
#print(y.index.name)
#print(y.columns.values)
#print(y.to_string(index=False,header=False))
#print(y.sample(n= 5))
#print(y["A"])
#print(y[["A","B"]])
#print(y.iloc[:3,:2])
#print(y.iloc[[4]])
#print(y.iloc[[0,5,6,7],[1,2]])
#print(y.describe(include='all'))
#print(pd.concat([x,y.T]))
# df = pd.DataFrame({"x":[1, 2, 3, 4, 5], "y":["a", "b", "a", "b", "b"]})
# index = np.arange(5)
# df.index.name="id"
#print(df)
#print(df.sort_index())
#print(df.sort_values(by="y",ascending=False)
# slownik = {"Day": ["Mon", "Tue", "Mon", "Tue", "Mon"],
#           "Fruit": ["Apple","Apple", "Banana", "Banana", "Apple"],
#           "Pound": [10, 15, 50, 40, 5],
#           "Pro-fit":[20, 30, 25, 20, 10]}
# df3 = pd.DataFrame(slownik)
# print(df3)
# print(df3.groupby("Day").sum())
# print(df3.groupby(["Day","Fruit"]).sum())
# df=pd.DataFrame(np.random.randn(20, 3),
#                 index=np.arange(20),
#                 columns=["A’","B","C"])
# df.index.name="id"
# print(df)
#Wykonaj i opisz jak działają poniższe komendy:
# df["B"]=1 #ustawia wszystkie wartosci columny B na 1
# print(df)
# df.iloc[1,2]=10
# print(df)
# df[df!=0]=-df #zamienia wartosci na ujemne jesli nie sa 0
# print(df)

# df.iloc[[0, 3], 1] = np.nan # ustawia wartosc nan dla wartosci 0 i 3 w kolumnie 1
# print(df)
# df.fillna(0, inplace=True) # wypelnia wartosci nan zerem
# print(df)
# df.iloc[[0, 3], 1] = np.nan
# df = df.replace(to_replace=np.nan, value=-9999) # zamienia wardosci nan na -9999
# print(df)
# df.iloc[[0, 3], 1] = np.nan
# print(pd.isnull(df)) # sprawdza czy wartosci sa nulle

df = pd.DataFrame({"x": [1, 2, 3, 4, 5],
                  "y": ["a", "b", "a", "b", "b"]})
# print(df)
'''zad1'''
print(df.groupby("y").mean())
'''zad2'''
print(df.value_counts())#zlicza ile razy wystepuje dana wartosc
'''zad3'''
plik = np.loadtxt("autos.csv",dtype=str,delimiter=",")
plik2 = pd.read_csv("autos.csv")
print(plik)
'''zad4'''
zad4 = plik2.groupby("make").mean()
print(zad4.loc[:,["city-mpg","highway-mpg"]])
'''zad5'''
zad5 = plik2.groupby("make").count()
print(zad5.loc[:,"fuel-type"])
'''zad6'''
zad6_1 = np.polyfit(plik2["city-mpg"],plik2["length"],1)
zad6_2 = np.polyfit(plik2["city-mpg"],plik2["length"],2)
print(zad6_1)
print(zad6_2)
print(np.polyval(zad6_1,plik2["city-mpg"]))
print(np.polyval(zad6_2,plik2["city-mpg"]))
'''zad7'''
print(sc.stats.pearsonr(plik2["city-mpg"],plik2["length"]))
'''zad8'''
city_mpg = np.linspace(plik2["city-mpg"].min(), plik2["city-mpg"].max())
plt.figure()
plt.plot(plik2["city-mpg"], plik2["length"], 'o')
plt.plot(city_mpg, np.polyval(zad6_1, city_mpg))
plt.plot(city_mpg, np.polyval(zad6_2, city_mpg))
plt.savefig("zad8.png")
plt.show()
'''zad9'''
length = np.linspace(plik2["length"].min(), plik2["length"].max())
zad9 = sc.stats.gaussian_kde(plik2["length"])
fig,ax = plt.subplots(2,1,figsize=(20,10))
ax[0].plot(length,zad9(length),label="length")
ax1 = ax[0].twinx()
ax1.plot(plik2["length"], plik2["city-mpg"], 'r.', label="probki")
ax[0].legend(loc = 'upper left')
ax1.legend(loc = 'upper right')
'''zad10'''
width = np.linspace(plik2["width"].min(), plik2["width"].max())
zad10 = sc.stats.gaussian_kde(plik2["width"])
ax[1].plot(width, zad10(width), label="width")
ax3 = ax[1].twinx()
ax3.plot(plik2["width"], plik2["city-mpg"], 'r.', label="probki")
ax[1].legend(loc = 'upper left')
ax3.legend(loc = 'upper right')
fig.savefig("zad9-10.png")
fig.show()
'''zad11'''
xmin = plik2["width"].min()
xmax = plik2["width"].max()
ymin = plik2["length"].min()
ymax = plik2["length"].max()
X,Y = np.meshgrid(np.linspace(xmin,xmax,100),np.linspace(ymin,ymax,100))
positions = np.vstack([X.ravel(),Y.ravel()])
values = np.vstack([plik2["width"], plik2["length"]])
kernel = sc.stats.gaussian_kde(values)
Z = np.reshape(kernel(positions).T, X.shape)
fig,ax = plt.subplots(figsize=(10,8))
ax.scatter(plik2["width"],plik2["length"])
ax.contour(X, Y, Z, colors='k', linewidths=1)
ax.plot(plik2["width"],plik2["length"], 'k.', markersize=2)
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
plt.savefig("zad11.png")
plt.savefig("zad11.pdf")
plt.show()
