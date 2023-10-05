# utk operasi numerik dan manipulasi data.
import numpy as np
# Import class 'Counter' dari modul 'Collection', untuk menghitung frekuensi kemunculan elemen
from collections import Counter
import re


# Fungsi untuk mengonversi kunci
def konversi_kunci(kunci):
    # Membuat list kosong.
    sortkunci = []
    # Menambahkan kunci ke list sortkunci.
    sortkunci.append(kunci)
    # Menambahkan list kosong ke list sortkunci.
    sortkunci.append([])
    # Loop untuk menambahkan indeks ke list sortkunci.
    i = 0
    while i < len(kunci):
        sortkunci[1].append(i + 1)
        i += 1

    # Mengubah list sortkunci menjadi array, di mana baris pertama berisi elemen-elemen list kunci dan baris kedua berisi nilai-nilai dari 1 hingga panjang kunci.
    sortkunci = np.array(sortkunci)
    # Mengurutkan kunci yang ditampung pada variabel newsortkunci
    newsortkunci = sortkunci[:, sortkunci[0].argsort()]
    # Mengubah array menjadi list. Hasilnya adalah sortkunci yang kini berisi data yang telah diurutkan.
    sortkunci = newsortkunci.tolist()
    # Menambahkan list kosong ke list sortkunci.
    sortkunci.append([])
    # Menghitung jumlah huruf yang sama.
    hitung = Counter(sortkunci[0])
    # Loop untuk menambahkan indeks ke list sortkunci
    i = 0
    n = 1
    while i < len(kunci):
        # Mengecek jika ada elemen yang sama
        if hitung[sortkunci[0][i]] > 1:
            for j in range(hitung[sortkunci[0][i]]):
                sortkunci[2].append(n)
               # Menambahkan nilai i dengan jumlah huruf yang sama dikurangi 1. Sehingga huruf yang sama memiliki nilai urutan yang sama
            i += (hitung[sortkunci[0][i]] - 1)
        else:
            sortkunci[2].append(n)
        n += 1
        i += 1
    # Mengubah list sortkunci menjadi array.
    sortkunci = np.array(sortkunci)
    # Mengurutkan indeks berdasarkan urutan elemen awal yang terdapat pada kunci
    newsortkunci = sortkunci[:, sortkunci[1].argsort()]
    return ' '.join(map(str, newsortkunci[2]))


def encrypt(teks, kunci):
    enkripsi = []
    enkripsi.append(kunci)

    # Hanya mengambil huruf-huruf dan spasi dari teks, mengabaikan karakter khusus
    teks = re.sub(r'[^A-Za-z\s]', '', teks)

    # ganti spasi
    teks = teks.replace(" ", "-")
    teks = teks.upper()

    for i in range(0, len(teks), len(kunci)):
        x = teks[i: i + len(kunci)]
        x = list(x)
        enkripsi.append(x)

    while len(enkripsi[len(enkripsi) - 1]) < len(kunci):
        # ganti simbol disini
        enkripsi[len(enkripsi) - 1].append("~")

    enkripsi = np.array(enkripsi)
    print(" " + np.array2string(enkripsi[1: len(enkripsi)],
                                formatter={"str_kind": lambda x: x},
                                separator=" ",
                                )[1:-1])

    # jk mulai dari angka terbesar = enkripsi[:, enkripsi[0].argsort()[::-1]]
    newenkripsi = enkripsi[:, enkripsi[0].argsort()]
    # Counter({'U': 2, 'D': 1, 'I': 1, 'N': 1, 'S': 1})
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
    teks = 'Pada jaman dahulu kala, di lembah gunung Telomayo hiduplah sepasang suami istri yang bernama Ki Hajar dan Nyai Selakanta. Mereka hidup sederhana dan belum dikarunia keturunan. Ki Hajar akhirnya memutuskan untuk pergi bertapa di Gunung Telomoyo untuk memohon kepada Yang Maha Kuasa agar dikarunia seorang anak. Setelah beberapa lama Ki Hajar bertapa di gunung, sang istri kemudian hamil. Perut Nyai Selakanta pun semakin hari semakin membesar hingga akhirnya melahirkan seorang anak. Namun betapa terkejutnya Nyai Selakanta, ternyata yang dilahirkan olehnya bukanlah bayi manusia melainkan seekor Naga. Ajaibnya naga tersebut dapat berbicara dan Nyai Selakanta pun menamainya Baru Klinting. Hari demi hari Naga Baru Klinting semakin besar. Hingga pada suatu hari dia bertanya kepada ibunya, ”Ibu di manakah keberadaan ayahku”?. Nyai Selakanta pun memberitahukan bahwa ayahnya sedang bertapa di lereng Gunung Telomoyo. Naga Baru Kiinting pun pergi kesana dan bertemu seorang pria tua yang merupakan ayahnya. Ki Hajar tidak percaya begitu saja dengan Naga Baru Klinting, “jika kamu memang anakku, coba lingkari gunung ini dengan tubuhmu”. Naga Baru Klinting melaksanakan dan berhasil. Ki Hajar akhimya percaya, setelah melihat klintingan (lonceng kecil) yang dikalungkan Nyai Selakanta di leher Baru Klinting. Dan supaya dirinya berubah menjadi manusia, ia harus bertapa di Bukit Tugur. Naga Baru Khlintingpun dengan senang hati melaksanakan perintah ayahnya tersebut. Pada saat itu, penduduk desa yang berada di bawah Bukit Tugur sedang berburu binatang buruan di hutan. Tiba-tiba mereka melihat Naga Baru Klinting yang diam di dalam Gua. Oleh karena mereka tidak satupun mendapatkan binatang, akhirnya para penduduk itu memotong tubuh Naga Baru Klinting untuk di jadikan makanan. Kemudian para penduduk desa itu pulang dan mengadakan pesta besarbesaran karena telah mendapatkan daging yang banyak. Ketika mereka sedang menikmati makanan pesta, datanglah seorang anak kecil yang kumel dan bau. Anak itu mendekat dan berharap untuk diberikan makanan. Namun penduduk desa menolaknya, ”Pergilah kau dasar pengemis!, tubuhmu kotor dan bau!”. Melihat kejadian itu seorang nenek tua yang bemama Nyai Latung merasa kasihan. ”Nak ikutlah ke rumah nenek!” kata nenek itu. Anak itu lalu mengikuti ke rumahnya. Disana ia diberi makanan yang banyak. hingga menghabiskan semua makanan yang dihidangkan. “Terimakasih, Nenek sangat baik tidak seperti penduduk desa itu!” kata anak itu. Sebelum pergi anak itu berpesan bahwa jika nanti mendengar suara gemuruh, carilah sebuah lesung dan naiklah diatasnya.Kemudian anak tersebut kembali ke pesta yang meriah itu. Ia kembali meminta makanan kepada warga desa. ”Pak kasihanilah saya pak?, berilah makanan sedikit saja”. Akan tetapi, penduduk desa itu makin menjadi marah, “kamu lagi, sana pergi jauh. kamu sudah mengganggu pesta disini”, kata seorang warga desa sambil menendang anak itu hingga tersungkur. Anak itu kemudian bangkit dan mengeluarkan sebuah lidi lalu ditancapkannya di tanah, Wahai kalian penduduk desa, jika kalian bisa mencabut lidi ini, Aku akan pergi dan tidak mengganggu kalian lagi”, pinta anakitu.Satu persatu warga desa mencoba mencabut lidi itu. Tetapi anehnya tidak ada seorangpun dapat mencabutnya. “Payah kalian, hanya mencabut lidi sekecil itu saja tidak mampu,“ ejek anak itu Akhirnya anak itu mencabut lidi yang tertancap di tanah. Tiba-tiba lubang tanah bekas tancapan lidi tersebut mengeluarkan air yang semakin lama semakin deras. Air tersebut berubah menjadi banjir yang besar hingga menenggelamkan seluruh desa yang angkuh tersebut. Tak seorangpun dapat selamat kecuali nenek tua yang menaiki Iesungnya. Tak lama setelah itu, Ki Hajsar mendatangi anak kecil tersebut dan mengajaknya pergi menemui Nyai Selakanta. Ternyata anak kecil itu adalah penjelmaan dari Naga Baru Klinting yang tubuhnya telah dimakan penduduk desa. Hingga saat ini rendaman air itu masih ada dan menjadi telaga yang dikenal dengan Telaga Rawa Pening.'
    kunci = "udinus"
    kunci = list(kunci.upper())

    print("\nK:", konversi_kunci(kunci))
    encrypt(teks, kunci)


if __name__ == "__main__":
    main()
