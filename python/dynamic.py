import sys
import time

""" ------Overview------
Fibonacci sequence is produced by adding a number to the one that preceeded it
For this fibonacci sequence the first two starter numbers are 1 and 0
This produces the sequence [0,1],1,2,3,5,8,13,21
Different starting numbers can produce different sequences, however this sequence is the most famous
The argument taken into the function references the number returned at the given position along the sequence 
e.g.  Fib(0) == 0, Fib(1) == 1, Fib(2) == 1, Fib(3) == 2, etc... """


""" ------ Fibonacci Recursive ------
Description: fib_rec solves the problem by taking the the number we want and working backwards
                since the last number is produced by the addition of the previous two elements, 
                fib_rec is called again using the previous elements in a naive recursive manner

Complexity - Runtime: O(2^n) - Every call produces two branches, while the tree may not be 
                        filled out entirely this will become 2^n under big O
Complexity - Space: O(n) - the call stack should only be holding the elements that form a straight
                            line from the root node to a leaf node, thus only requiring n stack elements
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



""" ------ Fibonacci Dynamic Memoization ------
Description: fib_dyn_mem solves the problem above by minimising the number of times the 
                same function is called in many parts of the tree by passing a partially 
                completed version of the mem array as its filled out. This is beneficial 
                when wanting to solve top-down and solve only the function calls that will
                be required

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
    


""" ------ Fibonacci Dynamic Tabulation ------
Description: fib_dyn solves the problem by starting at the bottom and solving for every entry
                until the desired result is achieved. This takes advantage of the fact that a 
                lot of redundant work is created when done recursively by calling the same 
                function many times. 

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

    
