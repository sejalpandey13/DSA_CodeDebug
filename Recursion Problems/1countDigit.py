def countDigit(n):
    num=n
    count = 0

    while num>0:
        count += 1
        num=num//10
    return count

digit = countDigit(2345)
print(digit)