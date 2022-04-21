apple_score = int(input()*3 + input()*2 + input())
banana_score = int(input()*3 + input()*2 + input())

if (apple_score < banana_score):
    print("A")
elif (banana_score < apple_score):
    print("B")
elif (apple_score == banana_score):
    print("T")