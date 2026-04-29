def reverseNumber(n):  
    num=n
    result = 0

    while num>0:
        lastDigit = num%10
        result = (result*10)+lastDigit
        num=num//10
    return result==n
    #print(result)

reverse = reverseNumber(121)
print(reverse)


"""
def checkPalindrome(s):
    reversed_string = ""

    for char in s:
        reversed_string = char + reversed_string   # reverse the string

    return reversed_string == s


result = checkPalindrome("madam")
print(result)"""

"""
Convert number ➝ string
Reverse it
Convert result back to integer
Print the output as integer

def reverseNumber(n):
    # convert number to string
    s = str(n)
    
    # reverse string
    reversed_s = s[::-1]
    
    # convert back to integer
    result = int(reversed_s)
    
    return result


reverse = reverseNumber(121)
print(reverse)"""