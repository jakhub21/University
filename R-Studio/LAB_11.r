# ZAD 1
# wprowadzanie danych: 
plony = c(2.6,2.4,2.0,1.8,2.2,1.5,1.5,1.4,1.2,2.5,2.2,1.8,1.7,1.8,1.5,1.2,1.5,0.8,1.0) # zmienna mierzalna
kombin = c(rep('1',5),rep('2',4),rep('3',5),rep('4',5))
# a)
# normalnosc rozkładów (test shapiro wilka):
# H01: rozklad plonow przy nawozeniu 1 jest normalny H11: ~H01
# H02: rozklad plonow przy nawozeniu 2 jest normalny H12: ~H02
# H03: rozklad plonow przy nawozeniu 3 jest normalny H13: ~H03
# H04: rozklad plonow przy nawozeniu 4 jest normalny H14: ~H04
by(plony,kombin,shapiro.test)
#1: W = 0.98676, p-value = 0.9672
#2: W = 0.82743, p-value = 0.1612
#3: W = 0.85805, p-value = 0.2213
#4: W = 0.90345, p-value = 0.4292
# alfa = 0.05
# Nie ma podstaw do odrzucenia hipotez zerowych, że rozkłady plonów przy wszystkich kombinacjach są normalne
# b)
#jednorodność wariancji
#H0: sig1^2=sig2^2=..=sigk^2 (wariancje są jednakowe)
#H1: ~H0; wariancje nie są jednakowe
bartlett.test (plony ~ kombin)
# Bartlett's K-squared = 2.0916, df = 3, p-value = 0.5536
# Nie ma podstaw do odrzucenia hipotezy H0 o jednakowych wariancjach plonów przy wszystkich kombinacjach
# c)
# test ANOVA
# H0: m1=m2=m3=m4 (brak wpływu czynnika)
# H1: wpływ istotny czynnika
anova (aov(plony ~ kombin))
# statystyka testowa (przedostatnia kolumna): 12.713(statystyka Fischera), 0.0002131(p-value = Pr(>F))

# Wniosek: alfa > p-value, więć odrzucamy H0 i przyjmujemy H1, zatem wpływ nawożenia rzepaku jarego jest ISTOTNY

# d) analiza post hoc (test Tukeya) | nieobowiązkowe!
TukeyHSD(aov(plony ~ kombin))
plot(TukeyHSD(aov(plony ~ kombin)))

# ZAD 2
# a) założenie o normalności rozkładu
# H0: rozkład średnich ocen za kursy jest normalny
# H1: ~H0
shapiro.test(Ankieta$Sr.kursy)
# W = 0.94705, p-value = 0.02188, alfa = 0.05
# odrzucamy H0 -> rozkład nie jest normalny

# test nieparametryczny (Wilcoxona)
# H0: med = 3.8
# H1: med > 3.8
wilcox.test(Ankieta$Sr.kursy, mu = 3.8, alternative = 'g')
# V = 927, p-value = 0.002597
# Wniosek: alfa > p-value, zatem odrzucamy H0 i przyjmujemy H1, czyli mediana średnich ocen za kursy jest wyższa niż 3.8

# ZAD 3
utarg = c(7.6, 12.0, 7.3, 11.3, 7.0, 10.8, 6.5, 8.1, 3.2, 8.7, 8.8, 11.7, 12.7, 18.5, 3.3, 6.7, 8.6, 6.9, 3.8, 3.7)
sklepy = c(rep('A',13),rep('B',7))

# a) normalność rozkładów
# H01: rozkład utargów w mieście A jest normalny; H11: ~H01
# H02: rozkład utargów w mieście B jest normalny; H12: ~H02
by(utarg,sklepy,shapiro.test)
# A : W = 0.94565, p-value = 0.5341
# B : W = 0.76886, p-value = 0.01989
# alfa = 0.05
# Wniosek: odrzucamy hipoteze o normalności rozkładu w mieście B

# test nieparametryczny Wilcoxona
# H0: medA = medB
# H1: medA > medB
wilcox.test (utarg ~ sklepy, alternative = 'g')
# W = 65, p-value = 0.0674
# Wniosek: brak podstaw do odrzucenia H0, która mówi że rozkłady utargów w miastach A i B są zbliżone

# ZAD 4
# alfa=0.05
# zalozenie 1: normalnosc  rozkladow
# H01:rozklad sredniej ocen dla inna jest normalny
# H11:nieprawda ze H01
# H02:rozklad sredniej ocen dla lo(pm) jest normalny
# H12:nieprawda ze H02
# H03:rozklad sredniej ocen dla lo(rm) jest normalny
# H13:nieprawda ze H03
# H04:rozklad sredniej ocen dla TI jest normalny
# H14:nieprawda ze H04 

by(Ankieta$Sr.kursy,Ankieta$Sz.srednia,shapiro.test)
# inna - W = 0.73812, p-value = 0.02302       a>p-value
# lo(pm) - W = 0.93802, p-value = 0.6433     a<p-value
# lo(rm) - W = 0.92401, p-value = 0.3916     a<p-value
# ti - W = 0.96214, p-value = 0.3319         a<p-vale

#odrzucamy wniosek o normalnosci rozkladu w inna
#nieparametryczny test Kuskala – Wallisa (bo 3 lub wiecej zmiennych)
#h0: meInna=meLO(pm)=meLO(rm)=meTI         h1: nie h0
kruskal.test(Ankieta$Sr.kursy~Ankieta$Sz.srednia)
#chi-squared = 9.7585, p-value = 0.02073
#alfa > p-value zatem odrzucamy h0 i przyjmujemy h1 ze szkola srednia ma wplyw na srednia ocen

# ZAD 6
# normalność rozkładu
# H0: rozkład liczby godzin spę-dzanych w ciągu doby przy komputerze jest normalny
# H1: ~H0
shapiro.test(Ankieta$L.godz)
# W = 0.94019, p-value = 0.0114, alfa = 0.05
# Wniosek: alfa > p-value -> odrzucamy H0, przyjmujemy H1

# test nieparametryczny (Wilcoxona)
# H0: med = 9
# H1: med < 9
wilcox.test(Ankieta$L.godz, mu = 9, alternative = 'l')
# V = 408.5, p-value = 0.01271
# Wniosek: alfa > p-value -> mediana liczby godzin spędzanych w ciągu doby przy komputerze w populacji wszystkich studentów I roku na WI jest mniejsza od 9 godzin

# ZAD 5
x = c(Ankieta$Sr.kursy,Ankieta$M.zamieszk)
table(Ankieta$M.zamieszk)
# a)
# normalnosc rozkładów
# H01: rozkład średniej ocen za kursy z 1. semestru dla osób mieszkających w akademiku jest normalny; H11: ~H01
# H02: rozkład średniej ocen za kursy z 1. semestru dla osób mieszkających z rodziną jest normalny; H12: ~H02
# H03: rozkład średniej ocen za kursy z 1. semestru dla osób mieszkających na stancji lub innej jest normalny; H12: ~H02
by(Ankieta$Sr.kursy,Ankieta$M.zamieszk,shapiro.test)
# 1: W = 0.94158, p-value = 0.4777 alfa < p-value
# 2: W = 0.93159, p-value = 0.03886 alfa > p-value
# 3: W = 0.95347, p-value = 0.7682 alfa < p-value
# Wniosek: odrzucamy hipotezę o normalności rozkładów 

# test nieparametryczny (test Kuskala – Wallisa)
# H0: wariancje są niejednorodne
# H1: wariacje sa jednorodne
kruskal.test (Ankieta$Sr.kursy ~ Ankieta$M.zamieszk)
# Kruskal-Wallis chi-squared = 0.31139, df = 2, p-value = 0.8558
# alfa < p-value -> brak podstaw do odrzucenia H0, o tym że miejsce zamieszkania ma wpływ na srednia ocen z kursów w populacji wszystkich studentów I roku na WI
