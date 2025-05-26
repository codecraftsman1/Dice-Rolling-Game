import random
playing = True
while playing:
    que = input("Do you want to roll a dice (Y/N) : ").lower()
    if que == "y":
        print(random.randrange(1,7))
    elif que == "n":
        print("Thanks for playing")
    else:
        print("INVALID INPUT")