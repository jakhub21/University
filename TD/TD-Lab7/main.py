


from Hamming import koderHamminga, dekoderHamminga
from modulacja_demodulacja import kluczowanie_fazy, demodulacjaPSK, ASCIIToBinary, ct_to_bitstream, kluczowanie_czestotliwosci, kluczowanie_amplitudy, demodulacjaASK, demodulacjaFSK
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def normalizacja_sygnalu(sygnal):
    sygnal = np.array(sygnal)
    sygnal = sygnal / np.max(np.abs(sygnal))
    return sygnal


def szum_bialy(sygnal, alpha):
    szum = np.random.normal(0, 1, N)*alpha
    szum = normalizacja_sygnalu(szum)
    sygnal = sygnal + szum
    return sygnal


def tlumienie(sig, beta, t):
    damping_sig = np.exp(-beta*t)
    return damping_sig * sig


W = 2
tekst = ASCIIToBinary("abcd")
# tekst = ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0']
n = 7 #ilość bitów w kodzie hamminga

modulacje = ['ASK', 'FSK', 'PSK']


alfa = [0.5, 1, 1.9]

# if len(tekst) % 4 != 0:
#     for i in range(4 - len(tekst) % 4):
#         tekst.append('0')
# df = pd.DataFrame(columns=['Modulacja', 'Alfa', 'BER'])
# for m in modulacje:
#     for a in alfa:
#         zakodowane = []
#         zdekodowane = []
#         for i in range(0, len(tekst), 4):
#             ham = koderHamminga(tekst[i:i + 4], n)
#             zakodowane.extend(ham)
#
#         for j in range(len(zakodowane)):
#             zakodowane[j] = str(zakodowane[j])
#
#         dlugosc = len(zakodowane)
#         fs = 2 ** 10  # częstotliwość próbkowania
#         Tb = 1  # czas trwania bitu
#         Tc = Tb * len(zakodowane)  # czas trwania całego ciągu
#         fn = W * Tb**-1 #częstotliwość nośnej
#         fn1 = (W + 1)/Tb #częstotliwość nośnej
#         fn2 = (W + 2)/Tb #częstotliwość nośnej
#         A1 = 2 #amplituda
#         A2 = 7 #amplituda
#         N = round(Tc * fs) #ilość próbek
#         t = np.linspace(0, Tc, N) #wektor czasu
#
#         if m == 'ASK':
#             ASK = kluczowanie_amplitudy(t, zakodowane, A1, A2, fn, N)
#             ASK = szum_bialy(ASK, a)
#             # plt.plot(t, ASK)
#             # plt.title("ASK" + str(a))
#             # plt.show()
#             xt, pt, ct = demodulacjaASK(t, ASK, N, fn, zakodowane)
#             # plt.plot(t, pt)
#             # plt.show()
#             # plt.plot(t, ct)
#             # plt.show()
#         elif m == 'FSK':
#             FSK = kluczowanie_czestotliwosci(t, zakodowane, N, fn1, fn2)
#             FSK = szum_bialy(FSK, a)
#             # plt.plot(t, FSK)
#             # plt.title("FSK" + str(a))
#             # plt.show()
#             xt1, xt2, pt1, pt2, ct = demodulacjaFSK(t, FSK, N, fn1, fn2, fs, zakodowane)
#         elif m == 'PSK':
#             PSK = kluczowanie_fazy(t, zakodowane, N, fn)
#             PSK = szum_bialy(PSK, a)
#             # plt.plot(t, PSK)
#             # plt.title("PSK" + str(a))
#             # plt.show()
#             xt, pt, ct = demodulacjaPSK(t, PSK, N, fn, zakodowane)
#         bitstream = ct_to_bitstream(ct, N, len(zakodowane))
#
#         for i in range(len(bitstream)):
#             bitstream[i] = int(bitstream[i])
#
#         for i in range(0, len(bitstream), 7):
#             ham = dekoderHamminga(bitstream[i:i + 7])
#             zdekodowane.extend(ham)
#
#         for j in range(len(zdekodowane)):
#             zdekodowane[j] = str(zdekodowane[j])
#
#         print("Początkowa wartość:" + m + " " + str(a), tekst, sep="\n")
#         print("Wartość po zdekodowaniu:", zdekodowane, sep="\n")
#         BER = 0
#         for i in range(len(tekst)):
#             if tekst[i] != zdekodowane[i]:
#                 BER += 1
#         BER = BER/len(tekst)
#         print("BER:", BER)
#         print("\n\n")
#         df = pd.concat([df, pd.DataFrame([[m, a, BER]], columns=['Modulacja', 'Alfa', 'BER'])], ignore_index=True)
# print(df)



# #Tłumienie
beta = [0.5, 5, 15]

# df2 = pd.DataFrame(columns=['Modulacja', 'Beta', 'BER'])
# for m in modulacje:
#     for b in beta:
#         zakodowane = []
#         zdekodowane = []
#         for i in range(0, len(tekst), 4):
#             ham = koderHamminga(tekst[i:i + 4], n)
#             zakodowane.extend(ham)
#
#         for j in range(len(zakodowane)):
#             zakodowane[j] = str(zakodowane[j])
#
#         dlugosc = len(zakodowane)
#         fs = 2 ** 10  # częstotliwość próbkowania
#         Tb = 1  # czas trwania bitu
#         Tc = Tb * len(zakodowane)  # czas trwania całego ciągu
#         fn = W * Tb**-1 #częstotliwość nośnej
#         fn1 = (W + 1)/Tb #częstotliwość nośnej
#         fn2 = (W + 2)/Tb #częstotliwość nośnej
#         A1 = 2 #amplituda
#         A2 = 7 #amplituda
#         N = round(Tc * fs) #ilość próbek
#         t = np.linspace(0, Tc, N) #wektor czasu
#
#         if m == 'ASK':
#             ASK = kluczowanie_amplitudy(t, zakodowane, A1, A2, fn, N)
#             ASK = tlumienie(ASK, b, t)
#             # plt.plot(t, ASK)
#             # plt.title("ASK" + str(b))
#             # plt.show()
#             xt, pt, ct = demodulacjaASK(t, ASK, N, fn, zakodowane)
#         elif m == 'FSK':
#             FSK = kluczowanie_czestotliwosci(t, zakodowane, N, fn1, fn2)
#             FSK = tlumienie(FSK, b, t)
#             # plt.plot(t, FSK)
#             # plt.title("FSK" + str(b))
#             # plt.show()
#             xt1, xt2, pt1, pt2, ct = demodulacjaFSK(t, FSK, N, fn1, fn2, fs, zakodowane)
#         elif m == 'PSK':
#             PSK = kluczowanie_fazy(t, zakodowane, N, fn)
#             PSK = tlumienie(PSK, b, t)
#             # plt.plot(t, PSK)
#             # plt.title("PSK" + str(b))
#             # plt.show()
#             xt, pt, ct = demodulacjaPSK(t, PSK, N, fn, zakodowane)
#         bitstream = ct_to_bitstream(ct, N, len(zakodowane))
#
#         for i in range(len(bitstream)):
#             bitstream[i] = int(bitstream[i])
#
#         for i in range(0, len(bitstream), 7):
#             ham = dekoderHamminga(bitstream[i:i + 7])
#             zdekodowane.extend(ham)
#
#         for j in range(len(zdekodowane)):
#             zdekodowane[j] = str(zdekodowane[j])
#
#         print("Początkowa wartość:" + m + " " + str(b), tekst, sep="\n")
#         print("Wartość po zdekodowaniu:", zdekodowane, sep="\n")
#         BER = 0
#         for i in range(len(tekst)):
#             if tekst[i] != zdekodowane[i]:
#                 BER += 1
#         BER = BER/len(tekst)
#         print("BER:", BER)
#         print("\n\n")
#         df2 = pd.concat([df2, pd.DataFrame([[m, b, BER]], columns=['Modulacja', 'Beta', 'BER'])], ignore_index=True)
# print(df2)

# df3 = pd.DataFrame(columns=['Modulacja', 'Alfa', 'Beta', 'BER'])
# for m in modulacje:
#     for a in alfa:
#         for b in beta:
#             zakodowane = []
#             zdekodowane = []
#             for i in range(0, len(tekst), 4):
#                 ham = koderHamminga(tekst[i:i + 4], n)
#                 zakodowane.extend(ham)
#
#             for j in range(len(zakodowane)):
#                 zakodowane[j] = str(zakodowane[j])
#
#             dlugosc = len(zakodowane)
#             fs = 2 ** 10  # częstotliwość próbkowania
#             Tb = 1  # czas trwania bitu
#             Tc = Tb * len(zakodowane)  # czas trwania całego ciągu
#             fn = W * Tb**-1 #częstotliwość nośnej
#             fn1 = (W + 1)/Tb #częstotliwość nośnej
#             fn2 = (W + 2)/Tb #częstotliwość nośnej
#             A1 = 2 #amplituda
#             A2 = 7 #amplituda
#             N = round(Tc * fs) #ilość próbek
#             t = np.linspace(0, Tc, N) #wektor czasu
#
#             if m == 'ASK':
#                 ASK = kluczowanie_amplitudy(t, zakodowane, A1, A2, fn, N)
#                 ASK = szum_bialy(ASK, a)
#                 ASK = tlumienie(ASK, b, t)
#                 # plt.plot(t, ASK)
#                 # plt.title("ASK szum + tlumienie" + str(a))
#                 # plt.show()
#                 xt, pt, ct = demodulacjaASK(t, ASK, N, fn, zakodowane)
#                 # plt.plot(t, pt)
#                 # plt.show()
#                 # plt.plot(t, ct)
#                 # plt.show()
#             elif m == 'FSK':
#                 FSK = kluczowanie_czestotliwosci(t, zakodowane, N, fn1, fn2)
#                 FSK = szum_bialy(FSK, a)
#                 FSK = tlumienie(FSK, b, t)
#                 # plt.plot(t, FSK)
#                 # plt.title("FSK szum + tlumienie" + str(a))
#                 # plt.show()
#                 xt1, xt2, pt1, pt2, ct = demodulacjaFSK(t, FSK, N, fn1, fn2, fs, zakodowane)
#             elif m == 'PSK':
#                 PSK = kluczowanie_fazy(t, zakodowane, N, fn)
#                 PSK = szum_bialy(PSK, a)
#                 PSK = tlumienie(PSK, b, t)
#                 # plt.plot(t, PSK)
#                 # plt.title("PSK szum + tlumienie" + str(a))
#                 # plt.show()
#                 xt, pt, ct = demodulacjaPSK(t, PSK, N, fn, zakodowane)
#             bitstream = ct_to_bitstream(ct, N, len(zakodowane))
#
#             for i in range(len(bitstream)):
#                 bitstream[i] = int(bitstream[i])
#
#             for i in range(0, len(bitstream), 7):
#                 ham = dekoderHamminga(bitstream[i:i + 7])
#                 zdekodowane.extend(ham)
#
#             for j in range(len(zdekodowane)):
#                 zdekodowane[j] = str(zdekodowane[j])
#
#             print("Początkowa wartość szum " + str(a) + " tlumienie " + str(b) + ": " + m + " ", tekst, sep="\n")
#             print("Wartość po zdekodowaniu szum + tlumienie:", zdekodowane, sep="\n")
#             BER = 0
#             for i in range(len(tekst)):
#                 if tekst[i] != zdekodowane[i]:
#                     BER += 1
#             BER = BER/len(tekst)
#             print("BER:", BER)
#             print("\n\n")
#             df3 = pd.concat([df3, pd.DataFrame([[m, a, b, BER]], columns=['Modulacja', 'Alfa', 'Beta', 'BER'])], ignore_index=True)
# print(df3)



df4 = pd.DataFrame(columns=['Modulacja', 'Alfa', 'Beta', 'BER'])
for m in modulacje:
    for b in beta:
        for a in alfa:
            zakodowane = []
            zdekodowane = []
            for i in range(0, len(tekst), 4):
                ham = koderHamminga(tekst[i:i + 4], n)
                zakodowane.extend(ham)

            for j in range(len(zakodowane)):
                zakodowane[j] = str(zakodowane[j])

            dlugosc = len(zakodowane)
            fs = 2 ** 10  # częstotliwość próbkowania
            Tb = 1  # czas trwania bitu
            Tc = Tb * len(zakodowane)  # czas trwania całego ciągu
            fn = W * Tb**-1 #częstotliwość nośnej
            fn1 = (W + 1)/Tb #częstotliwość nośnej
            fn2 = (W + 2)/Tb #częstotliwość nośnej
            A1 = 2 #amplituda
            A2 = 7 #amplituda
            N = round(Tc * fs) #ilość próbek
            t = np.linspace(0, Tc, N) #wektor czasu

            if m == 'ASK':
                ASK = kluczowanie_amplitudy(t, zakodowane, A1, A2, fn, N)
                ASK = tlumienie(ASK, b, t)
                ASK = szum_bialy(ASK, a)
                plt.plot(t, ASK)
                plt.title("ASK tlumienie + szum" + str(a))
                plt.show()
                xt, pt, ct = demodulacjaASK(t, ASK, N, fn, zakodowane)
            elif m == 'FSK':
                FSK = kluczowanie_czestotliwosci(t, zakodowane, N, fn1, fn2)
                FSK = tlumienie(FSK, b, t)
                FSK = szum_bialy(FSK, a)
                plt.plot(t, FSK)
                plt.title("FSK tlumienie + szum" + str(a))
                plt.show()
                xt1, xt2, pt1, pt2, ct = demodulacjaFSK(t, FSK, N, fn1, fn2, fs, zakodowane)
            elif m == 'PSK':
                PSK = kluczowanie_fazy(t, zakodowane, N, fn)
                PSK = tlumienie(PSK, b, t)
                PSK = szum_bialy(PSK, a)
                plt.plot(t, PSK)
                plt.title("PSK tlumienie + szum" + str(a))
                plt.show()
                xt, pt, ct = demodulacjaPSK(t, PSK, N, fn, zakodowane)
            bitstream = ct_to_bitstream(ct, N, len(zakodowane))

            for i in range(len(bitstream)):
                bitstream[i] = int(bitstream[i])

            for i in range(0, len(bitstream), 7):
                ham = dekoderHamminga(bitstream[i:i + 7])
                zdekodowane.extend(ham)

            for j in range(len(zdekodowane)):
                zdekodowane[j] = str(zdekodowane[j])

            print("Początkowa wartość tlumienie " + str(b) + " szum " + str(a) + ": " + m + " ", tekst, sep="\n")
            print("Wartość po zdekodowaniu tlumienie + szum:", zdekodowane, sep="\n")
            BER = 0
            for i in range(len(tekst)):
                if tekst[i] != zdekodowane[i]:
                    BER += 1
            BER = BER/len(tekst)
            print("BER:", BER)
            print("\n\n")
            df4 = pd.concat([df4, pd.DataFrame([[m, a, b, BER]], columns=['Modulacja', 'Alfa', 'Beta', 'BER'])], ignore_index=True)
print(df4)
