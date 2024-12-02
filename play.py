from utils import LEN, LEFT, MIDDLE, RIGHT, kredit, clear_terminal, update_kredit, tampilkan_kredit, nilai_kredit
import random as rn

HADIAH = [0, 0, 1]      # INISIASI hadiah di sini nanti akan diupdate seiring fungsi berjalan
FREESPIN = 0
MULTIPLIER = 1


def play():
    global kredit, HADIAH

    display = [
        ["❔", "❔", "❔"],
        ["❔", "❔", "❔"],
        ["❔", "❔", "❔"]
    ]

    clear_terminal()
    kred = nilai_kredit()
    print(kred)
    print_display(display)
    
    mode = 0
    while mode not in [1, 2, 3]:
        mode = int(input("Masukkan mode spin (1/2/3): "))
    
    while kred > 0:
        kred = nilai_kredit()
        clear_terminal()
        ans = input("Tekan Enter untuk Spin (ketik 0 untuk kembali) ")

        if ans == "0":      # KELUAR DARI PERMAINAN
            break

        display = spin()
        reward(mode, display)
        bet(mode)
        print_display(display)

        if kred <= 0:
            print("Kredit Anda habis")
            break

        ans = input("Tekan Enter untuk Spin (ketik 0 untuk kembali) ")

        if ans == "0":      # KELUAR DARI PERMAINAN
            break


def spin():
    pivot_kiri = rn.randint(0, LEN - 1)
    pivot_tengah = rn.randint(0, LEN - 1)
    pivot_kanan = rn.randint(0, LEN - 1)

    atas = [LEFT[pivot_kiri - 1], MIDDLE[pivot_tengah - 1], RIGHT[pivot_kanan - 1]]
    tengah = [LEFT[pivot_kiri], MIDDLE[pivot_tengah], RIGHT[pivot_kanan]]
    bawah = [LEFT[(pivot_kiri + 1) % LEN], MIDDLE[(pivot_tengah + 1) % LEN], RIGHT[(pivot_kanan + 1) % LEN]]

    return [atas, tengah, bawah]


def bet(mode): # Mengurangi kredit user seharga harga spin, dan menambahkan kredit user sebanyak yang dimenangkan
    global HADIAH, FREESPIN, MULTIPLIER

    if FREESPIN > 0:            # Jika terdapat freespin
        FREESPIN -= 1
        HADIAH[1] = FREESPIN
    else:
        update_kredit(-5 * mode)

    update_kredit(HADIAH[0] * MULTIPLIER)
    if HADIAH[0] * MULTIPLIER != 0:
        print(f"Selamat Anda mendapatkan {HADIAH[0] * MULTIPLIER} kredit!")
    
    if MULTIPLIER != 1:          # Jika multiplier digunakan
        MULTIPLIER = 1
        HADIAH[2] = MULTIPLIER

    HADIAH[0] = 0
    FREESPIN, MULTIPLIER = HADIAH[1], HADIAH[2]


def reward(mode, display): # update HADIAH dengan [Kredit (default=0), FreeSpin (default=0), Multiplier (default=1)]  
    def compare(comp): # return hadiah
        freq = {
            "🌟": 0, "💎": 0, "🍉": 0, "🍇": 0, "🍓": 0, "🔄": 0, "⚡": 0
        }
        
        # jika terdapat simbol yang yang sama, masukkan sesuai index
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
    
    global HADIAH
    rows = [display[0], display[1], display[2]]
    diag1 = [display[0][0], display[1][1], display[2][2]]
    diag2 = [display[0][2], display[1][1], display[2][0]]
    
    def update(h):
        if h == "REROLL":
            HADIAH[1] += 1
        elif h == "REROLL+":
            HADIAH[1] += 1
            HADIAH[2] *= 2
        else:
            HADIAH[0] += h

    if mode == 1:       # Cek display[1] (horizontal tengah)
        h = compare(display[1])
        update(h)
        
    else:               # Cek mode 2 dan mode 3 
        for row in rows:        # Cek semua baris
            h = compare(row)
            update(h)
        if mode == 3:           # Mode 3 only
            h = compare(diag1)
            update(h)
            h = compare(diag2)
            update(h)


def print_display(display):
    global kredit
    tampilkan_kredit()
    print("==============")
    print()
    for baris in display:
        print(end="   ")
        for kolom in baris:
            print(kolom, end=" ")
        print()
    print()
    print("==============")


if __name__ == "__main__":
    play()