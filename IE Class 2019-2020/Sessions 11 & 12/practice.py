def fl(filename):
    fd = open (filename)
    for line in fd:
        words = line.split()
        for word in words:
            if len(word) == 3 and word [0] == "b":
                print (word)
