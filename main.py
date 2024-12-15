# INFO SEPUTAR PROGRAM INI
# DISCLAIMER: Jangan judi pls

# Program ini merupakan program yang mensimulasikan mesin slot di dunia nyata
# Mesin slot diasumsikan sangat adil (tidak rigged, tidak bisa disetting)
# Di bawah ini merupakan kode yang dibuat untuk mensimulasikan mesin slot
# Kode ini merupakan kode utama dari 3 bagian kode (main.py , play.py , utils.py)
# Untuk mensimulasikan mesin slot, jalankan program dari kode ini ("python main.py")
# main.py merupakan program interface untuk kode ini
# Notes untuk yang memeriksa kode ini: Saya sebagai programmer dari kode ini juga tidak tahu bagian mana saja yang dirombak (karena program terlalu masif)
#                                      Program ini terlalu besar untuk ukuran projek seperti ini, cek github untuk mengeetahui perkembangan timeline kode ini
#                                      Program ini dibuat terlebih dahulu daripada psuedocode dan flowchartnya jadi seharusnya ada ketidaksinambungan


# IMPORT SEMUA BAHAN YANG DIBUTUHKAN
from utils import clear_terminal, enter_to_continue, kredit, update_kredit, tampilkan_kredit, nilai_kredit, update_animation, update_mode
from play import play
import sys


# PROGRAM UTAMA: looping menu
def main():
    while True:
        menu()


# Prosedur untuk melakukan mencetak tampilan menu dan menerima input user (menu yang dipilih)
def menu():
    # Print menu untuk ditampilkan ke user
    clear_terminal()
    print("SELAMAT DATANG DI MESIN SLOT GACORR PENGKOM WIN69")
    print()
    print("================================================")
    print("1. Menang atau Mati!")
    print("2. Masukkan Kredit")
    print("3. Tampilkan Kredit")
    print("4. Pengaturan")
    print("5. Cashout")
    print("6. Cara Bermain")
    print("7. Menyerah")
    print("================================================")
    print()

    # INPUT USER: menu yang ingin dipilih user
    pilihan = input("Masukkan pilihan anda: ")
    if pilihan == "1":
        play()
    elif pilihan == "2":
        input_kredit()
    elif pilihan == "3":
        clear_terminal()
        tampilkan_kredit()
        enter_to_continue()
    elif pilihan == "4":
        pengaturan()
    elif pilihan == "5":
        cashout()
    elif pilihan == "6":
        cara_bermain()
    elif pilihan == "7":
        quit()


# Pilihan menu untuk mengubah jumlah kredit user
def input_kredit():
    global kredit

    clear_terminal()
    
    # Pastikan user tidak memasukkan bilangan negatif
    uang = -1
    while uang < 0:
        uang = int(input("Berapa dollar yang ingin dimasukkan (masukkan 0 untuk kembali)? "))
    update_kredit(uang)


# Menu untuk user mengatur mode dan animasi saat bermain
def pengaturan():
    # basa-basi
    clear_terminal()
    print("PENGATURAN: ")
    print()
    print("1. Pilih mode")
    print("2. Animasi")
    print()
    
    # Input untuk pilihan pengaturan
    pilihan = input("Masukkan pilihan Anda (0 untuk kembali): ")
    
    # User ingin kembali ke menu (tidak usah lakukan apa-apa :D ), sbenarnya tidak perlu 0, cukup karakter lain selain 1 dan 2
    if pilihan == "0":
        pass
    
    # Pengaturan mode
    elif pilihan == "1":
        clear_terminal()
        print("Mode Permainan:  ")
        print("1. Baris tengah                  (5 koin)")
        print("2. Seluruh baris                 (10 koin)")
        print("3. Seluruh baris dan diagonal    (15 koin)")
        print()
        pil = int(input("Pilih mode yang anda inginkan (1/2/3): "))
        update_mode(pil)


    # Pengaturan animasi
    elif pilihan == "2":
        clear_terminal()
        pil = input("Masukkan mode animasi (ON/OFF): ").lower()

        if pil == "on":
            update_animation(True)
        elif pil == "off":
            update_animation(False)


# Pilihan menu untuk menampilkan cara bermain
def cara_bermain():
    clear_terminal()
    print(
        """Panduan Cara Bermain:

    1. Silakan mengisi saldo anda pada menu 'Masukkan koin'
    2. Silakan mengecek saldo anda pada menu 'Tampilkan kredit'
    3. Silakan memilih mode bermain pada menu 'Pengaturan' (mode default = 1)
    3. Silakan berjudi sepuas-puasnya pada menu 'Menang atau mati!', Yang Mahakuasa melihat kelakuan anda, bermainlah sesuai dengan kapasitas dosa anda 
    4. Jika anda cupu, silakan melakukan cashout di menu 'Cashout'
    5. Jika anda sudah bertaubat, silakan menyerah dengan memilih 'Menyerah'
    """
    )
    print()
    print("Mode Permainan:  ")
    print("    1. Baris tengah ")
    print("    2. Seluruh baris ")
    print("    3. Seluruh baris dan diagonal")
    print()
    print("KOMBINASI GACORRR: ")
    print("    🌟🌟🌟  💎💎💎  3000  kredit")
    print("    🌟🌟💎  🌟💎💎  90    kredit")
    print("    🍉🍉🍉  🍇🍇🍇  15    kredit")
    print("    🍓🍓    8 kredit")
    print("    🍓      4 kredit")
    print("    🔄🔄🔄          Spin lagi")
    print("    ⚡⚡⚡          Spin lagi, hadiah selanjutnya x2")
    print()
    print()
    print("""
          Selamat Berinvestasi
        "99% Penjudi menyerah sebelum kemenangan besarnya" - Waren Bopet Padang
          """)

    enter_to_continue()


# Menu untuk cashout (mengurangi kredit saja)
def cashout():
    global kredit

    # basa-basi
    clear_terminal()
    tampilkan_kredit()

    # Bagian input (pastikan user tidak input bilangan negatif)
    cash = -1
    while cash < 0:
        cash = int(input("Berapa nominal yang ingin anda cashout (0 untuk kembali)? "))           # Asumsikan user hanya input bilangan bulat
    
    # User ingin kembali (jangan lakukan apa-apa :D )
    if cash == 0:
        pass

    # Jika jumlah uang melebihi 
    elif cash > nilai_kredit():
        print("KREDIT TIDAK CUKUP")
        enter_to_continue()
    
    # Lainnya
    else: 
        update_kredit(-1 * cash)
        print(f"{cash} kredit berhasil dicairkan")
        enter_to_continue()


# Pilihan menu untuk keluar dari permainan
def quit():
    clear_terminal()
    print("Apakah anda yakin? (y/n)")
    print("99% orang berhenti sebelum menang besar")

    while True:    
        respone = input()
        if respone.lower() == "y" or respone.lower() == "yes":
            sys.exit("Sampai jumpa")
        elif respone.lower() == "n" or respone.lower() == "no":
            menu()


# bagian eksekusi kode (harus seperti ini agar fungsi lain tidak terpanggil)
if __name__ == "__main__":
    main()