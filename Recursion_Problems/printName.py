# Print name n times using recursion
# This is head recursion

count=0
def printName(n):
    global count
    if count==n:
        return
    print("My name is John")
    count+=1
    printName(n)

printName(10)