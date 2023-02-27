import sys
import threading


# def compute_height(n, parents):
#     Write this function
#     max_height = 1
#     Your code here
#     number = parents[0]
#     while number!=-1:
#         for j in range(n):
#             if number== j :
#                 number = parents[j]
#                 max_height=max_height+1
                


#     return max_height
def length(i, parents):
    #int inkrement=0
    #int height=0
    if parents[i]==-1:
        return 0
    return  1+length(parents[i],parents)

def compute_height(parents):
    max_height=0
    for i in range (len(parents)):
        max_height=max(max_height, length(i,parents))
        
    return max_height + 1
def main():
    # implement input form keyboard and from files


    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    mode=input()
    if "I" in mode:
         text=input()
         text=list(map(int,text.split()))
         print(compute_height(text[1:]))
        
    if "F" in mode:
          filename=input()
          with open ("./test/"+filename, mode ='r') as fails:
             n=int(fails.readline())
             text = fails.readline()
             text=list(map(int,text.split()))
             print(compute_height(text))
   
    
    

    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
