import random



options = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
user = ""
file = open("./RockPaperScissor.txt", "r")
content = file.read().split("\n")
userPoint = int(content[0][-1])
computerPoint = int(content[1][-1])
draw = int(content[2][-1])
flag = False


def userInput():
    global user
    user = input("Choose one (Rock, Paper, Scissor, Lizard, Spock) q for quit:")
    if user not in options:
        if(user == "q"):
            update = open("./RockPaperScissor.txt", "w")
            update.write(f"user = {userPoint}\ncomputer = {computerPoint}\nDraw = {draw}")
            print("Good Bye")
            global flag
            flag = True
        else:
            print("Invalid choice. Please try again.")
            userInput()


while(True):
    userInput()
    if(flag):
        break
    computer = random.choice(options)
    print("Computer Choice:", computer)
    if(computer == user):
        draw += 1
    elif((computer == options[0] and user == options[1]) or (computer == options[0] and user == options[4])):
        userPoint += 1
    elif((computer == options[0] and user == options[2]) or (computer == options[0] and user == options[3])):
        computerPoint += 1
    elif((computer == options[1] and user == options[3]) or (computer == options[1] and user == options[2])):
        userPoint += 1
    elif((computer == options[1] and user == options[0]) or (computer == options[1] and user == options[4])):
        computerPoint += 1
    elif((computer == options[2] and user == options[0]) or (computer == options[2] and user == options[4])):
        userPoint += 1
    elif((computer == options[2] and user == options[1]) or (computer == options[2] and user == options[3])):
        computerPoint += 1
    elif((computer == options[3] and user == options[0]) or (computer == options[3] and user == options[2])):
        userPoint += 1
    elif((computer == options[3] and user == options[4]) or (computer == options[3] and user == options[1])):
        computerPoint += 1
    elif((computer == options[4] and user == options[1]) or (computer == options[4] and user == options[3])):
        userPoint += 1
    elif((computer == options[4] and user == options[2]) or (computer == options[4] and user == options[0])):
        computerPoint += 1

    print("---------Scores-----------")
    print("|    User:", userPoint, "            |")
    print("|    Computer:", computerPoint, "        |")
    print("|    Draw:", draw, "            |")
    print("--------------------------")



    
    # elif(computer == options[0] and user == options[2]):
    #     computerPoint += 1
    # elif(computer == options[0] and user == options[1]):
    #     userPoint += 1
    # elif(computer == options[1] and user == options[2]):
    #     userPoint += 1
    # elif(computer ==options[1] and user == options[0]):
    #     computerPoint += 1
    # elif(computer == options[2] and user == options[0]):
    #     userPoint += 1
    # elif(computer == options[2] and user == options[1]):
    #     computerPoint += 1
    