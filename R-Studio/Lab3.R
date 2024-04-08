#Zad 1
#a) rozklad N(0,1)
qnorm(0.97)
#b) rozklad chi^2
qchisq(0.975,9)
#c)rozklad studenta
qt(0.95,9)
#d) rozklad fishera
qf(0.995,10,23)

#Zad 2 N(1.5,2)
#a)P(X<2.5) = F(2.5)
pnorm(2.5,1.5,2)
#b)P(X>-0.5) = 1-F(-0.5)
1 - pnorm(-0.5,1.5,2)
#c)P(0.5<X<2) = F(2)-F(0.5)
pnorm(2,1.5,2) -pnorm(0.5,1.5,2)
#d)P(|X-2|<3) = P(-1<X<5)
pnorm(5,1.5,2) -pnorm(-1,1.5,2)
#e)P(|2X-1|<1) = P(0<X<1)
pnorm(1,1.5,2) -pnorm(0,1.5,2)
#f)P(|X|>0.5) = P(X<-0.5)+P(X>0.5)
pnorm(-0.5,1.5,2)+(1 - pnorm(0.5,1.5,2))
#g)P(|3X-1|>2) = P(3X-1<-2)+P(3X-1>2) = P(X<-1/3)+P(X>1)
pnorm(-1/3,1.5,2)+(1 - pnorm(1,1.5,2))
 
#Zad 3 N(1000h, 50h) 4000 zarowek 900h
pnorm(900,1000,50)*4000

#Zad4 (6.8,0.3)
#a) P(X>7.1) 
pnorm(7.1,6.8,0.3,F)*30
#b) P(X < a) = 0.15
qnorm(0.15,6.8,0.3)

#Zad5 (15,13)
#a)22:05<X<22:10
pnorm(10,15,13) -pnorm(5,15,13)
#b)22:20
pnorm(20,15,13,F)

# Zad 6
# N(20,5)
# a)
qnorm(0.8849,20,5)
# b)
qnorm(0.6554,20,5,F)
#c)
20-qnorm((1-0.6826)/2,20,5)
#d)
20-qnorm(0.00511/2,20,5)
#Zad 4b (4,3)
#a)
pnorm(2,4,3)
#b
1-pnorm(5,4,3)

#Zad 5b
#a)
(pnorm(174,178,9)-pnorm(170,178,9))*1500
#b)
qnorm(0.95,178,9)

#Zad 6b (-5,12)
#a
qnorm(0.7606,-5,12)
#b
qnorm(0.4668,-5,12,F)
#c
-5-qnorm((1-0.8434)/2,-5,12)
#d
-5-qnorm(0.4532/2,-5,12)
