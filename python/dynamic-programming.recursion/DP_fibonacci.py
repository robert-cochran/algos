import sys
import time

""" 
------Overview------
Fibonacci sequence [0,1],1,2,3,5,8,13,21
e.g.  Fib(0) == 0, Fib(1) == 1, Fib(2) == 1, Fib(3) == 2, etc... 
"""


""" 
------ Fibonacci Recursive ------
Description: Recursive naive/brute force solution 
Complexity - Runtime: O(2^n)
Complexity - Space: O(n) - the call stack forms a straight line from the root node to a leaf node, thus only requiring n stack elements
"""
def fib_rec(n):
    if (n<1):
        return(0)
    elif (n==1):
        return(1)
    else:
        #we can produce the fibonacci number at pos n if we know what the number is at pos n-1 and pos n-2
        #this self referencing works as long as there are conditions to catch it (i.e. if n<1 and if n==1)
        return(fib_rec(n-1) + fib_rec(n-2))



""" 
------ Fibonacci Dynamic Memoization ------
Description - top down memoizatioon for only values needed to be computed and stored
Complexity - Runtime: O(n)
Complexity - Spacetime: O(n) - this might be larger since the array is being passed through functions
"""
def fib_dyn_mem(n, mem):
    if (n<1):
        return 0
    elif (n==1):
        return 1
    elif (mem[n] == None):
        mem[n] = fib_dyn_mem(n-1, mem) + fib_dyn_mem(n-2, mem)
        return (mem[n])
    else:
        return mem[n]
    


""" 
------ Fibonacci Dynamic Tabulation ------
Description: bottom up tabulatin where all values are calculated 
Complexity - Runtime: O(n) - reducing the time complexity of the original function down from O(2^n) to O(n)
Complexity - Spacetime: O(n) 
"""
def fib_dyn_tab(n):
    mem = [0,1]

    if(n<1):
        return mem[0]
    elif(n==1):
        return mem[1]
    
    for i in range(2,n+1):
        mem.append(mem[i-1] + mem[i-2])

    return mem[n]
    
    

if __name__ == "__main__":
    position = int(input("Type a number: "))
    
    begin_rec = time.time()
    fib_rec = fib_rec(position)
    end_rec = time.time()
    time_rec = end_rec - begin_rec

    begin_dm = time.time()
    # l = [None] * (position+1)
    fdm = fib_dyn_mem(position, [None]*(position+1))
    end_dm = time.time()
    time_dm = end_dm - begin_dm
    
    begin_dt = time.time()
    fdt = fib_dyn_tab(position)
    end_dt = time.time()
    time_dt = end_dt - begin_dt
    
    print(f"The fibonacci number at position {position} is {fib_rec}")

    print(f"Recursive: Computation time taken was {time_rec:0.4f}s")
    print(f"Memoization: Computation time taken was {time_dm:0.4f}s")
    print(f"Tabulation: Computation time taken was {time_dt:0.4f}s")

    
