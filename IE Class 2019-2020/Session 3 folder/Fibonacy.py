
def fib(n):
    prepre =0
    pre=1
    if n==0:
        return prepre
    elif n==1:
        return pre
    for i in range(2,n):
        fib2 = pre + prepre
        prepre = pre
        pre= fib2
    return fib2