from numToWords import *

def fib(n):
    if n<3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    last2 = [1, 1]
    if n<2:
        return 1
    else:
        for x in range(2, n):
            temp = last2[1]
            last2[1]=last2[0]+last2[1]
            last2[0]=temp
        return last2[1]

def fib3(n):
    fibseq = [1, 1]
    if n<2:
        return 1
    else:
        for index in range(2, n):
            fibseq.append(fibseq[index-1]+fibseq[index-2])
        return fibseq[n-1]


for i in range(16):
    num = fib2(i+1)
    print(num, " - ", numToWords(num))