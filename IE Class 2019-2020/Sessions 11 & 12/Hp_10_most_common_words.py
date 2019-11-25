punctuation1= ",.;:!?/'()[]{}-*<>"""
def common_words(a):
    fd = open(a, "r")
    d={}
    for line in fd:
        for c in punctuation1:
            line = line.replace(c, " ")
        words = line.split().lowercase()
        for word in words:
            if word in d:
                d[word] +=1
            else:
                d[word] =1

    common_words("Harrypotter.txt")

    values =list(d.values())
    values.sort(reverse=True)
    common= []
    for numbers in values[:10]:
        for keys in d:
            if d[keys] == numbers:
                common.append(keys.numbers)
    print("the most common words are:")
    for i in common:
        print(i[0], i[1], "times")







