Ankieta$Plec = factor(Ankieta$Plec)
Ankieta$M.zamieszk = factor(Ankieta$M.zamieszk)
Ankieta$Sz.srednia = factor(Ankieta$Sz.srednia)
Ankieta$System = factor(Ankieta$System)
Ankieta$L.sys.op = factor(Ankieta$L.sys.op)

Ankieta$Sr.kursy = (Ankieta$Algebra+Ankieta$MSzS1+Ankieta$Narz.inz+Ankieta$Prog1+Ankieta$WdI)/5

Ankieta.kursy = subset(Ankieta, select =7:11)

Ankieta$Waga.dag = (Ankieta$Waga)*100
Ankieta$Waga.dag = NULL

ggplot(Ankieta,aes(x=Plec,y=Wzrost))+geom_boxplot(fill='yellow',col='red')
ggplot(Ankieta,aes(x=Plec,y=Waga))+geom_boxplot(fill='yellow',col='red')

zakres3sigm = function(x)
{
 lewy.kres= (mean(x)-3*sd(x))
 prawy.kres = (mean(x)+3*sd(x))
 cbind(lewy.kres,prawy.kres)
}
zakres3sigm(Ankieta$Waga)

Ankieta.M = filter(Ankieta,Plec=='M')
Ankieta.K = filter(Ankieta,Plec=='K')

zakres3sigm(Ankieta.K$Wzrost)
summary(Ankieta.K$Wzrost)

zakres3sigm(Ankieta.K$Waga)
summary(Ankieta.K$Waga)

zakres3sigm(Ankieta.M$Wzrost)
summary(Ankieta.M$Wzrost)

zakres3sigm(Ankieta.M$Waga)
summary(Ankieta.M$Waga)

which(Ankieta.M$Waga>144)
Ankieta.M$Waga[7]=mean(Ankieta.M$Waga[-7])

which(Ankieta$Waga>144)
Ankieta$Waga[7]=mean(Ankieta$Waga[-7])

zakres3sigm(Ankieta.M$Waga)
summary(Ankieta.M$Waga)

Ankieta$L.g.kody = cut(Ankieta$L.godz,c(0,4,8,24),c('krotko','srednio','dlugo'))
summary(Ankieta$L.g.kody)


stem(Ankieta.M$Waga)
stem(Ankieta.M$Wzrost)

hist(Ankieta.M$Waga)
ggplot(Ankieta.M,aes(x=Waga))geom_histogram(fill='yellow',col='red',binwidth = 15)+ylab('Ilosc studentow')
ggplot(Ankieta.M, aes(x=Waga))+geom_histogram (fill='red',col='black', binwidth=15) +ylab('liczba')
ggplot(Ankieta.M, aes(x=Wzrost))+geom_histogram (fill='red',col='black', binwidth=10) +ylab('liczba')
ggplot(Ankieta, aes(x=Sz.srednia))+geom_bar(fill= 'black',col='red')+ylab('liczba')
ggplot(Ankieta,aes(x=Sr.kursy,y=Sz.srednia))+geom_boxplot(fill='yellow',col='red')
