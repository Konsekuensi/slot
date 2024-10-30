import os

# VAR GLOBAL
LEFT = [
    "🌟", "🍓", "🍉", "🔄", "⚡", "🍇", "💎", "🍇", "🍓", "⚡", "🔄", "🍉", "🌟", "⚡", "🍇", "🔄", "🍉", "💎", "⚡", "🍇", "🔄"
]

MIDDLE = [
    "🌟", "🍓", "🔄", "🍇", "🍉", "🍓", "🔄", "⚡", "⚡", "🍇", "💎", "🍇", "🔄", "🍓", "🍉", "🍇", "🔄", "🍓", "🍇", "🔄", "🍓"
    ]

RIGHT = [
    "🌟", "⚡", "💎", "🔄", "🍇", "🍉", "🔄", "🍇", "⚡", "🍉", "🔄", "🍇", "🍉", "⚡", "🔄", "🍇", "🍉", "⚡", "🔄", "🍇", "🍓"
]

SYMBOL = ["🌟", "💎", "🍉", "🍇", "🍓", "🔄", "⚡"]

LEN = len(LEFT)
kredit = 0


# FUNGSI
def clear_terminal():
    # Untuk Windows
    if os.name == "nt":
        os.system("cls")
    else: # untuk linux, mac, dan lainnya
        os.system("clear")


def enter_to_continue():
    print()
    print("Tekan enter untuk melanjutkan")
    input()


def update_kredit(amount):
    global kredit
    kredit += amount


def tampilkan_kredit():
    global kredit
    print(f"Kredit anda saat ini adalah: {kredit}")


def nilai_kredit():
    global kredit
    return kredit