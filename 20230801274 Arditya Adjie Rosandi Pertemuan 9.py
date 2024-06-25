def MenuUtama():
        
    print("\n==||==||==||==||==||==||==")
        
    print("\n1. (SEQUENCIAL) TOKO BUKU GAMMAURA")
    print("2. (BINARY) NOMOR ANTRIAN PASIEN")
    print("3. INPUT BINARY")
    print("\n0. KELUAR")

def MenuLanjutan():
    
    print("\n==||==||==||==||==||==||==")
        
    print("\n1. TAMPILKAN DAFTAR BUKU")
    print("2. CARI BUKU")
    print("3. TAMBAHKAN BUKU")
    print("4. HAPUS BUKU")
    print("\n0. KELUAR")
    
def MenuLanjutan1():
    
    print("\n==||==||==||==||==||==||==")
        
    print("\n1. TAMPILKAN DAFTAR PASIEN")
    print("2. URUTKAN PASIEN")
    print("3. TAMBAHKAN PASIEN")
    print("4. CARI NOMOR PASIEN")
    print("\n0. KELUAR")
    
def TambahBuku():
    
    print("\n==||==||==||==||==||==||==")
    
    n = int(input("\nMASUKKAN JUMLAH JUDUL BUKU : "))
    
    print("\n==||==||==||==||==||==||==")
                
    for i in range(n):
        print("\n=> BUKU",(i+1))
        N = input("MASUKKAN JUDUL BUKU  : ")
        K = input("MASUKKAN KODE BUKU   : ")
        J = int(input("MASUKKAN JUMLAH BUKU : "))
                    
        Buku = {
            "JUDUL BUKU" : N,
            "KODE BUKU" : K,
            "JUMLAH" : J
        }
                    
        DataBuku.append(Buku)

def TampilkanBuku():
    if not DataBuku:
        
        print("\n==||==||==||==||==||==||==")
        
        print("\nBELUM ADA BUKU YANG TERSEDIA")
        
    else:
        
        print("\n==||==||==||==||==||==||==")
        
        print("\nDAFTAR BUKU TOKO GAMMAURA")
        for i, Buku in enumerate(DataBuku, start=1):
            print("\nNOMOR BUKU : ",i)
            print("JUDUL BUKU : ",Buku['JUDUL BUKU'])
            print("KODE       : ",Buku['KODE BUKU'])
            print("JUMLAH     : ",Buku['JUMLAH'])

def CariBuku():
    
    print("\n==||==||==||==||==||==||==")
    
    Kode = input("\nMASUKKAN JUDUL / KODE BUKU : ")
    
    for Buku in DataBuku:
        if Buku['KODE BUKU'] == Kode or Buku['JUDUL BUKU'] == Kode:
            print("\nJUDUL BUKU : ",Buku['JUDUL BUKU'])
            print("KODE       : ",Buku['KODE BUKU'])
            print("JUMLAH     : ",Buku['JUMLAH'])
            return
        
    print("\nBUKU TIDAK DITEMUKAN")
    
def HapusBuku():
    
    print("\n==||==||==||==||==||==||==")
    
    Kode = input("\nMASUKKAN NAMA / KODE BUKU : ")
    for Buku in DataBuku:
        if Buku['KODE BUKU'] == Kode or Buku['JUDUL BUKU'] == Kode:
            DataBuku.remove(Buku)
            print("\nBUKU BERHASIL DIHAPUS")
            return
    print("\nBUKU TIDAK DITEMUKAN")

def TampilkanPasien():
    if not DataPasien:
        
        print("\n==||==||==||==||==||==||==")
        
        print("\nBELUM ADA PASIEN YANG TERDAFTAR")
        
    else:
        
        print("\n==||==||==||==||==||==||==")
        
        print("\nDAFTAR PASIEN RUMAH SAKIT GAMMAURA")
        for i, Pasien in enumerate(DataPasien, start=1):
            print("\nNAMA PASIEN   : ",Pasien['NAMA PASIEN'])
            print("NOMOR ANTRIAN : ",Pasien['NOMOR ANTRIAN'])
            
            
def TambahPasien():
    
    print("\n==||==||==||==||==||==||==")
    
    m = int(input("\nMASUKKAN JUMLAH PASIEN : "))
    
    print("\n==||==||==||==||==||==||==")
                
    for i in range(m):
        print("\n=> PASIEN",(i+1))
        P = input("NAMA PASIEN   : ")
        A = input("NOMOR ANTRIAN : ")
                    
        Pasien = {
            "NAMA PASIEN" : P,
            "NOMOR ANTRIAN" : A,
        }
                    
        DataPasien.append(Pasien)

def UrutanPasien():
    if not DataPasien:
        print("\n==||==||==||==||==||==||==")
        print("\nBELUM ADA PASIEN YANG TERDAFTAR")
    else:
        print("\n==||==||==||==||==||==||==")
        Urutan = sorted(DataPasien, key=lambda x: x['NOMOR ANTRIAN'])
        print("\nDAFTAR URUTAN ANTRIAN RUMAH SAKIT GAMMAURA")
        for Pasien in Urutan:
            print("\nNAMA PASIEN   : ", Pasien['NAMA PASIEN'])
            print("NOMOR ANTRIAN : ", Pasien['NOMOR ANTRIAN'])
            
def CariUrutan():
    
    if not DataPasien:
        print("\n==||==||==||==||==||==||==")
        print("NOMOR ANTRIAN TIDAK DITEMUKAN")
        
    else:
        print("\n==||==||==||==||==||==||==")
        Cari = input("MASUKKAN NOMOR ANTRIAN : ")
        Urutan = sorted(DataPasien, key=lambda x: x['NOMOR ANTRIAN'])
        
        found = False
        for i, Pasien in enumerate(Urutan, start=1):
            if Pasien['NOMOR ANTRIAN'] == Cari:
                print("NOMOR ANTRIAN",Cari,"DITEMUKAN PADA URUTAN KE",i)
                found = True
                break
        
        if not found:
            print("\nNOMOR ANTRIAN TIDAK DITEMUKAN")
            
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

print("NIM  : 20230801274")
print("NAMA : ARDITYA ADJIE ROSANDI")
print("TUGAS PERTEMUAN 9 (SEARCHING ALGORITHM)")

DataBuku = []

Buku = {
    "JUDUL BUKU" : "BUMI MANUSIA",
    "KODE BUKU" : "B101",
    "JUMLAH" : 34
}
                    
DataBuku.append(Buku)

Buku = {
    "JUDUL BUKU" : "LASKAR PELANGI",
    "KODE BUKU" : "B102",
    "JUMLAH" : 32
}
                    
DataBuku.append(Buku)

Buku = {
    "JUDUL BUKU" : "LAUT BERCERITA",
    "KODE BUKU" : "B103",
    "JUMLAH" : 36
}
                    
DataBuku.append(Buku)

DataPasien = []

while True:
    MenuUtama()
    Menu = input("\nMASUKKAN PILIHAN : ")
    
    if Menu == "1":
        
        while True:
        
            MenuLanjutan()
        
            Pilihan = input("\nMASUKKAN PILIHAN : ")
        
            if Pilihan == "1":
            
                TampilkanBuku()
            
            if Pilihan == "2":
            
                CariBuku()
            
            if Pilihan == "3":
            
                TambahBuku()
                
            if Pilihan == "4":
            
                HapusBuku()
            
            if Pilihan == "0":
            
                break
            
            else:
                continue

    if Menu == "2":
        
        while True:
            
            MenuLanjutan1()
            
            Pilihan = input("\nMASUKKAN PILIHAN : ")
        
            if Pilihan == '1':
                
                TampilkanPasien()
            
            if Pilihan == '2':
                
                UrutanPasien()
            
            if Pilihan == '3':
                
                TambahPasien()
                
            if Pilihan == '4':
                
                CariUrutan()
            
            if Pilihan == '0':
                break
        
            else:
                continue
    
    if Menu == "3":
        
        print("\n==||==||==||==||==||==||==")
        
        arr = list(map(int, input("\nMASUKKAN DAFTAR ELEMEN YANG SUDAH TERURUT DENGAN SPASI : ").split()))

        x = int(input("MASUKKAN ELEMEN YANG INGIN DICARI: "))

        Hasil = binary_search(arr, x)

        if Hasil != -1:
            print("ELEMEN DITEMUKAN PADA INDEKS KE",Hasil)
        else:
            print("ELEMEN TIDAK DITEMUKAN")
           
    if Menu == "0":
        break

    else:
        continue