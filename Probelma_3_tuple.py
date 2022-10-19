n=int(input('numarul de personae; '))
list1 = []
for i in range(n):              #vârsta, înălțimea, masa (greutatea), sexul(genul), starea civilă(căsătorit sau nu)
    persoana = []
    age = int(input('vârsta; ')); persoana.append(age)
    height = int(input('inaltime (cm); ')); persoana.append(height)
    weight = int(input('greutate (kg); ')); persoana.append(weight)
    gender = str(input('sexul (M/F); ')); persoana.append(gender)
    sc = str(input('starea civila (da/nu); ')); persoana.append(sc)
    list1.append(tuple(persoana))

nr_age = 0
nr_height = 0
weight = 0
nr_weight = 0
nr_ft = 0
nr_fnu = 0
nr_20_50 =0
nr_high_weight = 0
weight_med = sum([i[2] for i in list1])/len(list1)

for i in list1:
    if i[0]<20:
        nr_age += 1
    if i[1]>170:
        nr_height += 1
    if i[0]>=18:
        weight+=i[2]
        nr_weight+=1
    if i[3]=='F':
        nr_ft += 1
        if i[4]=='nu':
            nr_fnu += 1
    if i[0]>=20 and i[0]<=50:
        nr_20_50 += 1
        if i[2]>weight_med:
            nr_high_weight += 1

print('\n',list1)
print(nr_age,'de persoane cu varsta sub 20 de ani')
print('procentul persoanelor cu inaltimea mai mare de 170 = ',round(nr_height/n,2)*100)
print("masa medie a persoanelor cu varsta de peste 18 ani = ",weight/nr_weight)
print('procentul din numărul persoanelor de sex feminin ce au peste 20 de ani și nu sunt căsătorite = ',round(nr_fnu/nr_ft,2)*100)
print('procentul din numărul persoanelor între 20 și 50 ani care au greutatea mai mare decât greutatea medie = ',round(nr_high_weight/nr_20_50,2)*100)