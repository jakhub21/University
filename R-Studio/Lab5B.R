#zad1
m=2
#P(0.5<X<3.5)=0.4
sig = (0.5-m)/qnorm((1-0.4)/2)
#P(X<3/4)
pnorm(3/4,m,sig)

#Zad 2
#3/10 = 5281.21
#0.75 = 9090.90

#zad3
m =44
#P(32<X<56)=503/524
sig = (32-m)/qnorm((1-(503/524))/2)
#P(X<17)
pnorm(17,m,sig)

#zad4
#P(X<=172)=0.9
#P(X>164)=0.57     P(X<164)=0.43
A = matrix(c(1,1,qnorm(0.9),qnorm(0.43)),2,2)
B = matrix(c(172,164),2,1)
m= solve(A,B)[1]
sig= solve(A,B)[2]
pnorm(160,m,sig,F)*700
