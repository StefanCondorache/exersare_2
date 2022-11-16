def sum_prod_iterativ(x):
    suma=0
    for i in range(x+1):
        suma+=i*(2*(i-1))
    return suma

def sum_prod_recursiv(x):
    if x==0:
        return x
    else:
        return x*(2*(x-1))+sum_prod_recursiv(x-1)

def sum_raport_iterativ(x):
    suma=0
    for i in range(x+1):
        suma+=i/((2*i-1)*(2*i+1))
    return suma

def sum_raport_recursiv(x):
    if x==0:
        return x
    else:
        return (x/((2*x-1)*(2*x+1)))+sum_raport_recursiv(x-1)
n=int(input("n> "))
print("a)iterativ) ",sum_prod_iterativ(n))
print("a)recursiv) ",sum_prod_recursiv(n))
print("b)iterativ) ",sum_raport_iterativ(n))
print("b)recursiv) ",sum_raport_recursiv(n))