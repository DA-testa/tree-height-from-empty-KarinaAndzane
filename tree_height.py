# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    max_height = 1
    # Your code here
    number = parents[0]
    while number!=-1:
        for j in range(n):
            if number== j :
                number = parents[j]
                max_height=max_height+1
                
    return max_height


def main():
    # implement input form keyboard and from files

    # file=input()
    # with open (file, mode='r') as f:
    #     readen = f.read()

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    mode=input()
    if 'I' in mode:
         text=input()
        
    if 'F'in mode:
          filename=input()
          with open ("./test/"+filename, mode ='r') as fails:
             text=fails.read()
             
   
    text=list(map(int,text.split()))
    print(compute_height(text[0],text[1:]))

    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
