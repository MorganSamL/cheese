
Answer = "SSNWES"
counter = 0
lives = 3
while True:

    for i in range(0,6):
        move = input("Please write your move")
        counter += 1
        if counter == 10 or counter == 20 or counter == 30:
            lives += -1
            if lives == 0:
                break
            else:
                print("You have just lost a life. You now only have ", lives, ". Watch out!")
        if i==5:
            if move[i] == Answer[i]:
                print("Congratulations, you have won the game!!! with " , lives , " left")
                counter = -1
                break
        elif counter == 30:
            break
        elif move[i] != Answer[i]:
            print("that was wrong", counter)
            break
        else:
            print("Correct" , i)

    if counter == 30:
        print("You have run out of moves, please try again")
        break
    elif lives == 0:
        print("You have run out of lives, please try again")
        break
    elif counter == -1:
        break
    else:
        continue









