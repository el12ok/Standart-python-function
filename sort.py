numbers = [2, 17, 3, 875, 13, 1, 0, 19]
numbers.sort()
print(numbers)

#modified the list
numbers.sort(reverse=True)
print(numbers)

#create a new list 
print(sorted(numbers))

print(sorted(numbers, reverse=True))

items = [
    ("Product", 10),
    ("Product", 8), 
    ("Product", 12)
]
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items, sep = "\n")

print()


numbers = []
import random 
for i in range(15): 
    numbers.append(random.randint(0, 100))

    
def sort(numbers): 
    start = 0 
    for i in range(len(numbers)):    
        for j in range(i, len(numbers)):    
            if(numbers[i] > numbers[j]):
                start = numbers[i]    
                numbers[i] = numbers[j]    
                numbers[j] = start   
    return(numbers) 

print(sort(numbers))