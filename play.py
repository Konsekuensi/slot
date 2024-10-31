from utils import LEN, LEFT, MIDDLE, RIGHT, SYMBOL, kredit, clear_terminal, enter_to_continue, update_kredit, tampilkan_kredit, nilai_kredit
import random as rn

HADIAH = [0, 0, 1]      # INISIASI hadiah di sini nanti akan diupdate seiring fungsi berjalan
FREESPIN = 0
MULTIPLIER = 1

def main():
    play()


def play():
    # KREDIT: ---
    # ==============
    #
    #    ❔ ❔ ❔
    #    ❔ ❔ ❔
    #    ❔ ❔ ❔
    # 
    # ==============
    # Opsi bet (1/2/3) {1 untuk baris tengah, 2 untuk baris atas dan bawah, 3 untuk diagonal}
    # Enter untuk spin 
    # Ketik EXIT untuk keluar
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
        mode = int(input("Masukkan mode spin: "))
    
    while kred > 0:
        kred = nilai_kredit()
        clear_terminal()
        ans = input("Tekan Enter untuk Spin (ketik 0 untuk kembali) ")

        if ans == "0":
            break

        # DEBUG
        display = spin()

        reward(mode, display)
        print(HADIAH)
        bet(mode)
        
        
        print_display(display)

        if kred <= 0:
            print("Kredit Anda habis")
            break

        enter_to_continue()



def spin():
    pivot_kiri = rn.randint(0, LEN - 1)
    pivot_tengah = rn.randint(0, LEN - 1)
    pivot_kanan = rn.randint(0, LEN - 1)

    atas = [LEFT[pivot_kiri - 1], MIDDLE[pivot_tengah - 1], RIGHT[pivot_kanan - 1]]
    tengah = [LEFT[pivot_kiri], MIDDLE[pivot_tengah], RIGHT[pivot_kanan]]
    bawah = [LEFT[(pivot_kiri + 1) % LEN], MIDDLE[(pivot_tengah + 1) % LEN], RIGHT[(pivot_kanan + 1) % LEN]]

    return [atas, tengah, bawah]


def bet(mode): # TODO
    global HADIAH, FREESPIN, MULTIPLIER

    if FREESPIN > 0:           # Jika terdapat freespin
        FREESPIN -= 1
        HADIAH[1] = FREESPIN
        print("Freespin digunakan!")
    else:
        update_kredit(-5 * mode)

    update_kredit(HADIAH[0] * MULTIPLIER)
    
    if MULTIPLIER != 1:          # Jika multiplier digunakan
        MULTIPLIER = 1
        HADIAH[2] = MULTIPLIER
        print("Multiplier digunakan!")

    HADIAH[0] = 0
    FREESPIN, MULTIPLIER = HADIAH[1], HADIAH[2]


def compare(comp): # return hadiah
    # ["🌟", "💎", "🍉", "🍇", "🍓", "🔄", "⚡"]
    #   0     1     2     3      4     5     6

    freq = [0 for i in range(len(SYMBOL))]
    
    # jika terdapat simbol yang yang sama, masukkan sesuai index
    for symbol in comp:
        if symbol == "🌟":
            freq[0] = freq[0] + 1

        elif symbol == "💎":
            freq[1] = freq[1] + 1

        elif symbol == "🍉":
            freq[2] = freq[2] + 1

        elif symbol == "🍇":
            freq[3] = freq[3] + 1

        elif symbol == "🍓":
            freq[4] = freq[4] + 1

        elif symbol == "🔄":
            freq[5] = freq[5] + 1

        elif symbol == "⚡":
            freq[6] = freq[6] + 1
    
    # Bandingkan dengan list reward (kredit, reroll, atau reroll+)
    if freq[0] == 3 or freq[1] == 3:
        return 300
    elif (freq[0] == 2 and freq[1] == 1) or (freq[1] == 2 and freq[0] == 1): 
        return 90
    elif freq[2] == 3 or freq[3] == 3:
        return 15
    elif freq[4] == 2 or freq[4] == 3:
        return 8
    elif freq[4] == 1:
        return 4
    elif freq[5] == 3:
        return "REROLL"
    elif freq[6] == 3:
        return "REROLL+"
    else:
        return 0



def reward(mode, display): # TODO update HADIAH dengan [Kredit (default=0), FreeSpin (default=0), Multiplier (default=1)]
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
    main()