def count(_list, item_to_count):
    a = 0
    for i in _list: 
        if i == item_to_count: 
            a+=1
    return a

arr = [3, 1, 2, 2, 0, 3, 3, 3, 4]
print(count(arr, 3))

fruits = ("apple", "cherry", "banana")
print(count(fruits, "cherry"))

import random
import time 
random_list = []
for i in range(10_000_000): 
    random_list.append(random.randint(1, 100))
s = time.time()
print(random_list.count(5))
print(time.time()-s)

s = time.time()
print(count(random_list, 5))
print(time.time()-s)