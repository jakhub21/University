#Zadanie 1
#rozk³ad dwumianowy n=4 p=1/3
x =c(0,1,2,3,4)
pr = dbinom(x,4,1/3)
rozklad =data.frame(x,pr)
plot(x,pr)
#P(A)=P(X<2)=P(X<=1)
pbinom(1,4,1/3)
#P(B)=P(X>=3)=1-P(x<3)=1-P(X<=2)
1-pbinom(2,4,1/3)
pbinom(2,4,1/3,F)

#Zadanie 2
#rozk³¹d Poissona, lambda = 12
x=0:99
pr =dpois(x,12)
plot(x,pr)
#podpunkt 1a
#P(X=15)
dpois(15,12)
#podpunkt 1b
#P(7<=X<=13)
ppois(13,12)-ppois(6,12)
sum(dpois(7:13,12))
#podpunkt 2
#P(X<=k)=0,96
qpois(0.96,12)
#k=18

#zadanie 3
#rozklad geometryczny, p=0.02
#podpunkt a
#P(X=3)
dgeom(3,0.02)
#podpunkt b
#P(X<=2)
pgeom(2,0.02)

#zadanaie 4
#rozklad dwumianowy/ rozklad poissona n=100, p=0.01
#podpunkt A
dbinom(2,100,0.01)
dpois(2,1)
#podpunkt b
pbinom(2,100,0.01)
ppois(2,1)

#zadanie 5
#n=4,p=1/7
dbinom(2,4,1/7)

#zadanie 6
#P(X<=2)
pbinom(2,750,0.004)

#zadanie 7
#podpunkt a
dbinom(5,10,0.5)
#podpunkt b
sum(dbinom(3:8,10,0.5))

#zadanie8
#podpunkt a
dgeom(4,1/6)
#podpunkt b
1- pgeom(5,1/6)

#Zadanie 9
1-pbinom(2,400,0.005)

#zadanie 10
#a)
dgeom(1,18/38)
#b)
pgeom(4,18/38)

