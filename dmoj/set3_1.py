cup_index = 1
moves = input()

for i in range(0, len(moves)):
    if moves[i] == "A":
        if cup_index == 1:
            cup_index = 2
        elif cup_index == 2:
            cup_index = 1
    elif moves[i] == "B":
        if cup_index == 2:
            cup_index = 3
        elif cup_index == 3:
            cup_index = 2
    elif moves[i] == "C":
        if cup_index == 1:
            cup_index = 3
        elif cup_index == 3:
            cup_index = 1

print(cup_index)