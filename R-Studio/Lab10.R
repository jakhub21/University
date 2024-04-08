#zad1
table(Ankieta$Sz.srednia)
#l.sukcesow = 10
#a) przedzial ufnosci dla wskaznika struktury
prop.test(10,52,conf.level = 0.98)
#0.09025192 0.35643396
#interpretacja: przedzial liczbowy o koncach 0.09025192 i 0.35643396 z ufnoscia 0.98 obejmuje odsetek osob ktore ukonczyly LO(RM) w populacji studentow 1 rokuna WI ZUT w Szczecinie

#b) test dla wskaznika struktury
#hipoteza:    h0:p=0.10    h1:p>0.10
prop.test(10,52,p=0.1,alternative = 'g')
#X-squared = 3.9509
#p-value = 0.02342
#alfa = 0.05
#alfa > p-value zatem odrzucamy h0 i przyjmujemy h1 czyli odsetek studentow ktorzy ukonczyli LO(RM) jest istotnie wiekszy niz 10%

#c) test dla dwoch wskaznikow struktury
table(Ankieta$Sz.srednia,Ankieta$Sr.kursy>4)
#h0:p1=p2 h1:p1>p2
prop.test(c(15,16),c(23,29),alternative = 'g')
#X-squared = 0.20131
#p-value = 0.3268
#alfa = 0.05
#na poziomie istotnosci 0.05 nie mozna odrzucic hipotezy h0 ktora mowi ze odsetek osob po technikum infomatycznym jest taki sam dla studentow o sredniaj za kursy wikszej niz 4 oraz dla studentow o sredniaj mniejszej rownej 4

#zad2
#a)zalozenie 1: normalnosci rozkaldow
#h0:rozklad wzrostu w populacji kobiet jest normalny
#h1~h0
#h0' rozklad wzrostu w populacji mezczyzn jest normalny
#h1'~h0'
by(Ankieta$Wzrost,Ankieta$Plec,shapiro.test)
#K:W = 0.92417, p-value = 0.5572
#M:W = 0.94943, p-value = 0.04114
#alfa = 0.01
#na poziomie 0.01 nie ma podstaw do odrzucenia h0 i h0' ze rozklady wzrostu w populacjach kobiet i mazczyzn sa normalne

#b)zalozenie 2: jednorodnosc wariancji
#h0 (sig.k)^2=(sig.m)^2
#h1~h0
var.test(data = Ankieta,Wzrost~Plec)
#F = 1.815,
#p-value = 0.2843
#alfa 0.01
#nie ma podstaw do odrzucenia wniasku o jendakowych wariancjach wzrostu 

#c)test dla dwoch srednich
#h0:m.K=m.M
#h1:m.K<m.M
t.test(data=Ankieta,Wzrost~Plec,alternative ='l',var.equal=T)
#t = -7.0027
#p-value = 2.971e-09
#alfa = 0.01
#odrzucamy h0 i przyjmujemy h1 zatem wyniki proby potwierdzaja hipoteze ze wzrost kobiet jest istotnie nizszy niz wzrost mezczyzn

#zad 3
#a)zalozenie 1: normalnosci rozkaldow
#h0:rozklad wagi w populacji kobiet jest normalny
#h1~h0
#h0' rozklad wagi w populacji mezczyzn jest normalny
#h1'~h0'
by(Ankieta$Waga,Ankieta$Plec,shapiro.test)
#W = 0.95548, p-value = 0.7762
#W = 0.97943, p-value = 0.569
#alfa = 0.01
#na poziomie 0.01 nie ma podstaw do odrzucenia h0 i h0' ze rozklady wagi w populacjach kobiet i mazczyzn sa normalne

#b)zalozenie 2: jednorodnosc wariancji
#h0 (sig.k)^2=(sig.m)^2
#h1~h0
var.test(data = Ankieta,Waga~Plec)
#F = 0.53543
#p-value = 0.5793
#alfa = 0.01
#odrzucamy h0 i przyjmujemy h1 zatem wyniki proby potwierdzaja hipoteze ze waga kobiet jest istotnie nizszy niz waga mezczyzn

#c)test dla dwoch srednich
#h0:m.K=m.M
#h1:m.K<m.M
t.test(data=Ankieta,Waga~Plec,alternative ='two.sided',var.equal=T)
#t = -4.4576
#p-value = 4.691e-05
#alfa=0.01
#alfa>p-value
#Wnioske: Odrzucamy H0 i przyjmyjemy H1, zatem wyniki, próby potwierdzają hipotezę, że waga kobiet i męzczyzn rózni się w zaleznosci od plci

#zad4
#a)
table(Ankieta$Sz.srednia)
#l.sukcesow = 31
#przedzial ufnosci dla wskaznika struktury
prop.test(31,52,conf.level = 0.99)
#0.4108018 0.7586231
#interpretacja: przedzial liczbowy o koncach 0.4108018 i 0.7586231 z ufnoscia 0.99 obejmuje odsetek osob ktore ukonczyly TI w populacji studentow 1 rokuna WI ZUT w Szczecinie

#b) test dla wskaznika struktury
#hipoteza:    h0:p=0.65    h1:p<0.65
prop.test(31,52,p=0.65,alternative = 'l')
#X-squared = 0.44717
#p-value = 0.0.2518
#alfa = 0.01
#alfa < p-value zatem brak podstaw do odrzucenia h0

#c)test dla dwoch wskaznikow struktury
table(Ankieta$L.g.kody,Ankieta$Wiek>6)
#h0:p1=p2 h1:p1>p2
prop.test(c(6,19),c(15,37),alternative = 'g')
#X-squared = 0.19002
#p-value = 0.6686
#alfa = 0.01
#na poziomie istotnosci 0.05 nie mozna odrzucic hipotezy h0 ktora mowi ze odsetek osob po technikum infomatycznym jest taki sam dla studentow o sredniaj za kursy wikszej niz 4 oraz dla studentow o sredniaj mniejszej rownej 4








