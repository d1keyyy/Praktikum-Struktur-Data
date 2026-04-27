import time

# class lagu
class Lagu:
    def __init__(self, judul, penyanyi):
        self.judul = judul          
        self.penyanyi = penyanyi    
        self.next = None            

#singly linked list
class PlaylistMusik:
    def __init__(self):
        self.head = None  

    def tambah_lagu(self, judul, penyanyi):
        lagu_baru = Lagu(judul, penyanyi)

        if self.head is None:
            self.head = lagu_baru
            return

        lagu_saat_ini = self.head
        while lagu_saat_ini.next is not None:
            lagu_saat_ini = lagu_saat_ini.next
        
        lagu_saat_ini.next = lagu_baru

    def tampilkan_playlist(self):
        print("\n=== Daftar Lagu di Playlist Anda ===")
        lagu_saat_ini = self.head
        nomor = 1
        
        if lagu_saat_ini is None:
            print("Playlist kosong.")
            return

        while lagu_saat_ini is not None:
            print(f"{nomor}. {lagu_saat_ini.judul} - {lagu_saat_ini.penyanyi}")
            lagu_saat_ini = lagu_saat_ini.next
            nomor += 1
        print("====================================\n")

    def putar_semua(self):
        print("Memulai pemutaran playlist...")
        lagu_saat_ini = self.head

        while lagu_saat_ini is not None:
            print(f"Sedang memutar: {lagu_saat_ini.judul} oleh {lagu_saat_ini.penyanyi}")
            time.sleep(1.5) 
            
            lagu_saat_ini = lagu_saat_ini.next 
            
            if lagu_saat_ini is not None:
                print("Memuat lagu selanjutnya...\n")
        
        print("Playlist selesai diputar!")



my_playlist = PlaylistMusik()
def main():
    print("Selamat datang di aplikasi sportify")
    print("Silakan tambahkan lagu ke playlist Anda")
    my_playlist.tambah_lagu(input("Masukkan judul lagu: "), input("Masukkan nama penyanyi: "))
    print("Lagu berhasil ditambahkan ke playlist")
    print("Apakah Anda ingin menambahkan lagu lain? (y/n)")
    while True:
        pilihan = input().lower()
        if pilihan == 'y':
            my_playlist.tambah_lagu(input("Masukkan judul lagu: "), input("Masukkan nama penyanyi: "))
            print("Lagu berhasil ditambahkan ke playlist!")
            print("Apakah Anda ingin menambahkan lagu lain? (y/n)")
        elif pilihan == 'n':
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 'y' untuk ya atau 'n' untuk tidak.")

    my_playlist.tampilkan_playlist()

    my_playlist.putar_semua()


main()
