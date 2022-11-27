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

for i in range(len(obiecte_volum)-2):
    for j in range(len(obiecte_pret)-2):
        if (obiecte_volum[i]/obiecte_pret[i]==obiecte_volum[j+1]/obiecte_pret[j+1]) and (obiecte_volum[i]<obiecte_volum[j+1]):
            temp_vol=obiecte_volum[j+1]
            obiecte_volum[j+1]=obiecte_volum[i]
            obiecte_volum[i]=temp_vol
            temp_pret=obiecte_pret[j+1]
            obiecte_pret[j+1]=obiecte_pret[i]
            obiecte_pret[i]=temp_pret

obiecte_volum_2=obiecte_volum.copy()
obiecte_indice_sort=obiecte_indice.copy()
obiecte_indice_sort.sort(reverse=True)

for i in obiecte_indice_sort:
    if sum(rucsac)<=volum_rucsac and sum(rucsac)+obiecte_volum[obiecte_indice.index(i)]<=volum_rucsac :
        rucsac.append(obiecte_volum[obiecte_indice.index(i)])
        obiecte_volum.remove(obiecte_volum[obiecte_indice.index(i)])

print('rucsac - ',rucsac)
print('suma> ',sum([obiecte_pret[obiecte_volum_2.index(i)] for i in rucsac]))

