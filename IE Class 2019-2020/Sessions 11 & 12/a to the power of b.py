def f2(a,b):
    if b == 0:
        return 1
    return (a*f2(a,b-1))
#you are calling a method inside a method, that is the definition of a recursive function
