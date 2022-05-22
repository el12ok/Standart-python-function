#index
_list = ['cat', 'bat', 'mat', 'cat', 'pet']
# print("index:", _list.index('cat'))

def index(_list, item): 
    for index, value in enumerate(_list):
        if item == value: 
            return(index)
    return("Error")

print(index(_list, "lol"))


#sort
prime_numbers = [11, 3, 7, 5, 2]
prime_numbers.sort()
print("sort:", prime_numbers)


#reverse
prime_numbers = [9, 123, 71, 5, 22]
prime_numbers.reverse()
print("reverse:", prime_numbers)

#extend 
prime_numbers = {
    "a": "key", 
    "b": "doom", 
    "c": "juice"
}
second_numbers = [565, 909]
second_numbers.extend(prime_numbers)
print("extend:", second_numbers)