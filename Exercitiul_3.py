def citire(x,y):
    if y==2*len(x)-1:
        return x[len(x)-1]
    else:
        print(x[y-len(x)])
        return citire(x,y+1)

def citire_inversa(x,y):
    if y==0:
        return x[y]
    else:
        print(x[y])
        return citire_inversa(x,y-1)       

def suma(x,y):
    if y==0:
        return x[y]
    else:
        return x[y]+suma(x,y-1)  

def suma_pare(x,y):
    if y==0 :
        if x[y]%2==0:
            return x[y]
        else:
            return 0
    else:
        if x[y]%2==0:
            return x[y]+suma_pare(x,y-1)  
        else:
            return suma_pare(x,y-1)

def suma_impare(x,y):
    if y==0 :
        if x[y]%2!=0:
            return x[y]
        else:
            return 0
    else:
        if x[y]%2!=0:
            return x[y]+suma_impare(x,y-1)  
        else:
            return suma_impare(x,y-1)

def elem_pare(x,y):
    if y==0 :
        if x[y]%2==0:
            return x[y]
        else:
            return ''
    else:
        if x[y]%2==0:
            print(x[y])
            return elem_pare(x,y-1)  
        else:
            return elem_pare(x,y-1)

def elem_impare(x,y):
    if y==0 :
        if x[y]%2!=0:
            return x[y]
        else:
            return ''
    else:
        if x[y]%2!=0:
            print(x[y])
            return elem_impare(x,y-1)  
        else:
            return elem_impare(x,y-1)

list1=(1,2,3,4,5,6,7,8,9,10)

print('a)')
print(citire(list1,len(list1)))
print('b)')
print(citire_inversa(list1,len(list1)-1))
print('c)',suma(list1,len(list1)-1))
print("d)",suma_pare(list1,len(list1)-1))
print("e)",suma_impare(list1,len(list1)-1))
print("f)")
print(elem_pare(list1,len(list1)-1))
print("g)")
print(elem_impare(list1,len(list1)-1))