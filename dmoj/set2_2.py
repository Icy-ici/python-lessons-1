d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())

if d1 == 8 or d1 == 9:
    if d4 == 8 or d4 == 9:
        if d2 == d3:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")
