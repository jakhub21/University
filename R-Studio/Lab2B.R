#p = 2/5 n =6 
x = c(0,1,2,3,4,5)
dbinom(0,6,2/5)
dbinom(1,6,2/5)
dbinom(2,6,2/5)
dbinom(3,6,2/5)
dbinom(4,6,2/5)
dbinom(5,6,2/5)
dbinom(6,6,2/5)

#p =0,003 n=360
lambda = 360*0.003
x =0:359
#P(X=4)
dpois(4,lambda)
#P(X>=3) = 1 - P(X<3)
1 - dpois(3,lambda)#?


#p = 0.001 
#P(X=8)
#piszemy 7 bo bedzie 7 dobrze i 8 zle
dgeom(7,0.001)

#a = 2 n=5 p=1/7
dbinom(2,5,1/7)


#p = 0,5 
dbinom(3,5,0.5)
dbinom(2,3,0.5)

#P|(X>4)=1-P(X<4)
# n = 580 p = 0.002 
lambda2=580*0.002
dpois(4,lambda2)#?

#n = 900 p=0,00007
1-dpois(4,0.007)#?


#rzut kostka
#P(x=5)
1-pbinom(3,6,1/5)

