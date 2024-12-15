# INFO SEPUTAR PROGRAM INI
# DISCLAIMER: Jangan judi pls

# Ini merupakan play.py, salah satu kode yang digunakan di program mesin slot ini
# play.py merupakan menu permainan yang dipanggil dari main.py
# Karena kodenya masyaallah panjang sekali, jadinya dibuat kode terpisah saja biar rapi
# Kode ini berisikan logic bagaimana mesin slot bekerja


# Import benda-benda yang dibutuhkan
from utils import LEN, LEFT, MIDDLE, RIGHT, clear_terminal, update_kredit, nilai_kredit, nilai_animation, nilai_mode
import random as rn
import time


# INISIASI hadiah di sini nanti akan diupdate seiring fungsi berjalan
HADIAH = [0, 0, 1]          # 0: kredit, 1: freespin, 2: multiplier
FREESPIN = 0
MULTIPLIER = 1      # FREESPIN dan MULTIPLIER merupakan variabel sementara di sini


# Fungsi utama yang nantinya dipanggil oleh main.py
def play():
    # Inisiasi variabel HADIAH global
    global HADIAH

    # Dapatkan nilai MODE dan nilai ANIMATION
    MODE = nilai_mode()
    ANIMATION = nilai_animation()

    # Display kosongan
    display = [
        ["❔", "❔", "❔"],
        ["❔", "❔", "❔"],
        ["❔", "❔", "❔"]
    ]

    # Print tampilan awal
    clear_terminal()
    kred = nilai_kredit()
    print_display(display, False, "")

    # Tanya user ingin main atau tidak?
    ans = input("Tekan Enter untuk Spin (ketik 0 untuk kembali) ")
    if ans == "0":
        return 0
    
    # Loop ketika bermain (berhenti jika kredit habis atau user ingin berhenti)
    while kred > 0:
        # Cek berkala nilai kred untuk menghentikan permainan
        kred = nilai_kredit()
        
        # Acak display dan tentukan hadiah yang dimenangkan user
        display = spin()
        reward(MODE, display)
        pesan = bet(MODE)
        
        # Tampilkan display ke user
        clear_terminal()
        print_display(display, ANIMATION, pesan)

        # Hentikan permainan jika user kehabisan kredit
        if kred <= 0:
            break

        # Ajukan pertanyaan apakah user ingin main lagi atau keluat
        ans = input("Tekan Enter untuk Spin (ketik 0 untuk kembali) ")

        # Keluar dari permainan
        if ans == "0":      
            break


# Fungsi untuk mengocok/memutar wheel
def spin():
    # Pilih salah satu pivot di setiap wheel
    pivot_kiri = rn.randint(0, LEN - 1)
    pivot_tengah = rn.randint(0, LEN - 1)
    pivot_kanan = rn.randint(0, LEN - 1)

    # Pilih tetangga pivot 1 ke atas untuk baris atas dan 1 ke bawah untuk baris bawah, dan pilih pivotnya itu sendiri untuk baris tengah
    atas = [LEFT[pivot_kiri - 1], MIDDLE[pivot_tengah - 1], RIGHT[pivot_kanan - 1]]
    tengah = [LEFT[pivot_kiri], MIDDLE[pivot_tengah], RIGHT[pivot_kanan]]
    bawah = [LEFT[(pivot_kiri + 1) % LEN], MIDDLE[(pivot_tengah + 1) % LEN], RIGHT[(pivot_kanan + 1) % LEN]]

    # Return matrix 3x3 dengan isi wheel yang telah diacak
    return [atas, tengah, bawah]


# Algoritma yang menambahkan kredit yang didapatkan user dan/atau mengurangi kredit user sesuai dengan ketentuan (akan return pesan)
def bet(mode):
    # Inisiasi variabel global yang akan di-update
    global HADIAH, FREESPIN, MULTIPLIER

    # Mengurangi kredit user
    # Jika terdapat freespin (Tidak usah bayar kredit)
    if FREESPIN > 0:            
        FREESPIN -= 1
        HADIAH[1] = FREESPIN
    
    # Tidak ada freespin berarti harus bayar menggunakan kredit 
    else:
        update_kredit(-5 * mode)

    
    # Melakukan update pada kredit user 
    update_kredit(HADIAH[0] * MULTIPLIER)
    
    # Pesan jika menang hadiah (Jika tidak dapat, hanya ada empty string)
    pesan = ""
    if HADIAH[0] * MULTIPLIER != 0:
        pesan = f"Selamat Anda mendapatkan {HADIAH[0] * MULTIPLIER} kredit!"
    
    # Update nilai multiplier menjadi default jika digunakan
    if MULTIPLIER != 1: 
        MULTIPLIER = 1
        HADIAH[2] = MULTIPLIER

    # Kembalikan nilai ke nilai yang semestinya
    HADIAH[0] = 0
    FREESPIN, MULTIPLIER = HADIAH[1], HADIAH[2]

    # Return pesan yang didapatkan di atas
    return pesan
    

# Algoritma untuk menentukan hadiah yang diperoleh oleh user, hadiah nantinya akan diupdate di varaibel global sesuai dengan mode
def reward(mode, display): 
    
    # Fungsi untuk membandingkan display dengan hadiah yang dapat diperoleh
    def compare(comp): # return hadiah
        freq = {
            "🌟": 0, "💎": 0, "🍉": 0, "🍇": 0, "🍓": 0, "🔄": 0, "⚡": 0
        }
        
        # Jika terdapat simbol yang yang sama, masukkan sesuai index
        for symbol in comp:
            freq[symbol] += 1
        
        # Bandingkan dengan list reward (kredit, reroll, atau reroll+)
        if freq["🌟"] == 3 or freq["💎"] == 3:
            return 3000
        elif (freq["🌟"] == 2 and freq["💎"] == 1) or (freq["💎"] == 2 and freq["🌟"] == 1): 
            return 90
        elif freq["🍉"] == 3 or freq["🍇"] == 3:
            return 15
        elif freq["🍓"] == 2 or freq["🍓"] == 3:
            return 8
        elif freq["🍓"] == 1:
            return 4
        elif freq["🔄"] == 3:
            return "REROLL"
        elif freq["⚡"] == 3:
            return "REROLL+"
        else:
            return 0
    

    # Inisiasi variabel globla
    global HADIAH

    # Pecah matrix display ke 3 variabel berbeda
    rows = [display[0], display[1], display[2]]
    diag1 = [display[0][0], display[1][1], display[2][2]]
    diag2 = [display[0][2], display[1][1], display[2][0]]
    
    # Fungsi untuk memperbarui hadiah sesuai dengan hadiah yang didapatakan
    def update(h):
        if h == "REROLL":
            HADIAH[1] += 1
        elif h == "REROLL+":
            HADIAH[1] += 1
            HADIAH[2] *= 2
        else:
            HADIAH[0] += h

    # Cek mode 1 (display[1] saja / horizontal tengah)
    if mode == 1:
        h = compare(display[1])
        update(h)
        
    # Cek mode 2 dan mode 3
    else:                
        # Cek semua baris 
        for row in rows:        
            h = compare(row)
            update(h)

        # Mode 3 only, mode 2 tidak sampai ke sini
        if mode == 3:           
            h = compare(diag1)
            update(h)
            h = compare(diag2)
            update(h)


# Fungsi untuk melakukan print display (juga animasinya jika animation=True) TODO
def print_display(display, animation, pesan=""):
    # Matrix berisikan tanda tanya, untuk kepentingan animation
    mystery = [
            ["❔", "❔", "❔"],
            ["❔", "❔", "❔"],
            ["❔", "❔", "❔"]
        ]

    # Prosedur untuk print display seperti biasa
    def regular_display_print(display):
        print()
        print("================================================")
        print()
        for baris in display:
            print(end="                 ")
            for kolom in baris:
                print(kolom, end=" ")
            print()
        print()
        print("================================================")
        print()

    # Fungsi yang mengganti suatu baris n dari matrix A menjadi suatu baris matrix B (matrixnya pasti 3x3)
    def replace_baris(n, matrix_A, matrix_B):
        new_display = matrix_A.copy()
        new_display[0][n - 1] = matrix_B[0][n - 1]
        new_display[1][n - 1] = matrix_B[1][n - 1]
        new_display[2][n - 1] = matrix_B[2][n - 1]
        return new_display


    # Jika animation dinyalakan
    if animation:
        # print misteri dulu
        print("Kredit anda: ???")
        print()
        regular_display_print(mystery)
        time.sleep(1)
        
        # Ganti baris misteri dengan baris display, 2 kali 
        for i in range(2):
            time.sleep(1)
            clear_terminal()
            print("Kredit anda: ???")
            print()
            mystery = replace_baris(i + 1, mystery, display)
            regular_display_print(mystery)

        # Print bagian final
        time.sleep(1)
        clear_terminal()
        print(f"Kredit anda: {nilai_kredit()}")
        print(pesan)
        regular_display_print(display)

    # Jika animation dimatikan
    else: 
        print(f"Kredit anda: {nilai_kredit()}")
        print(pesan)
        regular_display_print(display)

