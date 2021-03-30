import sys
import time

#Fibonacci sequence is produced by adding a number to the one that preceeded it
#For this fibonacci sequence the first two starter numbers are 1 and 0
#This produces the sequence [0,1],1,2,3,5,8,13,21
#Different starting numbers can produce different sequences, however this sequence is the most famous
# -----
# The argument taken into the function references the number returned at the given position along the sequence 
#e.g.  Fib(0) == 0, Fib(1) == 1, Fib(2) == 1, Fib(3) == 2, etc...
def fib_rec(n):
    if (n<1):
        return(0)
    elif (n==1):
        return(1)
    else:
        #we can produce the fibonacci number at pos n if we know what the number is at pos n-1 and pos n-2
        #this self referencing works as long as there are conditions to catch it 
        return(fib_slow(n-1) + fib_slow(n-2))

#Fast Fib takes advantage of the fact that a lot of redundant work is created when doing the recursive method
def fib_fast(n):
    mem = [0,1]
    # mem[0] = 0
    # mem[1] = 1

    if(n<1):
        return mem[0]
    elif(n==1):
        return mem[1]
    
    for i in range(2,n+1):
        mem.append(mem[i-1] + mem[i-2])

    return mem[n]
    
    

if __name__ == "__main__":
    position = int(input("Type a number for the related fibonacci number: "))
    
    # begin = time.time()
    fib_n = fib_rec(position)
    # end = time.time()
    # timed = end-begin
    print(f"the fib number at position {position} is {fib_n}")

    fib_n_f = fib_fast(position)
    # print(f"this took {time} seconds to compute using non-dynamic programming")
    print(f"fast fib is {fib_n_f}")
