from itertools import combinations
A={1,2,3,'A','B','C'}
for i in range(len(A)):
    print(list(combinations(A,i)))

