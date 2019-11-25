num = int(input("Write a number"))
if(num>1):
    is_prime=True
    for i in range (2,num//2):
        if(num%i==0):
            print(num, "not prime")
            is_prime=False
            break
    if is_prime:
        print(num, "is prime")