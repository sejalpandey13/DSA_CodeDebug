# Print name n times using recursion
# This is head recursion type of recursion as the recursive call is made at the end of the function

count=0
def printName(n):
    global count
    if count==n:
        return
    print("My name is John")
    count+=1
    printName(n)

printName(10)