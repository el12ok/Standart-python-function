def _max(l):
    a = l[0]
    for i in l: 
        if i > a:
            a = i
    return(a)   


import random 
for index in range(10000): 
    l = []
    b = 10
    for i in range(b):
        l.append(random.randint(-1000, 1000))
    if max(l) != _max(l): 
        print(l)
        print(max(l), _max(l))