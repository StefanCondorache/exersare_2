def CMMDC(x , y):
    if y == 0:
        return x
    else:
        return CMMDC(y, x % y)
n=int(input("n> "))
m=int(input("m> "))
def verfificare(x,y):
    if x<y:
        if CMMDC(x,y)==CMMDC(x,y-x):
            return 'm>n',True
        else:
            return 'm>n',False 
    if x>y:
        if CMMDC(x,y)==CMMDC(x-y,y):
            return 'm>n',True
        else:
            return 'm>n',False
    if x==y:
        if CMMDC(x,y)==CMMDC(x-y,y):
            return 'm>n',True
        else:
            return 'm>n',False

