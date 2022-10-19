from random import randint,choice

a,b=randint(0,100),randint(0,100)
print('suma = ',a+b)
print('diferenta1 = ',a-b)
print('diferenta2 = ',b-a)
print('produsul = ',a*b,'\n')

list1=[]
for i in range(10):
    for i in range(5):
        list1.append(randint(0,36))
    print(list1)
    list1=[]

n=1
while ((n%6!=0) or (n%8!=0)):
    n=randint(0,999)
else:
    print('\n',n,'\n')

print('bun venit la ”Vreau să fiu milionar”')
teme=['Matematica','Informatica','Fizica','Biologia','Chimia']
intrebari = [['1+2=?','2+2=?','3+2=?','3+3=?','3+4=?','4+4=?','5+4=?','5+5=?','10*2=?','daca vantul are viteza de 2 km/h si soarele pe neasteptate a disparut, cum poate fi albastru egal cu 5 daca o rata a trecut drumul conform grarficului sinus, iar cealalta a ramas fara pene?'],
    ['5 in baza 2 = ?','True and False = ?','True or False = ?','unde se afla procesorul?','ce face functia print()?','pentru ce sunt librariile?','True zor False = ?','1010101 + 01010101 = ?','0101010 in baza 16 = ?','este C++ un limbaj de programare bun pentru incepatori?'],
    ['in ce se masoara forta?','cu ce este egala acceleratia gravitationala?','care este formula pentru legea atracției universale?','ce reprezinta lumina?','in ce se masoara viteza?','in ce se masoara sarcina electronica?','in ce se masoara Intensitatea?','in ce se masoara inaltimea?','in ce se masoara tensiunea?','daca gravitatia va fi anulata, cum vom putea cadea pe pamint?'],
    ['ce reprezinta citoplasma?','ce reprezinta celula?','ce reprezinta neuron?','ce reprezinta axon?','ce reprezinta gamet?','se inseamna haploid?','se inseamna dipliod','cati cromozomi are omul?','cati cromozomi are furnica?','daca molecula devine mai mica decat atomul, poate sangele sa circule prin vant fara pulsarea inimii?'],
    ['care este formula acidului acetic?','care-i formula acidului clorhidric?','care-i formula sarii?','care-i formula acidului sulfuric?','care-i formula acidului azotic?','care-i formula glucagonului?','care-i formula zaharoza?','care-i formula glucozei?','care-i formula fructozei?','care-i formula dioxid de carbon?','cati atomi de hidrogen poate avea un carbon trivalen?']]

a=choice(teme)
print('Tema: ',a)
print(choice(intrebari[teme.index(a)]))