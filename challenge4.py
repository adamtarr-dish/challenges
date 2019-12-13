from numToWords import *

def fib(n):
    if n<3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(11):
    num = fib(i+1)
    print(num, " - ", numToWords(num))

