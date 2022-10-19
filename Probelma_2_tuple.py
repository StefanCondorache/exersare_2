data = (19,10,'miercuri')
data = list(data)
numar = 0
while (data[1] >= 1):
    if data[0] > 7:
        numar+=1
        data[0]-=7
    else:
        data[1]-=1
        if data[1]==2:
            data[0]=28-(7-data[0])
        if data[1]<=7:
            if data[1]%2!=0:
                data[0]=31-(7-data[0])
            else:
                data[0]=30-(7-data[0])
        if data[1]>7:
            if data[1]%2!=0:
                data[0]=30-(7-data[0])
            else:
                data[0]=31-(7-data[0])

print(numar,'de',data[2],'sunt')