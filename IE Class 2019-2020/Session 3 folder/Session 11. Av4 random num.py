import random

def f(list_numbers):
    n = list_numbers[0]
    for i in list_numbers:
        if i > n:
            n = i
    return n

number_list = []
for i in range(4):
    number_list.append(random.randint(-1000, 1000))
a = f(number_list)
print(a)

def avg (list_numbers):
    sum=0
    for i in list_numbers:
        sum = sum+i
    average = sum/len(list_numbers)
    return average

i =0
b=[]
for i in range(i<4):
    try:
        n=input('give me a number')
        n=int(n)
        b.append(n)
        i=i+1
    except ValueError:
        print ('Please enter a number')
