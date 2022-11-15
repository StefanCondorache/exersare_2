def fibonacci(x):
    fibo=[0,1]
    if x==0 :
        return []
    if x==1:
        return [0] 
    while len(fibo)!=x:
        nr=fibo[len(fibo)-1]+fibo[len(fibo)-2]
        fibo.append(nr)
    return fibo

print(fibonacci(100000)[-1])
