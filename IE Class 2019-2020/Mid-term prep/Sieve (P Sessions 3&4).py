n=int(input("Please write a random number"))

prime_number = []

for i in range (2,n):
    prime=True
    for y in range (2,i//2):
        if (i%y==0):
            prime = False
            break
    if prime:
        prime_number.append(i)
print(prime_number)
print(4/2)