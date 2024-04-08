#zad 1
x=c(225,236,312,238,241,196,205,259,218)#przed kuracja
y=c(216,195,245,235,221,170,180,265,179)#po kuracji

#test dla prob zaleznych
#zalozenie:normalnosc rozkladu roznicy zmiennych 
#H0:rozklad roznicy zmirnnych jest normalny H1~H0
shapiro.test(x-y)
#stat.testowe W = 0.96898
#p-value = 0.8858
#alfa = 0.01
#brak podstaw do odrzucenia H0

#test t Studenta dla prob zaleznych
#H0:m1 - m2 = 0 nie wplywa
#H1:m1 - m2 > 0 wplywa
t.test(x,y,paired = T,alternative = 'g')
#stat.testowe t = 3.3633
#p-value = 0.004942
#alfa = 0.01
#alfa wieksze niz p-value wiec odrzucamy H0 i przyjmujemy hipoteze H1 zatem leczenie statynami skutecznie wplywa na obnizenie skutecznie cholesteroru

#zad2 
xi=c(150,300,450,600,750,900,1200,1500,1800)#zmienna niezalezna
yi=c(27.2,26.0,24.2,22.5,21.7,20.5,19.0,17.4,16.0)#zmienna zalezna 
#A
#wykres punktow wmpirycznych
plot(xi,yi)

#B
#wspolczynnik korelacji liniowej
cor(xi,yi)
# r = -0.98
#r<0.50 korelacja slaba
#0.7>r>0.5 korelacja umiarkowana
#r>0.7 korelacja silna 
#-r korelacja ujemna
#interpretacja wspolczynnika korelacji: pomiedzy wysokoscia nad poziomem morza a temp powietrza isnieje bardzo silna zaleznosc korelacyjna ujemna czyli im wyzej nad poziomem morza tym nizsza temp

#C
#przedzial ufnosci dla wspol. korelacji w populacji
cor.test(xi,yi,conf.level = 0.95)
#przedzial o koncach -0.997 i -0.926 z prawdopodobienstwem 0.95 obejmuje wspolczynnik korelacji liniowej miedzy wysokoscia nad poziomem morza a temp. powietrza 

#D
#oszacownia funkcji regresji liniowej 
lm(yi~xi)
#postac funkcji regresji: y = 27.322 - 0.007x
#0.007x wspolczynnik regresji
#interpretacja wspolczynnika regresji: wspolczynnik regresji rowny 0.007 oznacza ze ze wzrostem wysokosci nad poziomem morza o 100m srednio biorac spada temperatura powierza o okolo 0.7 stopnia celciusza

#E
#wykres oszacowaje funkcji regresji
abline(lm(yi~xi))

#F
#test istotnosci wspolczynnika regresji w populacji i  oznaczonego beta 1
#H0: beta1=0
#H1:~H0
summary(lm(yi~xi))
#wartosc testowa: t =-14.89 (przedostatnia kolumana drugi wiersz)
#p-value = 1.48e-06(ostatnia kolumna 2 wiersz)
#alfa = 0.02
#odrzucamy hipoteza H0 przyjmujemy H1 zatem wspolczynnik regresji miedzy wysokoscia a temp powietrza jest istotny

#zad3
#test niezaleznosci chi^2
#X - wielkosc cebulki
#Y - pojawienie sie pedu kwiatostanowego
#H0:X,Y sa niezalezne 
#H1:~H0
chisq.test(matrix(c(152,52,8,188),2,2))

#statystyka testowa:chi^2 = 203.67
#p-value = 2.2e-16
#alfa 0.01
#odrzucamy hipoteza H0 przyjmujemy H1 zatem na poziomie istotnosci 0.01 mozna potwierdzic hipoteze ze rośliny cebuli wyhodowane z większych cebulek dymki wyrastają częściej w pędy kwiatostanowe.

#zad 4

x=c(87.5,56,67,82.5,92,59,90.5,80.5,65,92)#przed dieta
y=c(86,54,66,83,87,62,87,90,61,70)#po diecie
#test dla prob zaleznych
#zalozenie: normalnosc rozkladu roznicy zmiennych
#h0: rozklad roznicy zmiennych jest normalny    h1: nie h0

shapiro.test(x-y)
#statystyka testow W = 0.83934
#p-value = 0.04333
#alfa=0.05
#odrzucamy h0

#h0:m1-m2=0    h1:m1>m2 -> m1-m2>0
wilcox.test (x, y, paired=TRUE, alternative = 'g')
#V = 40, p-value = 0.1162
#alfa <p-value
#brak podstaw do odrzucanie h0 ze zastosowana dieta nie ma wplywu na wage 

#zad5 
xi=c(0.8,1.2,1.6,1.8,2.2,1.6,2.4,2.0)#zmienna niezalezna
yi=c(6,10,12,15,18,15,20,16)#zmienna zalezna 

#A
cor(xi,yi)
#r = 0.98
#interpretacja wspolczynnika korelacji: pomiedzy wilkoscia produkcji a liczba brakow isnieje bardzo silna zaleznosc korelacyjna czyli im wieksza produkcja tym wieksza liczba brakow
# b)
cor.test(produkcja,braki, conf.level = 0.98)
# przedział ufności o końcach 0.8581196 i 0.9976229 z prawdop. 0.98 obejmuje współczynnik korealacji liniowej między wielkością produkcji i liczbą braków
# c)
lm(braki~produkcja)
# postać funkcji regresji:  y: -0.3438 + 8.4375x
# INTERPRETACJA: współcznnik regresji równy 8.44 oznacza że ze wzrostem wysokości o 1000 sztuk, liczba braków wzrasta średnio o lekko ponad 8 sztuk
# d)
summary(lm(braki~produkcja))
# H0: β1 = 0
# H1: ~H0
# stat. testowa t = 12.425
# p-value = 1.66e-05
# alfa = 0.01
# WNIOSEK: odrzucamy H0, przyjmujemy H1, zatem współczynnik regresji między wielkością produkcji a liczbą braków jest istotny

#zad6
#test niezaleznosci chi^2
#X - wyksztalcenie
#Y - zadowolenie
#H0:X,Y sa niezalezne 
#H1:~H0
chisq.test(matrix(c(45,35,30,25,25,40),3,2))
#statystyka testowa:chi^2 = 6.8783
#p-value = 0.03209
#alfa 0.05
#odrzucamy hipoteza H0 przyjmujemy H1 zatem na poziomie istotnosci 0.05 mozna potwierdzic hipoteze ze rośliny cebuli wyhodowane z większych cebulek dymki wyrastają częściej w pędy kwiatostanowe.








