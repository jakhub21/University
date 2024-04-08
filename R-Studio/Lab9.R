#zad1
przedz.odchyl=function(x,uf)
{
  n=length(x)
  
  ocena.dolna=sqrt((n-1)*(var(x))/qchisq(1-((1-uf)/2),n-1))
  ocena.gorna=sqrt((n-1)*(var(x))/qchisq((1-uf)/2,n-1))
  
  cbind(ocena.dolna,ocena.gorna)
  
}
przedz.odchyl(Ankieta.M$Wzrost,0.95)

#zad2
#(a)
ggplot(Ankieta.M, aes(x=Wzrost))+geom_histogram (aes(y=..density..), fill= ' pink ', col= ' red ', binwidth= 10)+stat_function (fun=dnorm, args=list (mean=mean(Ankieta.M$Wzrost), sd=sd(Ankieta.M$Wzrost)), col= ' black ')+ylab(' f(x) ')
#(b) test na normalnosc Shapiro-Wilka
#H0:rozklad wzrostuM jest normalny, H1:~H0
shapiro.test(Ankieta.M$Wzrost)
#W = 0.94943
#p-value = 0.04114
#alfa mniejsze niz p brak podstaw do odrzucenia hipotezy o normalnosci rozkladu wzrostu w populacji studentow 
#(c)
#przedzial ufnosci dla sredniej
t.test(Ankieta.M$Wzrost,conf.level = 0.95)
#przedzial liczbowy w okolicach 179.7242 183.3396 z prawdobodobiejstwem 5 setnych obejmuje zeczywista wartosc srednia wzrostu populacji studentow 
t.test(Ankieta.M$Wzrost,conf.level = 0.98)
#przedzial liczbowy w okolicach 179.3674 183.6964 z prawdobodobiejstwem 2 setnych obejmuje zeczywista wartosc srednia wzrostu populacji studentow 
#ze wzrostek wspoczynnika ufnosc rozszeza sie przedzial ufnosci
#(d)
#przedzial ufnosci dla odchylenia standardowego
przedz.odchyl(Ankieta.M$Wzrost,0.97)
#Przedział liczbowy o końcach 5.02 i 7.93 z prawdopodobieństwem 0.97 obejmuje rzeczywistą wartość odchylenia standardowego wzrostu w populacji studentów I roku WI.
#(e)
#test dla sredniej
#H0:m=181
#H1:m>181
t.test(Ankieta.M$Wzrost,mu=181,alternative = 'greater')
#t = 0.59229, df = 46, p-value = 0.2783
#alfa = 0.01
#na poziomie istotnosci 0.01 nie ma podstaw do odrzucenia hipotezy H0 nie mozna zatem potwierdzic hipotezy ze sredni wzrost studentow jest wyzszy niz 181 cm

#zad3
#(A)
shapiro.test(Ankieta.M$Waga)







#zad4
#a)
#przedzial ufnosci dla wskaznika struktury
table(Ankieta$Sz.srednia)
prop.test(10,52,conf.level = 0.98)
#b)
#H0:p=0.10
#H1:p>0.10
prop.test(10,52,p=0.10,alternative = 'greater')
#X-squared(chisq) = 3.9509, df = 1, p-value = 0.02342
#alfa = 0.05
#alfa wieksze niz p wiec odrzucamy H0 i przyjmujemy H1 zatem od setek studentow ktorzy ukonczyli LO(RM) jest istotnie wiekszy niz 10 %



