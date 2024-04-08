#Zad 1
# m = 86.5
# P(82.5<X<90.5)=0.3472
#P (X>95)*400
m1 = 86.5
#P(X<=82.5)=(1-0.3472)/2
sig1 =(82.5-m1)/qnorm((1-0.3472)/2)
400*pnorm(95,m1,sig1,F)

#Zad 2
#P(X>2)=0.2  ==>  P(X<=2)=0.8
#P(X<1.5)=0.44
#2-m2/sig2 = qnorm(0.8) ==> m2+qnorm(0.8)*sig2 = 2
#1.5-m2/sig2 = qnorm(0.44) ==> m2+qnorm(0.44)*sig2 =1.5
A = matrix(c(1,1,qnorm(0.8),qnorm(0.44)),2,2)
B = matrix(c(2,1.5),2,1)
m2 = solve(A,B)[1]
sig2 = solve(A,B)[2]
pnorm(0.5,m2,sig2)

#Zad 3
m3=4001.50
#P(X=1735.90)=0.2 
sig3=(1735.90-m3)/qnorm(0.20)
qnorm(0.75,m3,sig3)

#Zad 4
#P(X<17)=2/524
#P(X>70)=7/524 ==> P(X<70)=517/524
#17-m4/sig4 = qnorm(2/524) ==> m4+qnorm(2/524)*sig4 = 17
#70-m4/sig4 = qnorm(517/524) ==> m4+qnorm(517/524)*sig4 =70
A1 = matrix(c(1,1,qnorm(2/524),qnorm(517/524)),2,2)
B1 = matrix(c(17,70),2,1)
m4 = solve(A1,B1)[1]
sig4 = solve(A1,B1)[2]
#P(45<X<55)
pnorm(55,m4,sig4)-pnorm(45,m4,sig4)

#Zad5 
m5=165
#P(155<X<175)=0.93
#500*(X>170)=?
#P(X<=155)=(1-0.93)/2
sig5=(155-m5)/qnorm((1-0.93)/2)
500*pnorm(170,m5,sig5,F)

#Zad3B
m3b=44/524
#P(32<X<56)=503/524
#P(X<17)
sig3b = 
#50-m/sig=qnorm(0.4)
sig = (50-m)/qnorm(0.6)