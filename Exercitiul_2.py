def CMMDC(x , y):
    if y == 0:
        return x
    else:
        return CMMDC(y, x % y)
n=int(input("n> "))
m=int(input("m> "))
def verificare(x,y):
    if x<y:
        return CMMDC(x,y-x)
    if x>y:
        return CMMDC(x-y,y)
    if x==y:
        return x
print(verificare(m,n))