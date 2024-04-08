#Zad1
#N(162,178)
#P(X<155)=0.12
#a)
m= 172.5
sig = (155-m)/qnorm(0.12)
pnorm(178,m,sig)-pnorm(162,m,sig)
#b)
#P(X>180)=0.28
m= 172.5
sig = (180-m)/qnorm(0.72)
pnorm(178,m,sig)-pnorm(162,m,sig)

#Zad2
m = 2236.84
#P(X<1100)=0,13
sig = (1100-m)/qnorm(0.13)
qnorm(0.75,m,sig)

#Zad3
m =100
#P(X>133)=0.02
sig = (133-m)/qnorm(0.98)
pnorm(116,m,sig)-pnorm(84,m,sig)
qnorm(0.97,m,sig)

#Zad4
sig =0.1
#P(1.8<X<2.2)
#P(X>2.5)=0.002
m =2.5-sig*qnorm(0.998)
(pnorm(2.2,m,sig,F)+pnorm(1.8,m,sig))^3
(1-(pnorm(2.2,m,sig)-pnorm(1.8,m,sig)))^3
  