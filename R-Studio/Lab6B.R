#zad2
n =100
sig =2
m =10
#P(9.8<X/100<10.1)
pnorm(1010,n*m,sig*sqrt(n))-pnorm(980,n*m,sig*sqrt(n))

#zad3
n=100000
p=0.0001
q=1-p
#P(S<7) S<6.5
pnorm(6.5,n*p,sqrt(n*p*q))
