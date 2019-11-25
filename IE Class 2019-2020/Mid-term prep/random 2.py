String = "You have to give me da dough you doufus douche dynamite dinasour"
counter = 0
words = String.split()
for i in words:
    if counter < 3:
        if i[0] == "d":
            print(i)
            counter +=1




