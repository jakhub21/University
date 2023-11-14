import librosa as librosa
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
s, fs = sf.read('ZUT-Department-of-Computer-Science.wav', dtype='float32')
# sd.play(s, fs)
status = sd.wait()

s = s/np.max(np.abs(s))
czas = np.arange(0,s.shape[0])/fs
plt.figure()
plt.plot(czas,s)


frame_length_ms = 10
frame_length_samples = int(frame_length_ms * fs / 1000)
frames = []
num_frames = int(np.ceil(len(s) / frame_length_samples))

for i in range(num_frames):
    start = i * frame_length_samples
    end = (i + 1) * frame_length_samples
    frame = s[start:end]
    frames.append(frame)

energies = []
zero_crossing_rates = []

for frame in frames:
    energy = np.sum(frame ** 2)
    zero_crossings = np.sum(np.abs(np.diff(np.sign(frame)))) / (2 * len(frame))
    energies.append(energy)
    zero_crossing_rates.append(zero_crossings)

energies = energies / np.max(energies)
zero_crossing_rates = zero_crossing_rates / np.max(zero_crossing_rates)
x = np.arange(0, num_frames)*frame_length_ms/1000
plt.plot(x, energies, 'r')
plt.plot(x, zero_crossing_rates, 'g')
plt.savefig("energia.png")
plt.show()

#zadanie 3
#maksima wskazują na obszary wysokiej energii, a minima na obszary niskiej energii lub zerowego przekroczenia.
#mozna wykorzystac je do podzialu sygnalu na segmenty dzwiekowe.
#Funkcja Z (zero-crossing rates) odzwierciedla liczbę zmian znaku sygnału w czasie i może być użyta do rozróżnienia głosek dźwięcznych od bezdźwięcznych.
#Funkcja E (energies) odzwierciedla poziom energii w sygnale i również może być użyta do rozróżnienia głosek dźwięcznych od bezdźwięcznych.
#Na podstawie funkcji Z i E można automatycznie rozdzielić wiele typów głosek, takich jak:
#Głoski dźwięczne
#Głoski bezdźwięczne
#Pauzy międzygłosowe

fig, axs = plt.subplots(2,2,figsize=(15,15))
okna = [5, 10, 20, 50]
tmp = 0
for j in range(0, 2):
    for k in range(0, 2):
        frame_length_samples = int(okna[tmp] * fs / 1000)
        frames = []
        num_frames = int(np.ceil(len(s) / frame_length_samples))

        for i in range(num_frames):
            start = i * frame_length_samples
            end = (i + 1) * frame_length_samples
            frame = s[start:end]
            frames.append(frame)

        energies = []
        zero_crossing_rates = []

        for frame in frames:
            energy = np.sum(frame ** 2)
            zero_crossings = np.sum(np.abs(np.diff(np.sign(frame)))) / (2 * len(frame))
            energies.append(energy)
            zero_crossing_rates.append(zero_crossings)

        energies = energies / np.max(energies)
        zero_crossing_rates = zero_crossing_rates / np.max(zero_crossing_rates)
        x = np.arange(0, num_frames) * okna[tmp] / 1000
        axs[j, k].plot(czas, s)
        axs[j, k].plot(x, energies, 'r')
        axs[j, k].plot(x, zero_crossing_rates, 'g')
        axs[j, k].set_title('frame_length_ms = ' + str(okna[tmp]))
        tmp += 1
plt.savefig("energia1.png")
plt.show()

fig, axs = plt.subplots(2,2,figsize=(15,15))
okna = [5, 10, 20, 50]
tmp = 0
for j in range(0, 2):
    for k in range(0, 2):
        frame_length_samples = int(okna[tmp] * fs / 2000)
        frames_lenght_reduced = frame_length_samples // 2
        frames = []
        num_frames = int(np.ceil(len(s) / frame_length_samples))

        for i in range(num_frames):
            start = i * frame_length_samples - frames_lenght_reduced
            end = (i + 1) * frame_length_samples - frames_lenght_reduced
            frame = s[start:end]
            frames.append(frame)

        energies = []
        zero_crossing_rates = []

        for frame in frames:
            energies = np.append(energies, np.array(np.sum(frame ** 2)))
            zero_crossing_rates = np.append(zero_crossing_rates, np.array(np.sum(np.abs(np.diff(np.sign(frame)))) / (2 * frame_length_samples)))


        energies = energies / np.max(energies)
        zero_crossing_rates = zero_crossing_rates / np.max(zero_crossing_rates)
        x = np.arange(0, num_frames) * okna[tmp] / 2000
        axs[j, k].plot(czas, s)
        axs[j, k].plot(x, energies, 'r')
        axs[j, k].plot(x, zero_crossing_rates, 'g')
        axs[j, k].set_title('frame_length_ms = ' + str(okna[tmp]))
        tmp += 1
plt.savefig("energia2.png")
plt.show()

start_sample = int(fs * 2.3)
end_sample = start_sample + 2048
samogloska = s[start_sample:end_sample]
okno_hamminga = np.hamming(2048)
samogloska_maskowana = samogloska * okno_hamminga
W = scipy.fftpack.fft(samogloska_maskowana)
widmo_amp = 20 * np.log10(np.abs(W))
amplitude_spectrum = np.log10(np.abs(scipy.fftpack.fft(samogloska_maskowana)))
frequencies = np.linspace(0, fs, len(widmo_amp))

plt.figure(figsize=(20, 10))
plt.subplot(2, 4, (1, 4))
plt.plot(czas, s)
plt.plot(x, energies, 'r')
plt.plot(x, zero_crossing_rates, 'g')

plt.subplot(2, 4, 5)
plt.plot(frequencies, widmo_amp)
plt.xlim(0, 10000)

plt.subplot(2, 4, 6)
plt.plot(okno_hamminga)

plt.subplot(2, 4, 7)
plt.plot(samogloska*okno_hamminga)

plt.subplot(2, 4, 8)
plt.plot(amplitude_spectrum)
plt.savefig("widmo.png")
plt.show()

#Wizualnie, widmo głosek dźwięcznych będzie charakteryzować się obecnością wyraźnych i regularnych pasm harmonicznych,
#które są równo rozmieszczone wzdłuż osi częstotliwości. Pasma te reprezentują kolejne harmoniczne.
#Natomiast w przypadku głosek bezdźwięcznych, widmo będzie bardziej chaotyczne, bez wyraźnych pasm harmonicznych.
#Widma samogłosek mogą różnić się między sobą.
#Różne głoski mogą mieć różne wysokości tonu, co prowadzi do różnych wartości F0.
#Na przykład, samogłoski o wyższym tonie będą miały wyższe wartości F0, podczas gdy samogłoski o niższym tonie będą miały niższe wartości F0.


#zadanie 4
s1, fs1 = sf.read('samogloski.wav', dtype='float32')
s1 = s1/np.max(np.abs(s1))
czas1 = np.arange(0,s1.shape[0])/fs



okno = np.hamming(2048)
plt.figure(figsize=(20, 10))
for i in range(1, 7):
    start_sample = int(fs1 * i)
    end_sample = start_sample + 2048
    samogloska = s1[start_sample:end_sample]
    samogloska_maskowana = samogloska * okno

    widmo_amp = 20 * np.log10(np.abs(scipy.fftpack.fft(samogloska_maskowana)))

    a = librosa.lpc(samogloska, order=46)
    a = np.pad(a, (0, len(samogloska) - len(a)), mode='constant')

    lpc_spectrum = np.abs(scipy.fftpack.fft(a, 2048))
    lpc_spectrum = 20 * np.log10(lpc_spectrum)
    lpc_spectrum = -lpc_spectrum

    frequencies = np.linspace(0, fs1, len(widmo_amp))

    plt.subplot(2, 3, i)
    plt.plot(frequencies, widmo_amp*2, 'b')
    plt.plot(frequencies, lpc_spectrum-50, 'r')
    plt.xlim(0, 4000)

plt.savefig("samogloski.png")
plt.show()

#Liniowe Kodowanie Predykcyjne (Linear Predictive Coding, LPC) jest techniką stosowaną w przetwarzaniu
# sygnałów audio do modelowania i kompresji dźwięku. Polega na estymacji wartości przyszłych próbek sygnału
# na podstawie liniowej kombinacji poprzednich próbek.