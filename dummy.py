    rows = [display[0], display[1], display[2]]
    diagonals = [
        [display[0][1], display[1][1], display[2][2]],
        [display[2][0], display[1][1], display[0][2]]
    ]

    hadiah = [0, 0, 1]      # [Kredit (default=0), FreeSpin (default=0), Multiplier (default=1)]

    def calculate_reward(symbols):
        reward_value = compare(symbols)
        if reward_value == "REROLL":
            hadiah[1] += 1
        elif reward_value == "REROLL+":
            hadiah[2] += 1
        else:
            hadiah[0] += reward_value
    
    if mode == 1:   # Horizontal tengah
        calculate_reward(rows[1])
    if mode == 2:   # Seluruh baris
        for row in rows:
            calculate_reward(row)
    if mode == 3:   # Diagonal termasuk
        for row in rows:
            calculate_reward(row)
        for diag in diagonals:
            calculate_reward(diag)
        
    return hadiah
