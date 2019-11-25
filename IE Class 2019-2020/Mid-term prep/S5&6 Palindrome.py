palindrome = input("please enter potential palindrome")
num =len(palindrome) -1
flag = True
length = len(palindrome)//2
counter =0
while counter <= length:
    for i in palindrome:
        counter += 1
        if i!=palindrome[num]:
            print("not a palindrome")
            flag = False
            break
        else:
            num -=1
    if flag ==False:
        break
if flag:
    print(palindrome + " is a palindrome")


