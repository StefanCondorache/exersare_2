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

print('obiecte_volum - ',obiecte_volum,'\n','obiecte_indice_sort - ',obiecte_indice_sort)

for i in obiecte_indice_sort:
    if sum(rucsac)<=volum_rucsac and sum(rucsac)+obiecte_volum[obiecte_indice.index(i)]<=volum_rucsac :
        rucsac.append(obiecte_volum[obiecte_indice.index(i)])
    else:
        obiecte_volum.remove(obiecte_volum[obiecte_indice.index(i)])

print('rucsac - ',rucsac)