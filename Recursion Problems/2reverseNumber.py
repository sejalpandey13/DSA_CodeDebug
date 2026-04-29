def reverseNumber(n):  
    num=n
    result = 0

    while num>0:
        lastDigit = num%10
        result = (result*10)+lastDigit
        num=num//10
    return result
    

reverse = reverseNumber(123)
print(reverse)

"""
def reverseNumber(n):  
    num=n
    result = 0

    while num>0:
        lastDigit = num%10
        result = (result*10)+lastDigit
        num=num//10
    print(result)

reverse = reverseNumber(123)"""
