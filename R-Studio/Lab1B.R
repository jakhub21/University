(2*3^3)/(sin(pi/6))+log(2401,7)
abs(-9+5^(-3))+(2^(1/3))^(1/5)
2^(1/3)*log(3^5+5^2-12,2)+(3+(7^4)^(1/3))^(1/5)

A = matrix(c(1,-10,12,3,2,1,-8,4,5),3,3)
B =matrix(c(1,3,-1,2,1,5),3,2)

#wyznacznik macierza
det(A)
#macierz odwrotna 
solve(A)
#macierz transponowana
t(A)
#AB
A%*%B
#AA^T
A%*%t(A)
#pierwszy wiersz A z druga kolumna B
A[1,]*B[,2]

#uklad rownan
C=matrix(c(1,2,5,-2,1,2,5,-3,-1,0,2,1,-2,3,5,2),4,4)
D=matrix(c(-7,21,40,2),4,1)
solve(C,D)

#wektor
W=(1:100)^2
summary.factor(W%%10)
summary(W%%2==0)
summary(W%%3==0)
summary((W%%2==0)&(W%%3==0))

#radiany
rad = function(x)
{
  (x*pi)/180
}
x=rad(c(0,30,45,60,90))
Tablice = data.frame(sin=sin(x),cos=cos(x),tg=tan(x),ctg=1/tan(x))

#uklad rownan
E=matrix(c(-9,15,-14,-1,13,5,18,6,8,12,10,-4,1,5,8,12),4,4)
F=matrix(c(4,298,294,120),4,1)
solve(E,F)
#element w pierwszym wierszu i w 4 kolumnie odwrotnej macierzy ukladu
solve(E)[1,4]

#wektor 
W=seq(21,903,by = 7)^3
summary(W%%3==0)
summary(W%%11==0)
summary((W%%3==0)&(W%%11==0))

#p = 1/3 n =4
x =c(0,1,2,3,4)
pr = dbinom(x,4,1/3)
rozklad =data.frame(x,pr)
plot(x,pr)
#P(A)=P(X<2)=P(X<=1)
pbinom(1,4,1/3)
#P(B)=P(X>=3)=1-P(x<3)=1-P(X<=2)
1-pbinom(2,4,1/3)
pbinom(2,4,1/3,F)
