x={1,2,3,4}
y={2,3,4,5}
z={3,4,5,6}
sett=[]
for i in range(200):
    sett.append(i)
sett=set(sett)
settx=sett.copy()
setty=sett.copy()
settz=sett.copy()
xyz1=x|y|z
for i in x:
    settx.discard(i)
for i in y:
    setty.discard(i)
for i in z:
    settz.discard(i)
for i in xyz1:
    sett.discard(i)

if sett==(settx&setty&settz):
    print(True,' pentru primul caz')
else:
    print(False,' pentru primul caz')

sett=[]
for i in range(200):
    sett.append(i)
sett=set(sett)
xyz2=x&y&z
for i in xyz2:
    sett.discard(i)

if sett==(settx|setty|settz):
    print(True,' pentru primul caz')
else:
    print(False)