volum_rucsac=float(input('voulumul rucsacului> '))
rucsac=[]

obiecte_volum=[]
obiecte_pret=[]
obiecte_indice=[]

for i in range(int(input('cate obiecte vor fi in total> '))):
    vi=float(input(f'volumul{i+1}> '))
    pi=float(input(f'pretul{i+1}> '))
    if vi<=volum_rucsac:
        obiecte_volum.append(vi)
        obiecte_pret.append(pi)
        obiecte_indice.append(pi/vi)
    else:
        print(f'obiectul cu volumul {vi} nu va incapea in rucsac cu volumul {volum_rucsac}')

obiecte_indice_sort=obiecte_indice.copy()
obiecte_indice_sort.sort(reverse=True)

i=0                                                                                 
suma=0

while sum(rucsac)<=volum_rucsac and i!=len(obiecte_indice_sort):                                                # <<<<<<<< pentru obiecte infinite
    if sum(rucsac)+obiecte_volum[obiecte_indice.index(obiecte_indice_sort[i])]<=volum_rucsac:
        rucsac.append(obiecte_volum[obiecte_indice.index(obiecte_indice_sort[i])])
        suma+=obiecte_pret[obiecte_indice.index(obiecte_indice_sort[i])]
    else:
        i+=1

print(f'volumul total care a incaput este {sum(rucsac)} cu volumele {rucsac}')
print(f'suma totala este {suma}')
#print('obiecte_volum - ',obiecte_volum,'\n','obiecte_indice_sort - ',obiecte_indice_sort)                      #<<<<<< pentru obiecte finite

#for i in obiecte_indice_sort:
    #if sum(rucsac)<=volum_rucsac and sum(rucsac)+obiecte_volum[obiecte_indice.index(i)]<=volum_rucsac :
    #    rucsac.append(obiecte_volum[obiecte_indice.index(i)])
    #else:
    #    obiecte_volum.remove(obiecte_volum[obiecte_indice.index(i)])

#print('rucsac - ',rucsac)
