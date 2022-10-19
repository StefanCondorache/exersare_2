from random import  randint
n = randint(0,10**3)
b = randint(2,9)
def verific(x,y):
    if y>1 and y<=9 and x>=0:
        for i in [int(j) for j in str(x)]:
            if i < y:
                val = True
            else:
                val = False
                print(x,'nu este scris corect in baza',y)
                break
        if val:
            print(x,'este scris corect in baza',y)
        return val
    else:
        print('baza nu apartine intervalului [1,9]')
        return False
def calcul(numar,baza):
    def creare_numere(numar,baza):
        raspuns = ''
        list1=[]
        while numar>0:
            list1.append(numar%baza)
            numar//=baza
        else:
            for i in list1[::-1]:
                raspuns+=str(i)
        return raspuns
    z = randint(0,10**3)
    if z>=0 and verific(numar,baza) and verific(z,baza):
        S=int(str(numar),baza)+int(str(z),baza)
        P=int(str(numar),baza)*int(str(z),baza)
        Sc1=int(str(numar),baza)-int(str(z),baza)
        Sc2=int(str(z),baza)-int(str(numar),baza)
        Raspuns='suma = '+str(creare_numere(S,baza))+'\n'+'scaderea nr1 = '+str(creare_numere(Sc1,b))+'\n'+'scaderea nr2 = '+str(creare_numere(Sc2,baza))+'\n'+'produsul = '+str(creare_numere(P,baza))
        return Raspuns
    else:
        return 'nu au fost indeplinite cerintele'
    
print(calcul(n,b))