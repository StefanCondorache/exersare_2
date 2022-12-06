# Determinarea numerelor perfecte 

n=int(input("n > "))
suma = 0

def raspuns(a):
    global suma
    if suma==a:
        print(a)
        suma=0
    else:
        suma=0 

def verificare(a,b):
    if b<=a:
        global suma
        if a%b==0 and a!=b:
            suma+=b
        return True
    else:
        return False
        
for x in range(1,n+1):
    for y in range(1,n+1):
        if verificare(x,y):
            if x==y:
                raspuns(x)
        else:
            continue
