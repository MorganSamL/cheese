def f3(a):
    my_list = []
    #my_list[1,a]
    for i in range(1,a+1):
        #in range (2, a//2)
        #range goes to a-1
        if a%i==0:
            my_list.append(i)
        return(my_list)

def f4():
    while True:
        try:
            n=input("Please write a multiple of 6")
            n =int(n)
        except ValueError:
            print("That was not a number")
            continue
            #continue brings you back to the top of the while
        if n%6 ==0:
            return n
        else:
            print("That was not a multiple of 6, please try again")
            continue





