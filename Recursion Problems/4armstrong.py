def armstrongNumber(n):
    num=n
    total=0

    countPower = len(str(num))
    while num>0:
        lastDigit = num%10
        total = total+(lastDigit**countPower)
        num=num//10
    return total==n

arm  =armstrongNumber(159)
print(arm)