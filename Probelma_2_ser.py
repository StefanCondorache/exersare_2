x={1,2,3}
y={2,3,4}
term = True
for i in range(x):
    for j in range(y):
        if j<0 or j>200 or i <0 or i>200:
            term = False
if term:
    print(x,'\n',y)
    print('xUy = ', x|y)
    print('xny = ', x&y)
    print('x\y = ', x-y)
    print('(X\Y)U(Y\X) = ',(x-y)|(y-x))
    print('(X\Y)ꓵ(Y\X)= ', (x-y)&(y-x))