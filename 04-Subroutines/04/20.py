def max_dice_rolls_in_row(dice):
    max_count = 1
    current_count = 1
    most_rolled_dice = dice[0]

    for i in range(1, len(dice)):
        if dice[i] == dice[i-1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                most_rolled_dice = dice[i-1]
            current_count = 1

    if current_count > max_count:
        most_rolled_dice = dice[-1]

    return most_rolled_dice

# main program
dice1 = "5233165554211"
dice2 = "2133"

print(f"f(\"{dice1}\") returns {max_dice_rolls_in_row(dice1)}")  # 5
print(f"f(\"{dice2}\") returns {max_dice_rolls_in_row(dice2)}")  # 3