print("Welcome to Stone Paper Scissor.")
print("This is a round of 5 game.")
print("Press any key to start.")

q = input()
i = 1

user_score = 0
bot_score = 0

while i < 6:
    while True:
        print("Enter :")
        print("1 : Stone")
        print("2 : Paper")
        print("3 : Scissor")
        try:
            user_in = int(input())
            if user_in == 1 or user_in == 2 or user_in == 3:
                break
            else:
                print("Invalid Input")
                continue
        except:
            print("Invalid Input")
            continue

    import random

    bot_in = random.randint(1, 3)

    user_match = ""
    bot_match = ""

    if user_in == 1:
        user_match = "Stone"

    if user_in == 2:
        user_match = "Paper"

    if user_in == 3:
        user_match = "Scissor"

    if bot_in == 1:
        bot_match = "Stone"

    if bot_in == 2:
        bot_match = "Paper"

    if bot_in == 3:
        bot_match = "Scissor"
    match = f"{user_match} VS {bot_match}"

    print(match)

    if user_in == 1 and bot_in == 1:
        win = 0

    elif user_in == 1 and bot_in == 2:
        win = 2

    elif user_in == 1 and bot_in == 3:
        win = 1

    elif user_in == 2 and bot_in == 1:
        win = 1

    elif user_in == 2 and bot_in == 2:
        win = 0

    elif user_in == 2 and bot_in == 3:
        win = 2

    elif user_in == 3 and bot_in == 1:
        win = 2

    elif user_in == 3 and bot_in == 2:
        win = 1

    else:
        win = 0

    if win == 0:
        print("Match Draw")

    elif win == 1:
        print("You won")
        user_score += 1


    else:
        print("You lost")
        bot_score += 1

    print(f"Your score : {user_score}")
    print(f"Opponent's score : {bot_score}")

    q = input()
    i += 1

f = open("stats", "r")
games = int(f.readline())
won = int(f.readline())
lost = int(f.readline())
draw = int(f.readline())
f.close()

games += 1

if user_score > bot_score:
    print("You won the game")
    won += 1


elif bot_score > user_score:
    print("You lost the game")
    lost += 1


else:
    draw += 1
    print("Game draw")

f = open("stats", "w")

print("Games played : ", games)
print("Games won : ",won)
print("Games lost : ", lost)
print("Games drawn : ",draw)

f.write(f"{games}\n {won}\n{lost}\n{draw}")
