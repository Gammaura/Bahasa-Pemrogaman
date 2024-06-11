def MenuUtama():
        
    print("\n==||==||==||==||==||==||==")
        
    print("\n1. INPUT DATA MAHASISWA")
    print("2. INVENTARIS BARANG")
    print("3. PENGELOLAAN KEUANGAN PRIBADI")
    print("\n0. KELUAR")
    
def TambahBarang():
    NamaBarang = input("\nMASUKKAN NAMA BARANG : ")
    KodeBarang = input("MASUKKAN KODE BARANG : ")
    JumlahBarang = int(input("MASUKKAN JUMLAH BARANG : "))
    
    Barang = {"NAMA BARANG": NamaBarang, "KODE BARANG": KodeBarang, "JUMLAH": JumlahBarang}
    DataBarang.append(Barang)
    print("BARANG DENGAN KODE",KodeBarang,"BERHASIL DITAMBAHKAN")

def TampilkanBarang():
    if not DataBarang:
        print("\nBELUM ADA BARANG YANG DI INPUT")
    else:
        print("\nDAFTAR BARANG")
        for i, Barang in enumerate(DataBarang, start=1):
            print("\nNAMA BARANG : ",Barang['NAMA BARANG'])
            print("KODE BARANG : ",Barang['KODE BARANG'])
            print("JUMLAH      : ",Barang['JUMLAH'])

def CariBarang():
    Kode = input("\nMASUKKAN KODE BARANG : ")
    for Barang in DataBarang:
        if Barang['KODE BARANG'] == Kode:
            print("\nNAMA BARANG : ",Barang['NAMA BARANG'])
            print("KODE BARANG : ",Barang['KODE BARANG'])
            print("JUMLAH      : ",Barang['JUMLAH'])
            return
    print(f"\nBARANG DENGAN KODE {Kode} TIDAK DITEMUKAN")
    
def HapusBarang():
    Kode = input("\nMASUKKAN KODE BARANG : ")
    for Barang in DataBarang:
        if Barang['KODE BARANG'] == Kode:
            DataBarang.remove(Barang)
            print(f"BARANG DENGAN KODE {Kode} BERHASIL DIHAPUS")
            return
    print(f"\nBARANG DENGAN KODE {Kode} TIDAK DITEMUKAN")
    
def TambahTransaksi():
    Jenis = input("\nMASUKKAN JENIS TRANSAKSI (in/out) : ").lower()
    if Jenis not in ["in","out"]:
        print("SILAHKAN PILIH IN ATAU OUT")
        return

    Deskripsi = input("MASUKKAN DESKRIPSI : ")
    Jumlah = int(input("MASUKKAN JUMLAH : "))
    Transaksi.append({"JENIS TRANSAKSI": Jenis, "DESKRIPSI": Deskripsi, "JUMLAH": Jumlah})
    print(f"DATA TRANSAKSI '{Deskripsi}' BERHASIL DITAMBAHKAN")

def TampilkanTransaksi():
    if not Transaksi:
        print("\nBELUM ADA TRANSAKSI APAPUN")
    else:
        print("\nDAFTAR TRANSAKSI")
        for i, Trans in enumerate(Transaksi, start=1):
            print(f"{i}. {Trans['JENIS TRANSAKSI'].capitalize()}: {Trans['DESKRIPSI']} = {Trans['JUMLAH']}")
        print()

def TotalPemasukan():
    Total = sum(Trans['JUMLAH'] for Trans in Transaksi if Trans['JENIS TRANSAKSI'] == "in")
    print(f"\nTOTAL PEMASUKAN : {Total}")
    return Total

def TotalPengeluaran():
    Total = sum(Trans['JUMLAH'] for Trans in Transaksi if Trans['JENIS TRANSAKSI'] == "out")
    print(f"\nTOTAL PENGELUARAN : {Total}")
    return Total

def SaldoAkhir():
    Pemasukan = TotalPemasukan()
    Pengeluaran = TotalPengeluaran()
    Saldo = Pemasukan - Pengeluaran
    print(f"\nSALDO AKHIR : {Saldo}")
    return Saldo

print("NIM  : 20230801274")
print("NAMA : ARDITYA ADJIE ROSANDI")
print("TUGAS PERTEMUAN 9")

while True:
    MenuUtama()
    Menu = input("\nMASUKKAN PILIHAN : ")
    
    if Menu == "1":
                
        DataMahasiswa = []
        JumlahNilai = 0
        Tertinggi = 0
        Terendah = 100
                
        print("\n==||==||==||==||==||==||==")
                
        n = int(input("\nMASUKKAN JUMLAH MAHASISWA : "))
                
        for i in range(n):
            print("\nMASUKKAN DATA MAHASISWA",(i+1))
            Nama = input("MASUKKAN NAMA  : ")
            NIM = input("MASUKKAN NIM   : ")
            Nilai = int(input("MASUKKAN NILAI : "))
                    
            Mahasiswa = {
            "NAMA" : Nama,
            "NIM" : NIM,
            "NILAI" : Nilai
            }
                    
            DataMahasiswa.append(Mahasiswa)
                
        for i, Mahasiswa in enumerate(DataMahasiswa):
            print("NAMA  : ",Mahasiswa["NAMA"])
            print("NIM   : ",Mahasiswa["NIM"])
            print("NILAI : ",Mahasiswa["NILAI"])
                    
            JumlahNilai += Mahasiswa["NILAI"]
                    
            if Tertinggi < Mahasiswa["NILAI"]:
                Tertinggi = Mahasiswa["NILAI"]
                        
            if Terendah > Mahasiswa["NILAI"]:
                Terendah = Mahasiswa["NILAI"]
                    
        RataRata = JumlahNilai / n
        print("\n=> NILAI RATA RATA =", RataRata)
        print("\n=> NILAI TERTINGGI =", Tertinggi)
        print("\n=> NILAI TERENDAH =", Terendah)
                
        continue

    if Menu == "2":
        
        DataBarang = []

        while True:
            
            print("\n==||==||==||==||==||==||==")
            
            print("\n1. TAMBAH BARANG")
            print("2. TAMPILKAN BARANG")
            print("3. CARI BARANG")
            print("4. HAPUS BARANG")
            print("\n0. KEMBALI")
        
            Pilihan = input("\nMASUKKAN PILIHAN : ")
        
            if Pilihan == '1':
                print("\n==||==||==||==||==||==||==")
                TambahBarang()
                continue
            
            if Pilihan == '2':
                print("\n==||==||==||==||==||==||==")
                TampilkanBarang()
                continue
            
            if Pilihan == '3':
                print("\n==||==||==||==||==||==||==")
                CariBarang()
                continue
            
            if Pilihan == '4':
                print("\n==||==||==||==||==||==||==")
                HapusBarang()
                continue
            
            if Pilihan == '0':
                break
        
            else:
                continue
    
    if Menu == "3":
        
        Transaksi = []
    
        while True:
        
            print("\n==||==||==||==||==||==||==")
       
            print("\n1. TAMBAH TRANSAKSI")
            print("2. TAMPILKAN TRANSAKSI")
            print("3. HITUNG PEMASUKAN")
            print("4. HITUNG PENGELUARAN")
            print("5. HITUNG SALDO AKHIR")
            print("\n0. KEMBALI")
        
            Pilihan = input("\n1MASUKKAN PILIHAN : ")
        
            if Pilihan == '1':
                print("\n==||==||==||==||==||==||==")
                TambahTransaksi()
                continue
            
            if Pilihan == '2':
                print("\n==||==||==||==||==||==||==")
                TampilkanTransaksi()
                continue
            
            if Pilihan == '3':
                print("\n==||==||==||==||==||==||==")
                TotalPemasukan()
                continue
            
            if Pilihan == '4':
                print("\n==||==||==||==||==||==||==")
                TotalPengeluaran()
                continue
            
            if Pilihan == '5':
                print("\n==||==||==||==||==||==||==")
                SaldoAkhir()
                continue
            
            if Pilihan == '0':
                break
        
            else:
                continue
    
    if Menu == "0":
        break

    else:
        continue
