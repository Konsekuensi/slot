from utils import LEN, LEFT, MIDDLE, RIGHT, SYMBOL, kredit, clear_terminal, enter_to_continue, update_kredit, tampilkan_kredit, nilai_kredit
import random as rn


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
    global kredit

    hadiah = [0, 0, 1]
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

        bet(mode, display, hadiah)

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


def bet(mode, display, hadiah): # TODO
    # LOGIKA FREESPIN DAN MULTIPLIER MASIH BELUM TEPAT

    spin = hadiah[1]
    multiplier = hadiah[2]

    def update(harga):
        nonlocal spin, multiplier
        update_kredit(hadiah[0] * multiplier)           # tambah kredit jika menang
        
        print(f"spin: {spin}")
        print(f"multiplier: {multiplier}")

        if multiplier != 1:
            print("Menggunakan multiplier")
            multiplier = 1
        
        if spin > 0:
            spin -= 1
            print("Menggunakan freespin!")
            enter_to_continue()
        else:
            update_kredit(harga)                 # harga 1 spin


        multiplier = hadiah[2]
        spin += hadiah[1]



    print(reward(mode, display))
    hadiah = reward(mode, display)

    if mode == 1:
        update(-10)
    elif mode == 2:
        update(-20)
    else:
        update(-30)


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
    elif freq[4] == 2:
        return 8
    elif freq[4] == 1:
        return 4
    elif freq[5] == 3:
        return "REROLL"
    elif freq[6] == 3:
        return "REROLL+"
    else:
        return 0


def reward(mode, display): # Return list hadiah dengan [Kredit (default=0), FreeSpin (default=0), Multiplier (default=1)]
    list1 = [display[0][0], display[0][1], display[0][2]] # horizontal atas
    list2 = [display[1][0], display[1][1], display[1][2]] # horizontal tengah
    list3 = [display[2][0], display[2][1], display[2][2]] # horizontal bawah
    list4 = [display[0][0], display[1][1], display[2][2]] # diagonal kiri
    list5 = [display[2][0], display[1][1], display[0][2]] # diagonal kanan

    if mode == 1:       # Horizontal tengah saja
        hadiah = compare(list2)
        if hadiah == "REROLL":
            return [0, 1, 1]
        elif hadiah == "REROLL+":
            return [0, 1, 2]
        else:
            return [hadiah, 0, 1]
        
    elif mode == 2:     # Seluruh Baris
        hadiah = [compare(list1), compare(list2), compare(list3)]
        
        hf = [0, 0, 1]
        for i in hadiah:
            if i == "REROLL":
                hf[1] = hf[1] + 1
            elif i == "REROLL+":
                hf[1] = hf[1] + 1
                hf[2] = hf[2] * 2
            else:
                hf[0] = hf[0] + i

        return hf

    elif mode == 3:     # Sama diagonalnya
        hadiah = [compare(list1), compare(list2), compare(list3), compare(list4), compare(list5)]

        hf = [0, 0, 1]
        for i in hadiah:
            if i == "REROLL":
                hf[1] = hf[1] + 1
            elif i == "REROLL+":
                hf[1] = hf[1] + 1
                hf[2] = hf[2] * 2
            else:
                hf[0] = hf[0] + i
        
        return hf


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