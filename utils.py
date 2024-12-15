# INFO SEPUTAR PROGRAM INI
# DISCLAIMER: Jangan judi pls

# Kode ini merupakan salah satu bagian dari tiga bagian program slot
# Bagian utils.py merupakan library yang tidak tersedia di tempat lain, jadi ya buat sendiri
# Di kode ini terdapat beberapa variabel global dan fungsi yang sering digunakan di main.py dan play.py


# VAR GLOBAL
# wheel slot
LEFT = [
    "🌟", "🍓", "🍉", "🔄", "⚡", "🍇", "💎", "🍇", "🍓", "⚡", "🔄", "🍉", "🌟", "⚡", "🍇", "🔄", "🍉", "💎", "⚡", "🍇", "🔄"
]

MIDDLE = [
    "🌟", "🍓", "🔄", "🍇", "🍉", "🍓", "🔄", "⚡", "⚡", "🍇", "💎", "🍇", "🔄", "🍓", "🍉", "🍇", "🔄", "🍓", "🍇", "🔄", "🍓"
    ]

RIGHT = [
    "🌟", "⚡", "💎", "🔄", "🍇", "🍉", "🔄", "🍇", "⚡", "🍉", "🔄", "🍇", "🍉", "⚡", "🔄", "🍇", "🍉", "⚡", "🔄", "🍇", "🍓"
]


# semua simbol yang berada di mesin slot
SYMBOL = ["🌟", "💎", "🍉", "🍇", "🍓", "🔄", "⚡"]
# panjang dari wheel slot
LEN = len(LEFT)


# mode dan animasi, untuk kepentingan animasi (bisa diperbarui dari kode lain)
MODE = 1
ANIMATION = True


# kredit (bisa diperbarui dari kode lain)
kredit = 0


# PROSEDUR/FUNGSI yang digunakan
# Prosuder untuk menghapus apapun yang ada di terminal
import os
def clear_terminal():
    # Untuk Windows
    if os.name == "nt":
        os.system("cls")
    else: # untuk linux, mac, dan lainnya
        os.system("clear")


# Prosedur yang memberi jeda ke user sampai menekan enter
def enter_to_continue():
    print()
    print("Tekan enter untuk melanjutkan")
    input()


# Fungsi untuk memperbarui jumlah kredit
def update_kredit(amount):
    global kredit
    kredit += amount


# Fungsi untuk menampilkan jumlah kredit
def tampilkan_kredit():
    global kredit
    print(f"Kredit anda saat ini adalah: {kredit}")


# Fungsi untuk mereturn nilai kredit, itu saja
def nilai_kredit():
    global kredit
    return kredit


# Fungsi untuk memperbarui nilai MODE
def update_mode(update):
    global MODE
    MODE = update


# Fungsi untuk mendapatkan nilai mode
def nilai_mode():
    global MODE
    return MODE


# Fungsi untuk memperbarui nilai ANIMATION
def update_animation(update):
    global ANIMATION
    ANIMATION = update


# Fungsi untuk mendapatkan nilai animation
def nilai_animation():
    global ANIMATION
    return ANIMATION