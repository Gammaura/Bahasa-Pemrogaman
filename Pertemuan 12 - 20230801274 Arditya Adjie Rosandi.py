def Menu():
    print("\n==||==||==||==||==||==||==")
    print("\n1. TAMPILKAN DAFTAR BUKU")
    print("2. CARI BUKU")
    print("3. TAMBAHKAN BUKU")
    print("4. HAPUS BUKU")
    print("\n0. KELUAR")

def TambahBuku():
    print("\n==||==||==||==||==||==||==")
    n = int(input("\nMASUKKAN JUMLAH JUDUL BUKU : "))
    print("\n==||==||==||==||==||==||==")
    
    for i in range(n):
        print("\n=> BUKU", (i + 1))
        N = input("MASUKKAN JUDUL BUKU  : ").strip()
        K = input("MASUKKAN KODE BUKU   : ").strip()
        P = input("MASUKKAN PENULIS     : ").strip()
        J = int(input("MASUKKAN JUMLAH BUKU : "))
        
        Buku = {
            "JUDUL BUKU": N,
            "KODE BUKU": K,
            "PENULIS BUKU": P,
            "JUMLAH": J
        }
        DataBuku.append(Buku)
        print("\nBUKU BERHASIL DITAMBAHKAN!")

def TampilkanBuku():
    print("\n==||==||==||==||==||==||==")
    if not DataBuku:
        print("\nBELUM ADA BUKU YANG TERSEDIA")
    else:
        print("\nDAFTAR BUKU TOKO GAMMAURA")
        for i, Buku in enumerate(DataBuku, start=1):
            print("\nNOMOR BUKU :",i)
            print(f"JUDUL BUKU : {Buku['JUDUL BUKU']}")
            print(f"KODE       : {Buku['KODE BUKU']}")
            print(f"PENULIS    : {Buku['PENULIS BUKU']}")
            print(f"JUMLAH     : {Buku['JUMLAH']}")

def CariBuku():
    print("\n==||==||==||==||==||==||==")
    kata = input("\nMASUKKAN JUDUL / KODE / PENULIS : ").strip()
    
    if not kata:
        print("\nSILAHKAN MASUKKAN INPUT APAPUN")
        return
    
    ditemukan = False
    for Buku in DataBuku:
        
        if kata.lower() in map(str.lower, Buku['JUDUL BUKU'].split()) or kata.lower() in map(str.lower, Buku['KODE BUKU'].split()) or kata.lower() in map(str.lower, Buku['PENULIS BUKU'].split()):
            print(f"\nJUDUL BUKU : {Buku['JUDUL BUKU']}")
            print(f"KODE       : {Buku['KODE BUKU']}")
            print(f"PENULLIS   : {Buku['PENULIS BUKU']}")
            print(f"JUMLAH     : {Buku['JUMLAH']}")
            ditemukan = True
            
    if not ditemukan:
        print("\nBUKU TIDAK DITEMUKAN / BELUM TERSEDIA")

def HapusBuku():
    print("\n==||==||==||==||==||==||==")
    Kode = input("\nMASUKKAN JUDUL / KODE BUKU: ").strip()
    for Buku in DataBuku:
        if Buku['KODE BUKU'] == Kode or Buku['JUDUL BUKU'] == Kode:
            DataBuku.remove(Buku)
            print("\nBUKU BERHASIL DIHAPUS")
            return
    print("\nBUKU TIDAK DITEMUKAN")

print("NIM  : 20230801274")
print("NAMA : ARDITYA ADJIE ROSANDI")
print("TUGAS PERTEMUAN 10 (SEARCHING ALGORITHM)")

DataBuku = [
    {
        "JUDUL BUKU": "BUMI MANUSIA",
        "KODE BUKU": "B101",
        "PENULIS BUKU": "PRAMOEDYA ANANTA TOER",
        "JUMLAH": 30
    },
    {
        "JUDUL BUKU": "JEJAK LANGKAH",
        "KODE BUKU": "B102",
        "PENULIS BUKU": "PRAMOEDYA ANANTA TOER",
        "JUMLAH": 31
    },
    {
        "JUDUL BUKU": "ANAK SEMUA BANGSA",
        "KODE BUKU": "B103",
        "PENULIS BUKU": "PRAMOEDYA ANANTA TOER",
        "JUMLAH": 32
    },
    {
        "JUDUL BUKU": "LAUT BERCERITA",
        "KODE BUKU": "B104",
        "PENULIS BUKU": "LEILA SALIKHA CHUDORI",
        "JUMLAH": 36
    },
    {
        "JUDUL BUKU": "PULANG: SEBUAH NOVEL",
        "KODE BUKU": "B105",
        "PENULIS BUKU": "LEILA SALIKHA CHUDORI",
        "JUMLAH": 30
    },
    {
        "JUDUL BUKU": "9 DARI NADIRA",
        "KODE BUKU": "B106",
        "PENULIS BUKU": "LEILA SALIKHA CHUDORI",
        "JUMLAH": 34
    },
    {
        "JUDUL BUKU": "LASKAR PELANGI",
        "KODE BUKU": "B107",
        "PENULIS BUKU": "ANDREA HIRATA",
        "JUMLAH": 32
    },
    {
        "JUDUL BUKU": "SANG PEMIMPI",
        "KODE BUKU": "B108",
        "PENULIS BUKU": "ANDREA HIRATA",
        "JUMLAH": 36
    },
    {
        "JUDUL BUKU": "NEGERI 5 MENARA",
        "KODE BUKU": "B109",
        "PENULIS BUKU": "AHMAD FUADI",
        "JUMLAH": 30
    },
    {
        "JUDUL BUKU": "RUMAH KACA",
        "KODE BUKU": "B110",
        "PENULIS BUKU": "PRAMOEDYA ANANTA TOER",
        "JUMLAH": 34
    },
    {
        "JUDUL BUKU": "PERAHU KERTAS",
        "KODE BUKU": "B111",
        "PENULIS BUKU": "DEWI LESTARI",
        "JUMLAH": 32
    },
    {
        "JUDUL BUKU": "CANTIK ITU LUKA",
        "KODE BUKU": "B112",
        "PENULIS BUKU": "EKA KURNIAWAN",
        "JUMLAH": 36
    },
    {
        "JUDUL BUKU": "FILOSOFI TERAS",
        "KODE BUKU": "B113",
        "PENULIS BUKU": "HENRY MANAMPIRING",
        "JUMLAH": 30
    },
    {
        "JUDUL BUKU": "CINTA BRONTOSAURUS",
        "KODE BUKU": "B114",
        "PENULIS BUKU": "RADITYA DIKA",
        "JUMLAH": 34
    },
    {
        "JUDUL BUKU": "MANUSIA SETENGAH SALMON",
        "KODE BUKU": "B115",
        "PENULIS BUKU": "RADITYA DIKA",
        "JUMLAH": 32
    }
]

while True:
    Menu()
    Pilihan = input("\nMASUKKAN PILIHAN : ").strip()
    
    if Pilihan == "1":
        TampilkanBuku()
        
    elif Pilihan == "2":
        CariBuku()
        
    elif Pilihan == "3":
        TambahBuku()
        
    elif Pilihan == "4":
        HapusBuku()
        
    elif Pilihan == "0":
        break
    else:
        print("\nSILAHKAN MASUKKAN INPUT YANG TERSEDIA")