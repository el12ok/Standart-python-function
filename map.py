# def map(function_name, argument_list): 
#     for i in argument_list: 
#         function_name(i)

# function_name = len

from math import radians
import time 
import random
argument_list = ("apple", "cherry", "banana")
list_random = []
for i in range(10_000_000): 
    list_random.append(random.choice(argument_list))
s = time.time()
x = map(len, list_random)
print(time.time()-s)
# print(list(x))

s = time.time()
list = []
for number_words in list_random: 
    list.append(len(number_words))
print(time.time()-s)
# print(list)