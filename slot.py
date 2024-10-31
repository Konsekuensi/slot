from utils import clear_terminal, enter_to_continue, kredit, update_kredit, tampilkan_kredit, nilai_kredit
from play import play
import sys


def main():
    while True:
        menu()


def menu():
    clear_terminal()
    print("SELAMAT DATANG DI MESIN SLOT GACORR PENGKOM WIN69")
    print("================================================")
    print("1. Memasukkan koin")
    print("2. Tampilkan kredit")
    print("3. Menang atau mati!")
    print("4. Cashout")
    print("5. Kombinasi")
    print("6. Menyerah")

    pilihan = input("Masukkan pilihan anda: ")

    if pilihan == "1":
        input_kredit()
    elif pilihan == "2":
        clear_terminal()
        tampilkan_kredit()
        enter_to_continue()
    elif pilihan == "3":
        play()
    elif pilihan == "4":
        cashout()
    elif pilihan == "5":
        kombinasi()
    elif pilihan == "6":
        quit()


def input_kredit():
    global kredit

    clear_terminal()
    uang = int(input("Berapa dollar yang ingin dimasukkan (masukkan 0 untuk kembali)? "))       # Asumsikan user memasukkan bilangan bulat positif
    update_kredit(uang)
    

def kombinasi():
    clear_terminal()
    print("Mode Permainan:  ")
    print("1. Baris tengah ")
    print("2. Seluruh baris ")
    print("3. Seluruh baris dan diagonal")
    print()
    print("KOMBINASI GACORRR: ")
    print("🌟🌟🌟  💎💎💎  300 kredit")
    print("🌟🌟💎  🌟💎💎  90 kredit")
    print("🍉🍉🍉  🍇🍇🍇  15 kredit")
    print("🍓🍓    8 kredit")
    print("🍓      4 kredit")
    print("🔄🔄🔄          Spin lagi")
    print("⚡⚡⚡          Spin lagi, hadiah selanjutnya x2")
    print()

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