print("SELAMAT DATANG DI AGEN TIKET BUS ANTAR KOTA ANTON KECE SOLO")
print("kode tiket | tujuan | harga tiket | durasi")
print("------------------------------------------")
print("10         | SBY    | Rp. 100.000 | 2 jam ")
print("11         | JKT    | Rp. 150.000 | 3 jam ")
print("12         | MLG    | Rp. 200.000 | 4 jam ")
print("13         | MKS    | Rp. 250.000 | 5 jam ")
print("14         | BKS    | Rp. 300.000 | 6 jam ")
print("15         | MDN    | Rp. 350.000 | 7 jam ")
print("----------------------------------")
print("")
print("silahkan isi biodata anda (abaikan jika tidak memesan/ketik = jika ada yang salah)")
nama = input("Masukkan namamu: ")
nomor = input("Masukkan Nomor Handphone: ")
kodetiket = input("Masukkan kode tiket busmu: ")
tujuan = []
harga = []
if kodetiket == "10":
    tujuan.append("SURABAYA")
    harga = 100000
elif kodetiket == "11":
    tujuan.append("JAKARTA")
    harga = 150000
elif kodetiket == "12":
    tujuan.append("MALANG")
    harga = 200000
elif kodetiket == "13":
    tujuan.append("MAKASSAR")
    harga = 250000
elif kodetiket == "14":
    tujuan.append("BEKASI")
    harga = 300000
elif kodetiket == "15":
    tujuan.append("MEDAN")
    harga = 350000
else:
    tujuan.append("kodemu salah silahkan coba lagi")

jumlah = int(input("Mau beli berapa tiket?: "))
print()
if jumlah ==2:
    diskon = (jumlah+harga)*0.2
elif jumlah ==3:
    diskon = (jumlah+harga)*0.3
elif jumlah == 4:
    diskon = (jumlah+harga)*0.4
elif jumlah >=5:
    diskon = (jumlah+harga)*0.5
else:
    diskon =0

total = int(jumlah*harga-diskon)
pajak = total*0.05
jumlahbayar = total + pajak
def garis():
    print("-----------------------------------------")
garis()
print("Terima kasih sudah mengkonfirmasi")
garis()
print("Mohon dicek kembali")
garis()
print("Nama pembeli: ", nama)
print("Nomor Handphone: ",nomor)
print("Kode tiket yang akan dibeli: ",kodetiket)
print("Kota yang akan dituju: ", tujuan)
print("tiket yang akan dibeli: ",jumlah)
garis()
print("harga tiket: Rp.", harga)
print("Diskon     : Rp.", diskon)
print("PPN 10%    : ", pajak)
garis()
print("Pembayaran sebagai berikut")
print("Total Bayar : Rp.", jumlahbayar)
garis()
print("")
print("kelas express memungkinkan anda untuk datang di tujuan lebih cepat dari sebelumnya, fasilitas lebih baik dari ekonomi, akan tetapi akan menambah biaya sebesar Rp.100.000")
express = input(str("apakah anda ingin menggunakan kelas express? (y/n)"))
if express == "y":
    uangexpress = 100000
    x = jumlahbayar + uangexpress
    print("jumlah total yang harus dibayar sekarang: ", x)
    a = input(str("apakah pesanan sudah sesuai? (y/n)"))
    if a == "y":
        uang = int(input("Masukkan pembayaranmu: Rp."))
        garis()
        kembalian = uang - x
        print("uang kembalianmu : Rp.", kembalian)
        garis()
        print("TERIMA KASIH SUDAH MENGGUNAKAN PELAYANAN KAMI")
        print("THANKS FOR USING OUR SERVICE!!!!")
        garis()
    elif a == "n":
        print("Silahkan masukkan lagi data diri anda dengan benar")
        garis()
    else:
        print("error")
    

elif express == "n":
    print("terima kasih atas konfirmasinya")
    a = input(str("apakah pesanan sudah sesuai? (y/n)"))
    garis()
    uang = int(input("Masukkan pembayaranmu: Rp."))
    kembalian = uang - jumlahbayar
    print("uang kembalianmu : Rp.", kembalian)
    garis()
    print("TERIMA KASIH SUDAH MENGGUNAKAN PELAYANAN KAMI")
    print("THANKS FOR USING OUR SERVICE!!!!")
    garis()
else:
    ("error")