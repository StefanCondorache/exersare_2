def putere_iterativ(a,b):
    prod=1
    for i in range(b):
        prod*=a
    return prod

def putere_recursiv(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    else:
        return a*putere_recursiv(a,b-1)


print('2^15 = ',putere_iterativ(2,15))
print('4^10 = ',putere_recursiv(4,10))