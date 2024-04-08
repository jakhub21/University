#Zad 1
#a)
#P(3<X<6)=?
#P(X>5)=0.5, sigma=1
sig = 1
m =5
pnorm(6,m,sig)-pnorm(3,m,sig)

#b)
#P(X<6)=0.6
sig =2
m
#6-m/sig = qnorm(0.6)
#6-m = sig*qnorm(0.6)
m = 6-sig*qnorm(0.6)
pnorm(6,m,sig)-pnorm(3,m,sig)

#Zad2
m = 5.2
#P(X<3)=0.121
#3-m/sig=qnorm(0.121)
sig = (3-m)/qnorm(0.121)
qnorm(0.8,m,sig)

#Zad3
m =-5
#P(X<3) = 0.95
#3-m/sig=qnorm(0.95)
sig = (-3-m)/qnorm(0.95)
#P(X>0)
1-pnorm(0,m,sig)

#Zad4
#a)
#P(X>50)=0.4
m=46
#50-m/sig=qnorm(0.4)
sig = (50-m)/qnorm(0.6)
1 - pnorm(70,m,sig)
#b)
qnorm(0.9,m,sig)

#Zad3B
#a)
m=100
#P(X>133)=0.02
sig = (133-m)/qnorm(0.98)
pnorm(116,m,sig)-pnorm(84,m,sig)
#b)
qnorm(0.97,m,sig)

#Zad4B
sig = 0.1
#P(1.8<X<2.2)
#P(X<2.5)=0.98
m = 2.5-sig*qnorm(0.998)
(1-(pnorm(2.2,m,sig)-pnorm(1.8,m,sig)))^3
