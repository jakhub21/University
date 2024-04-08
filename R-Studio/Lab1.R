#Zad 1
#a
((2*3^3)/sin(pi/6))+log(2401,7)
#b
abs(-9+5^(-3))+(2^(1/3))^(1/5)
#c
2^(1/3)*log(3^5+5^2-12,2)+(3+(7^4)^(1/3))^(1/5)
#Zad 2
A =matrix(c(1,-10,12,3,2,1,-8,4,5),3,3)
B =matrix(c(1,3,-1,2,1,5),3,2)
#a
det(A)
#b
solve(A)
t(A)
#c
A%*%B
A%*%t(A)
A%*%A
#d
A[1,]*B[,2]
#Zad3(kol)
C=matrix(c(1,2,5,-2,1,2,5,-3,-1,0,2,1,-2,3,5,2),4,4)
D=matrix(c(-7,21,40,2),4,1)
solve(C,D)
#Zad4(kol)
W=(1:100)^2
summary.factor(W%%10)
summary(W%%2==0)
summary(W%%3==0)
summary((W%%2==0)&(W%%3==0))
#Zad5
rad = function(x)
{
  (x*pi)/180
}
x=rad(c(0,30,45,60,90))
Tablice = data.frame(sin=sin(x),cos=cos(x),tg=tan(x),ctg=1/tan(x))
#Zad6(kol)
E=matrix(c(-9,15,-14,-1,13,5,18,6,8,12,10,-4,1,5,8,12),4,4)
F=matrix(c(4,298,294,120),4,1)
solve(E,F)
solve(E)[1,4]
#Zad7(kol)
w= seq(21,903,by = 7)^3
summary(w%%3==0)
summary(w%%11==0)
summary((w%%3==0)&(w%%11==0))
