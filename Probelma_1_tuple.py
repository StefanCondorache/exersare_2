elevi = [('Condorache','Stefan','M',8,9,10),('Creciun','Mihail','M',1,2,3),('Reaboi','Pasa','M',10,10,10),('Iacuboi','Anna','F',10,10,10),('Piatra','Felicia','F',7,8,10)]
note = []
for i in elevi:
    note.append(round(sum(i[3:])/3,2))
    print('elevul',i[:2],'are nota medie = ',round(sum(i[3:])/3,2))

print('\n','elevii restantierii sunt:')
for i in note:
    if i < 5:
        print('elevul',elevi[note.index(i)][:2])

print('\n')

for i in elevi:
    if round(sum(i[3:])/3,2) >= 9 :
        for j in i[3:]:
            if j < 9:
                term = False
                break
            else:
                term = True
        if term:    
            print('elevul',i[:2],'este eminent')