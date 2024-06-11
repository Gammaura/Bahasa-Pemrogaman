def Integer():
    
    a = input("\n=> MASUKKAN ANGKA : ")
        
    try:
        b = int(a)
        print("\nBENAR,",b,"ADALAH ANGKA!")
    
    except ValueError:
        print("\nSALAH,",a,"BUKANLAH ANGKA!")
        
    except Exception as e:
        print("TERJADI KESALAHAN PADA :",e)
    
    finally:
        print("\nTERIMAKASIH!")
        
def File():
    
    try:
        nama_file = input("\n=> MASUKKAN NAMA FILE : ")
        
        file = open(nama_file,"r")
        isi_file = file.read()
        print(isi_file)
        
    except FileNotFoundError:
        print("\nFILE",nama_file,"TIDAK DITEMUKAN")
        
    except IOError:
        print("\nTIDAK DAPAT MEMBACA FILE")
        
    except Exception as e:
        print("TERJADI KESALAHAN PADA :",e)

def Custom():
    
    class KingLance(Exception):
        pass

    while True:
    
        try:
            c = input("\nKETIK => AJI KING LANCE : ")    
            if c == "AJI KING LANCE":
                print("\nBENAR, AJI MEMANG KING LANCE")
                break
            
            else:    
                raise KingLance()
                
        except KingLance:
            print("\nKETIK AJI KING LANCE DULU DONG")
            
        except Exception as e:
            print("TERJADI KESALAHAN PADA :",e)

        finally:
            print("#AJI_LANCE_TERKUAT")

print("NIM  : 20230801274")
print("NAMA : ARDITYA ADJIE ROSANDI")
print("TUGAS PERTEMUAN 9")
print("\n1. INPUT INTEGER")
print("2. INPUT FILE")
print("3. INPUT EXCEPTION CUSTOM")

print("\n0. KELUAR")

while True:
    
    print("\n==||==||==||==||==||==||==")
    I = input("\nMASUKKAN PILIHAN : ")

    if I == "1":
        Integer()
        continue

    if I == "2":
        File()
        continue
    
    if I == "3":
        Custom()
        continue
    
    if I == "0":
        print("\nOKE MAKASIH...")
        break

    else:
        print("MASUKIN INPUT YANG BENER LAH")
        continue
