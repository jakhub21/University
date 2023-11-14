import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
'''Dyskretyzacja'''
'''zad1'''
fs = [10, 20, 21, 30, 45, 50, 100, 150, 200, 250, 1000]
f = 10
'''zad2'''
def xfun(f,fs):
    t = np.arange(0, 1, 1/fs)
    s = np.sin(2*np.pi*f*t)
    return t, s

'''zad3'''
fig, axs = plt.subplots(nrows=len(fs), ncols=1, figsize=(10, 20))
for i, ax in enumerate(axs):
    t, s = xfun(f, fs[i])
    ax.plot(t, s)
    ax.set_title(f"fs={fs[i]}")
    ax.set_xlabel("Czas [s]")
    ax.set_ylabel("Amplituda")
plt.tight_layout()
plt.savefig("sin_all.png")
plt.show()
'''zad4'''
# Twierdzenie Nyquista mówi o tym jaka powinna być częstotliwość próbkowania gdy znamy najwyższą składową częstotliwości w mierzonym sygnale.
# Jak szybko próbkować ? Dithering polega na celowym dodaniu szumu do sygnału wejściowego w celu zmniejszenia zakłóceń.

'''zad5'''
# Aliasing – nieodwracalne zniekształcenie sygnału w procesie próbkowania wynikające z niespełnienia założeń twierdzenia o próbkowaniu.
# Zniekształcenie objawia się obecnością w wynikowym sygnale składowych o błędnych częstotliwościach (aliasów).

'''zad6'''
img = mpimg.imread('aliasing.jpeg')
height = img.shape[0]
width = img.shape[1]
imgplot = plt.imshow(img, interpolation='lanczos')
plt.show()


'''Kwantyzacja'''
'''zad2-3'''
print(img.shape)
'''zad4'''
R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
szary1 = (np.max([R, G, B], axis=0) + np.min([R, G, B], axis=0))/2
szary2 = (R+G+B)/3
szary3 = 0.21*R + 0.72*G + 0.07*B
plt.imshow(szary1, cmap='gray')
plt.show()
plt.imshow(szary2, cmap='gray')
plt.show()
plt.imshow(szary3, cmap='gray')
plt.show()
'''zad5'''
hist_szary1, bin_edges_szary1 = np.histogram(szary1,bins="auto")
hist_szary2, bin_edges_szary2 = np.histogram(szary2,bins="auto")
hist_szary3, bin_edges_szary3 = np.histogram(szary3,bins="auto")

plt.figure(figsize = (20,10))
plt.subplot(3,2,1)
plt.imshow(szary1, cmap='gray')
plt.title('Szary 1')

plt.subplot(3,2,2)
plt.bar(bin_edges_szary1[:-1], hist_szary1, width=1)
plt.title('Histogram szary 1')

plt.subplot(3,2,3)
plt.imshow(szary2, cmap='gray')
plt.title('Szary 2')

plt.subplot(3,2,4)
plt.bar(bin_edges_szary2[:-1], hist_szary2, width=1)
plt.title('Histogram szary 2')

plt.subplot(3,2,5)
plt.imshow(szary3, cmap='gray')
plt.title('Szary 3')

plt.subplot(3,2,6)
plt.bar(bin_edges_szary3[:-1], hist_szary3, width=1)
plt.title('Histogram szary 3')
plt.savefig("szary.png")
plt.show()
'''zad6'''
hist_szary1, bin_edges_szary1 = np.histogram(szary1, bins=16)
plt.figure(figsize = (20,10))
plt.subplot(2,2,1)
dig = np.digitize(szary1, bin_edges_szary1[:-1])
dig = np.round((bin_edges_szary1[dig[:-1]] + bin_edges_szary1[dig[:-1]])/2)
plt.imshow(dig, cmap='gray')
plt.title('Szary 4')

plt.subplot(2,2,2)
plt.bar(bin_edges_szary1[:-1], hist_szary1, width=1)
plt.title('Histogram szary 4 zad 6')

'''zad7'''
macierz = np.zeros((height, width))
for i in range(len(bin_edges_szary1)-1):
    mean = (bin_edges_szary1[i] + bin_edges_szary1[i+1])/2
    for j in range(height):
        for k in range(width):
            if szary1[j][k] >= bin_edges_szary1[i] and szary1[j][k] < bin_edges_szary1[i+1]:
                macierz[j][k] = mean

hist_szary4, bin_edges_szary4 = np.histogram(macierz, bins="auto")
plt.subplot(2,2,3)
plt.imshow(macierz, cmap='gray')
plt.title('Szary 5')
plt.subplot(2,2,4)
plt.bar(bin_edges_szary4[:-1], hist_szary4, width=1)
plt.title('Histogram szary 5 zad 7')
plt.savefig("szary2.png")
plt.show()

'''Binaryzacja'''
'''zad1'''
img = plt.imread('pilka.png')
plt.figure(figsize=(9,12))
plt.subplot(3,1,1)
plt.imshow(img)
img = (img*255).astype(int)
R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
img = 0.21*R + 0.72*G + 0.07*B
hist, bins = np.histogram(img, bins="auto")
plt.subplot(3,2,3)
plt.imshow(img, cmap='gray')
plt.title('Obraz "pilka.png"')
plt.subplot(3,2,4)
plt.bar(bins[:-1], hist, width=1)



'''zad3'''
def find_threshold(histogram, num_bins, threshold_factor=1.0):
    total_pixels = np.sum(histogram)
    sum_bg, sum_fg = 0, 0
    w_bg, w_fg = 0, 0
    max_var, threshold = 0, 0
    for i in range(num_bins):
        w_bg += histogram[i]
        if w_bg == 0:
            continue
        w_fg = total_pixels - w_bg
        if w_fg == 0:
            break
        sum_bg += i * histogram[i]
        mean_bg = sum_bg / w_bg
        sum_fg = sum(histogram[i+1:] * np.arange(i+1, num_bins))
        mean_fg = sum_fg / w_fg
        var_between = w_bg * w_fg * (mean_bg - mean_fg) ** 2
        if var_between > max_var:
            max_var = var_between
            threshold = i
    threshold *= threshold_factor
    return threshold

threshold = find_threshold(hist, len(bins)-1, 0.1)
# print(threshold)

'''zad4'''
img[img > threshold] = 255
img[img <= threshold] = 0
plt.subplot(3,2,5)
plt.imshow(img, cmap='gray')
plt.title('Obraz "pilka.png" po binaryzacji')
plt.subplot(3,2,6)
plt.bar(bins[:-1], hist, width=1)
plt.savefig("binaryzacja.png")
plt.show()



