spaces = int(input())

yesterday = input()
today = input()

both = 0

for i in range(0, spaces):
    if yesterday[i] == today[i] and today[i] == "C":
        both += 1

print(both)