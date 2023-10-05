import math  # Import module math untuk fungsi ceil() dan floor()


def tampilkan_menu():  # Fungsi untuk menampilkan menu
    print(
        "PROGRAM ENKRIPSI-DEKRIPSI ORTHOGONAL TRANSPOSITION"
    )  # Menampilkan judul program
    print("\n[MENU]")  # Menampilkan menu
    print(" [1] Enkripsi")
    print(" [2] Dekripsi")
    print(" [3] Keluar")


def orthogonal_encrypt(plain_text, step_size):  # Fungsi untuk enkripsi
    matrix_representation = (
        []
    )  # Matriks kosong untuk menyimpan representasi matriks dari teks
    encrypted_text = ""  # Teks terenkripsi

    for i in range(step_size):  # Mengisi matriks dengan karakter dari teks
        matrix_row = []  # Baris matriks
        # Loop ini akan mengulangi sebanyak kolom yang diperlukan dalam matriks, dan jumlah kolom dihitung dengan
        # membagi panjang teks (len(plain_text)) dengan step_size, dan menggunakan math.ceil()
        # untuk memastikan hasil pembagian dibulatkan ke atas agar semua karakter teks dapat masuk.
        for j in range(math.ceil(len(plain_text) / step_size)):
            index = (
                j * step_size
                + i  # j = indeks kolom saat ini, step_size = jumlah baris, i = indeks baris saat ini
            )  # Indeks karakter yang akan dimasukkan ke dalam baris matriks
            if index < len(
                plain_text
            ):  # Jika masih ada karakter yang tersisa, masukkan karakter ke dalam baris matriks
                matrix_row.append(
                    plain_text[index]
                )  # Masukkan karakter ke dalam baris matriks
            else:  # Jika tidak ada karakter yang tersisa, masukkan karakter '@' ke dalam baris matriks
                # Masukkan karakter '@' ke dalam baris matriks
                matrix_row.append("@")
        matrix_representation.append(
            matrix_row
        )  # Masukkan baris matriks ke dalam matriks representasi

    print("Matrix:\n")  # Tampilkan matriks representasi
    for row in matrix_representation:  # Untuk setiap baris dalam matriks representasi
        print(row)  # Tampilkan baris

    # proses enkripsi
    matrix_height = step_size  # Tinggi matriks
    matrix_width = math.ceil(len(plain_text) / matrix_height)  # Lebar matriks

    for i in range(matrix_height - 1, -1, -1):  # Mulai dari baris terakhir
        if matrix_height % 2 == 0:  # Jika height matriks genap
            if i % 2 != 0:  # Pasti baris ganjil
                for j in range(matrix_width - 1, -1, -1):  # Bergerak dari kanan ke kiri
                    # Jika bukan karakter '@'
                    if matrix_representation[i][j] != "@":
                        encrypted_text += matrix_representation[i][
                            j
                        ]  # Tambahkan karakter ke dalam teks terenkripsi
                    else:  # Jika karakter '@'
                        encrypted_text += (
                            "@"  # Tambahkan karakter '@' ke dalam teks terenkripsi
                        )
            else:  # Jika baris ganjil
                for j in range(matrix_width):  # Bergerak dari kiri ke kanan
                    # Jika bukan karakter '@'
                    if matrix_representation[i][j] != "@":
                        encrypted_text += matrix_representation[i][
                            j
                        ]  # Tambahkan karakter ke dalam teks terenkripsi
                    else:  # Jika karakter '@'
                        encrypted_text += (
                            "@"  # Tambahkan karakter '@' ke dalam teks terenkripsi
                        )
        else:  # Jika height matriks ganjil
            if i % 2 == 0:  # Pasti baris genap
                for j in range(matrix_width - 1, -1, -1):  # Bergerak dari kanan ke kiri
                    # Jika bukan karakter '@'
                    if matrix_representation[i][j] != "@":
                        encrypted_text += matrix_representation[i][
                            j
                        ]  # Tambahkan karakter ke dalam teks terenkripsi
                    else:  # Jika karakter '@'
                        encrypted_text += (
                            "@"  # Tambahkan karakter '@' ke dalam teks terenkripsi
                        )
            else:  # Jika baris ganjil
                for j in range(matrix_width):  # Bergerak dari kiri ke kanan
                    # Jika bukan karakter '@'
                    if matrix_representation[i][j] != "@":
                        encrypted_text += matrix_representation[i][
                            j
                        ]  # Tambahkan karakter ke dalam teks terenkripsi
                    else:  # Jika karakter '@'
                        encrypted_text += (
                            "@"  # Tambahkan karakter '@' ke dalam teks terenkripsi
                        )
    return encrypted_text


def orthogonal_decrypt(cipher_text, step_size):  # Fungsi untuk dekripsi
    matrix_height = step_size  # Tinggi matriks
    matrix_width = math.ceil(len(cipher_text) / matrix_height)  # Lebar matriks

    plain_text_matrix = (
        [  # Matriks kosong untuk menyimpan representasi matriks dari teks
            [" " for _ in range(matrix_width)] for _ in range(matrix_height)
        ]
    )

    idx = 0  # Indeks untuk mengakses karakter dalam teks terenkripsi

    for i in range(matrix_height - 1, -1, -1):  # Mulai dari baris terakhir
        if matrix_height % 2 == 0:  # Jika tinggi matriks genap
            if i % 2 != 0:  # Jika baris genap
                for j in range(matrix_width - 1, -1, -1):  # Bergerak dari kanan ke kiri
                    plain_text_matrix[i][j] = cipher_text[
                        idx
                    ]  # Masukkan karakter ke dalam matriks
                    idx += 1  # Tambahkan indeks
            else:  # Jika baris ganjil
                for j in range(matrix_width):  # Bergerak dari kiri ke kanan
                    plain_text_matrix[i][j] = cipher_text[
                        idx
                    ]  # Masukkan karakter ke dalam matriks
                    idx += 1  # Tambahkan indeks
        else:
            if i % 2 == 0:  # Jika baris genap
                for j in range(matrix_width - 1, -1, -1):  # Bergerak dari kanan ke kiri
                    plain_text_matrix[i][j] = cipher_text[
                        idx
                    ]  # Masukkan karakter ke dalam matriks
                    idx += 1  # Tambahkan indeks
            else:  # Jika baris ganjil
                for j in range(matrix_width):  # Bergerak dari kiri ke kanan
                    plain_text_matrix[i][j] = cipher_text[
                        idx
                    ]  # Masukkan karakter ke dalam matriks
                    idx += 1  # Tambahkan indeks

    print("Matrix:\n")  # Tampilkan matriks representasi
    for row in plain_text_matrix:  # Untuk setiap baris dalam matriks representasi
        print(row)  # Tampilkan baris

    plain_text = ""  # Teks terdekripsi
    for j in range(matrix_width):  # Untuk setiap kolom dalam matriks representasi
        for i in range(matrix_height):  # Untuk setiap baris dalam matriks representasi
            if plain_text_matrix[i][j] != "@":  # Jika bukan karakter '@'
                plain_text += plain_text_matrix[i][
                    j
                ]  # Tambahkan karakter ke dalam teks terdekripsi

    return plain_text.replace("-", " ")  # Kembalikan - menjadi spasi


while True:
    tampilkan_menu()
    pilih = input("Pilih menu: ")

    if pilih == "1":
        plain_text = 'anjay'

        plain_text = plain_text.replace(
            " ", "-"
        )  # Ganti spasi dengan karakter '-' agar bisa dienkripsi
        step_size = int(input("Masukan kunci (angka): "))  # Masukan kunci
        cipher = orthogonal_encrypt(
            plain_text, step_size
        )  # Panggil fungsi orthogonal_encrypt()
        print("\nCiphertext: " + cipher)  # Tampilkan teks terenkripsi

        lanjut = input("Apakah ingin melanjutkan? (y/n): ")
        if lanjut.lower() != "y":
            print("Terima kasih, program telah keluar.")
            break

    elif pilih == "2":
        cipher_text = ("@ennisdaintr-atd-aneprdng-imassa-l-kainuahi---ardad-cua-egeagk,iste,swntpen-rrjiSutam--hkDi-kusmnjn!-nue-agremtilaesakntd,eeuaabnbibpuning-au---n--ysaaenaigaKmranm-aaa--arinrnmNan-ila-pnybiS-sbr-rYt-urululisauk-nliKederitin-age--n-kmnaaitoynbd--iaiHapinltyioiso--cntmidglamhnairnriaautib--kraiNyGrmgn-iiiemsege-ponnnbmehsae-aake.g-a-ngigrt---aagst-ii-a?s-edi-gkdntudbn,uiieg,ualerbaljea-pbar-aAhne-egkayhn-jieialyn-aaaT@.-yd-aenKa-Tualeany-nthnaa-lnekiatyja-iaon-st”gplldhae-t-a--n.gadn-kkam-e-ancgak.ienrna.m.nunirmgkdiamaiaAae-gKate-dddlgen-e---tueug,erapNpseaeayaaihea-lener.geeildnieadeh-thlnn-iaa-aatrreaia,rbngaudnhubiS--puulguia-h-tku--daaeagiammioeyynbkatauK-n.-k-aSrh-eKksnaedim-iNmrhlg-yhDbua-ghesunBbr-tgmmnapnKau-nb-d-nnsy-ddN-lm--nee-etea-kkaeap-uawn-utkkhed-ana-jaha,adaitstana--niaetaecltsenucteta-.byeu-at-glmigm-lm-hpgn--ngnaaaag-uuli.enc-enaarhrm-usnk-b-nbr--uans-udSgentkeni-i-gng”gulnkkapkama-aas,ehntaesTysaiyminkmbatreia---.--aa.-a-akmj-o-tu-anaau--atrp-n.tn--eN)neke--na-l-pya---Taae-du-urii-pdujn-anNbeh-eydnjbr-aoa-aen-immd-uhhiaaaaak-npypao-auuNsnks--rkhiAb--umlatabaibyp-uiuyn-aKubi.gbatil-l.aarrig-eiyhgbbhilapaatu-eudannkdnhlutk.sggoar--a---nryi-“-ssiaadheinii-pa-nAue-agiregkkndap-uama.-bi-ekbu“iaaa-iriarr-uuomuutreenacerbnnmdgginnaaaiauajetemkaestaeklaierkadhbtch,ta-mapaaul-kba-t-agannannjumd-aaPeirladlunb--e-k-nbnehukhNggohtnrenuaaiaaeaaet-dKirornunatii-na--tnntuemyg-nite--n”-om-jkh-mgrgaamarIyasKeraae-aarean-ai--mnHheseoaar-dkynuhaadb-srNe-aaktmkasa-uetnk-nuytill.srtad-eun”eye-tnareaaaauacguinrsncainn-bgnaa-tawagTlndetiamad-ugsrkysklcbktadeeoienn”aelabaaa.ekdki-er---aelk”yk.u-m-eiweinnku-nkaak-tgcad-hciuknriaiuaebjgegsl-ess--mnknBtkHd-leePdehn-a--e-a-nkj-Ike-nsgn-dmllnTeeAp-natatnrina-ciailraAhm-smiand”aa--ambnhhumnga-annnhbimanm-uaslkpP-nne-ega-ntaend.-Bepbar-ie-ndasaakniu-iiidkei-aatmn-krsdyuteBuramNb-asbu-Bnaraenh-nmaaauukgil-u-orsjiar-e-om-neygbnennauelnKaeK--rpmgkat,aamgeca-ir--t,e--wen-prtai-a-,uhndj,lkg-trdsTleayaebea.mlias--m-knnapkaaamnknduak”--e-yt.uelud-gaaedknra-maaam-bn.smanikg-ig---baadijnudakaee-ayelm-mt-a-ee-tan-akse-aaaaikkpagm.eit--al-sraing-aagdnHmin-a-nibunsgnt.--uaimapkTmwaiike-l-lu-.ulndhr“kej--aamgeilueiseauiNkkng-r-nrna-uMur-uk-na-a-kbp--leaua-an-kdK-nts-dsnnsh-uainan-kaa-iunuaBut--e-aubhn.karanarakita-klauNrge-eii-ti-oebtHuaMa-nalam-magd-hr-u-ThaneadrPasni-jtiuaN-bayaBidey-?ua-Ggnban-t-kkublnHy-gutidjrtK-ah--i-aaa---kayugtnpunna-eitkdepad,am-taLa--u-aneag-td-petgbkdknenshhapa-ea-aitrnl-aa,mAtln---aaP-cmtugh-an-ib-hagTteka-a-rlnhaads-aiawandmie-yNaaeet-ilina-nk-iekgepganti-ea“dd.auaa---akyieauibradp,m-saaeaka-uie-np-au-,nmmaietaeh-ui.hsaumam-aatrgdaap-anatnkahmuktnrdkaasn-ian-lnlnta-aKugkiairai-ua-gbp”hnbak-Hnlra-ibdne.hi-t-t-mSuho-imiar.-nsoiajdlaaraekKeggmar-aas.nihakka--srgeei-aap-uau--ngNpnrkaggja-t-kicaeaaKaehkuakydu-uiueraedtriNuka-krnneadnl-r-dyau”-tiiktik-y--ahkdtmraasamty-kdll-,-h-utom-kigdn-sa,nk-tbui--ykk-iannamnasdrma.p-a-KiupS-l--hdn-aeR-kjui-agiaa--bg-kniatyaaarma-caay-kaen.nttoaa-aiseinindgkaessaauitii-aa-uen-rneuaniidaa-a--a-sa-n!bdnnnauea-mmaeaaura---iailiarhbgadaaagru-my-kkchrKau-in“aejapa--nanakkba-mg.aSbaouagkral-ralipl.aMenrm-idtaype--a,Te-jned.-eum-kk-a-ikareneanynkn--mgaeaiiahtade.gd-pabN-arnrn-einiaua-aBanl-Pudu--eBdOtphkhgmatdsmy-k,-mthaek-uuakyahkkinnguisaeklb-ah-KbaImanriptrn-essanuelaadindutsci-uaasdak-tbntyeejsl-udlea,neaitdrnlk-tniagdeitueiaaaaysauTma-baeents-uau-iani-hypa-nrng-ib-hk-mmun--puaaiakeag--te.naua-e-pbahmgaata-akNeiatuapkriugaia--eaip-nuuka----miuTad-heeB-ihprldolp.aaaa-,--Hug-noreknan-dgsNnait-eanaltamahamgtaaig-npan-saais-adalg-rHk-may-ukndnprnal-s---eyhmeaaani--g-aayauseyianr-anggkgBsl-el-eaua-i-dma.nr-rd-ag.adadbin--gbhgkntnk-ei-la-bdn--l”nusnneik--”bukslaass.arhbit-msm-aaase-hpak--igieeiygn-itandiltbr--ebgsenu--ttrnyy-dttda-m-alg-rau-n-unNkeai.gcuseg-mraie--dia--d,tnndmppnginuWaankr-stua--aed-iatuerydi-ite!itadsiaikA!taaea-,konrbk-aseinarnanatuu-nkanga-uteett--ad,bsBSg(maik-ngnnayieantol-hkamdingiteypys-e-Sagaenehaeaa-auGknnupa-thnaP")  # Masukan teks terenkripsi
        step_size = int(input("Masukan kunci (angka): "))  # Masukan kunci
        deciphered_text = orthogonal_decrypt(
            cipher_text, step_size
        )  # Panggil fungsi orthogonal_decrypt()
        print("\nPlaintext: " + deciphered_text)  # Tampilkan teks terdekripsi

        lanjut = input("Apakah ingin melanjutkan? (y/n): ")
        if lanjut.lower() != "y":
            print("Terima kasih, program telah keluar.")
            break

    elif pilih == "3":
        print("Terima kasih, program telah keluar.")
        break  # Keluar dari loop utama dan program selesai.

    else:
        print("[!] Pilihan tidak valid. Silakan masukkan pilihan yang sesuai.")
