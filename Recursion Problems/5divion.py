def countFactors (n):
    # code here
        
    result=[]
        
    for i in range(1,n+1):
        if n%i==0:
            result.append(i)
    return result

cf = countFactors(5)
print(cf)
print(len(cf))
