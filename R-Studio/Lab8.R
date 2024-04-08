#Zad 1 Kolokwium
p.opisowe = function(x)
{
  srednia=mean(x)
  mediana=median(x)
  kwartyl1=quantile(x,0.25)
  kwartyl2 =quantile(x,0.75)
  min=min(x)
  max=max(x)
  roztep_empiryczny=max(x)-min(x)
  rozstep_kwantylowy=IQR(x)
  odchylenie_standardowe=sd(x)
  wspolczynnik_zmiennosci=sd(x)/mean(x)
  skosnosc=skewness(x)
  wspolczynnik_asymetrii=skewness(x)
  kurtoza=kurtosis(x)
  rbind(srednia,mediana,kwartyl1,kwartyl2,min,max,roztep_empiryczny,rozstep_kwantylowy,odchylenie_standardowe,wspolczynnik_zmiennosci,skosnosc,wspolczynnik_asymetrii,kurtoza)
}
p.opisowe(Ankieta.M$Waga)
#wspolczynnik zmiennosci wyrazamy w % do 10% uznawany za mala zmiennosc, od 10 do 50% uznawana za srednia zmiennosc jezeli wieksze od 50% to duza zmiennosc
#Asymetria lewostronna y>0 / Asymetria prawostronna y<0 / Asymetria skrajna |y| -> 2 
#Kurtoza: k=3 rozklad normalny, k >3 wyzsze skupienie niz rozklad normalny, k<3 nizsze skupienie niz rozklad normalny


#Zad 2
p.opisowe(Ankieta.M$Wzrost)
#a) 
#Kwartyl dolny – wzrost 25% mężczyzn w badanej grupie nie przekroczyła 175,5 m
#Odchylenie standardowe – wzrost mężczyzn odchylała się od średniej wagi przeciętnie o około 6.1568 cm
#Współczynnik zmienności – udział odchylenia standardowego wagi w wartości średniej wynosi 0.0339, co świadczy o tym, że mężczyźni są słabo slabo zróżnicowani pod względem wagi. 
#Skośność – rozkład wagi mężczyzn charakteryzuje się silną umiarkowaną asymetrią lewostronną prawostronną.
#b)
p.opisowe(Ankieta$Sr.kursy)
#Mediana – srednia ocen 50% mężczyzn w badanej grupie nie przekroczyła 4
#Kwartyl górny – srednia ocen 75% mężczyzn w badanej grupie nie przekroczyła 4.3
#c)
p.opisowe(Ankieta$L.godz)
#Średnia - liczby godzin mężczyzn w badanej grupie skupiała się wokół wartości 8.0192308
#Kurtoza – rozkład liczby godzin mężczyzn charakteryzuje się niższym skupieniem wokół średniej wagi niż rozkład normalny.

#Zad3  
x = c(4,6,8,10,12,14)
w = c(9,17,13,6,3,2)
paramentry.wazone = function(x,w)
{
      srednia_wazona = weighted.mean(x,w)
      odchylenie_wazone=sqrt(sum((x-srednia_wazona)^2*w)/(sum(w)-1))
      rbind(srednia_wazona,odchylenie_wazone)
}
paramentry.wazone(x,w)


#zad4








