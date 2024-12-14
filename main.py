from utils import clear_terminal, enter_to_continue, kredit, update_kredit, tampilkan_kredit, nilai_kredit
from play import play, pengaturan
import sys

def main():
    while True:
        menu()


def menu():
    clear_terminal()
    print("SELAMAT DATANG DI MESIN SLOT GACORR PENGKOM WIN69")
    print("================================================")
    print("1. Menang atau Mati!")
    print("2. Masukkan Kredit")
    print("3. Tampilkan Kredit")
    print("4. Pengaturan")
    print("5. Cashout")
    print("6. Cara Bermain")
    print("7. Menyerah")

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


def input_kredit():
    global kredit

    clear_terminal()
    uang = int(input("Berapa dollar yang ingin dimasukkan (masukkan 0 untuk kembali)? "))       # Asumsikan user memasukkan bilangan bulat positif
    update_kredit(uang)
    

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


def cashout():
    global kredit

    clear_terminal()
    tampilkan_kredit()
    cash = int(input("Berapa nominal yang ingin anda cashout? "))           # Asumsikan user hanya input bilangan bulat
    if cash > nilai_kredit():
        print("KREDIT TIDAK CUKUP")
        enter_to_continue()
    else: 
        update_kredit(-1 * cash)
        print(f"{cash} kredit berhasil dicairkan")
        enter_to_continue()


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


if __name__ == "__main__":
    main()