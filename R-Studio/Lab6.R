#Zad 1
#rozklad dwumianowy
n = 1200
p = 0.08
q = 1 - p
#S = X+...+X1200
#P(0.07<S/1200<=0.11)=P(84<S<=132)=P(85<=S<=132)=P(84,5<=S<=132,5)
pnorm(132.5,n*p,sqrt(n*p*q))-pnorm(84.5,n*p,sqrt(n*p*q))
#rozklad rzeczywisty
sum(dbinom(85:132,n,p))

#Zad 2
#rozklad normalny
m = 1.99
sig = 0.05
n2 = 250
#P(X1+X250<=498)
pnorm(498,n2*m,sig*sqrt(n2))

#Zad 3
#rozklad dwumianowy
n3 = 5000
p3 =0.01
q3 = 1-p3
#S = X1+...+X5000
#P(S/5000<1.5)=P(S<74)
pnorm(74.5,n3*p3,sqrt(n3*p3*q3))

#Zad 4
m =7
sig = 0.5
n = 130
#P(X+X130>900)
1 - pnorm(900,n*m,sig*sqrt(n))

#Zad 5
#a)
n =1000
p = 0.525
q = 1-p
#S = X1+..+X1000
#P(S<=479)
1-pnorm(479.5,n*p,sqrt(n*p*q))
#b)
#P(448,5<S<520,5)
pnorm(519,5,n*p,sqrt(n*p*q))-pnorm(448,5,n*p,sqrt(n*p*q))

#Zad1b 
n = 130000
p = 0.85
q = 1 -p
#P(S>=110000-1)
1-pnorm(109999,n*p,sqrt(n*p*q))

#Zad2b
m = 10
sig =2
n =100
