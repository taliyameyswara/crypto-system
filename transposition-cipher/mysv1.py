# utk operasi numerik dan manipulasi data.
import numpy as n
# Import class 'Counter' dari modul 'Collection', untuk menghitung frekuensi kemunculan elemen

from collections import Counter


def konversi_kunci(kunci):
    sortkunci = []
    sortkunci.append(kunci)
    sortkunci.append([])
    i = 0
    while i < len(kunci):
        sortkunci[1].append(i + 1)
        i += 1

    sortkunci = np.array(sortkunci)
    newsortkunci = sortkunci[:, sortkunci[0].argsort()]
    sortkunci = newsortkunci.tolist()
    sortkunci.append([])
    hitung = Counter(sortkunci[0])
    i = 0
    n = 1
    while i < len(kunci):
        if hitung[sortkunci[0][i]] > 1:
            for j in range(hitung[sortkunci[0][i]]):
                sortkunci[2].append(n)
            i += (hitung[sortkunci[0][i]] - 1)
        else:
            sortkunci[2].append(n)
        n += 1
        i += 1

    sortkunci = np.array(sortkunci)
    newsortkunci = sortkunci[:, sortkunci[1].argsort()]
    return ' '.join(map(str, newsortkunci[2]))


def encrypt(teks, kunci):
    enkripsi = []
    enkripsi.append(kunci)

    # Hanya mengambil huruf-huruf dari teks, mengabaikan karakter khusus
    teks = ''.join(filter(str.isalpha, teks))
    teks = teks.upper()

    for i in range(0, len(teks), len(kunci)):
        x = teks[i: i + len(kunci)]
        x = list(x)
        enkripsi.append(x)

    while len(enkripsi[len(enkripsi) - 1]) < len(kunci):
        enkripsi[len(enkripsi) - 1].append("~")

    enkripsi = np.array(enkripsi)
    print(" " + np.array2string(enkripsi[1: len(enkripsi)],
                                formatter={"str_kind": lambda x: x},
                                separator=" ",
                                )[1:-1])

    newenkripsi = enkripsi[:, enkripsi[0].argsort()]
    hitung = Counter(newenkripsi[0])
    hasil = []
    i = 0
    while i < len(newenkripsi[0]):
        if hitung[newenkripsi[0][i]] == 1:
            for j in range(1, len(newenkripsi)):
                hasil.append(newenkripsi[j][i])
        else:
            for j in range(1, len(newenkripsi)):
                for k in range(i, hitung[newenkripsi[0][i]] + i):
                    hasil.append(newenkripsi[j][k])
            i += (hitung[newenkripsi[0][i]] - 1)
        i += 1

    hasil_enkripsi = "".join(hasil)
    hasil_enkripsi = hasil_enkripsi.replace(" ", "")
    print("\nHasil enkripsi =", hasil_enkripsi)


def main():
    teks = "Hey! This is a test. lol() fuck"" bye / lmao?"
    kunci = "kunci"
    kunci = list(kunci.upper())

    print("\nK:", konversi_kunci(kunci))
    encrypt(teks, kunci)


if __name__ == "__main__":
    main()
