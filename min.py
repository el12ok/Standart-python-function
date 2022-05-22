def _min(l):
    a = l[0]
    for i in l: 
        if i < a:
            a = i
    return(a)   


import random 
for index in range(10000): 
    l = []
    b = 100
    for i in range(b):
        l.append(random.randint(-1000, 1000))
    if min(l) != _min(l): 
        print(l)
        print(min(l), _min(l))

