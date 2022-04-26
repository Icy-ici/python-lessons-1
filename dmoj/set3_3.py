megabytes = int(input())
months = int(input())
used = []

for i in range(months):
    used.extend(input())

for i in used:
    used[i] = megabytes - used[i]

print(used)
