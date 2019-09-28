sequence = input("Please enter random lower case letters")

for i in range (0, 1):
    result = sequence[i]
result1 = " "
for i in range (0, len(sequence)):
    if i + 1 == len(sequence):
        if len(result) > len(result1):
            result1 = result
            break
        else:
            break
    elif sequence[i] < sequence[i+1] or sequence[i] == sequence[i+1]:
        result = result + sequence[i+1]
    else:
        if len(result) > len(result1):
            result1 = result
            result = sequence[i+1]
        else:
            result = sequence[i+1]
            continue
print(result1)



