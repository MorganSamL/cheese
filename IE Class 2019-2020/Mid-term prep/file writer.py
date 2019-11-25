f = open("yourock","w")
flag = True
while flag:
    wrote= input("Please write what you want to put on file")
    if wrote=="quit":
        flag=False
        break
    else:
        f.write(wrote)