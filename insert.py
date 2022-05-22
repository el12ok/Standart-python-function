#insert
vowels = ['a', 'e', 'i', 'u']
# vowels.insert(3, 'o')
# print('insert:', vowels)


def insert(vowels, index, value): 
    vowels.append("")
    prev = vowels[index] # = "e" 
    for i in range(index, len(vowels)-1): #пустая ячейка никуда не сдвигается
        curr = vowels[i+1] # = "i"
        vowels[i+1] = prev
        prev = curr 
    vowels[index] = value
    return(vowels)
    
# 0 a
# 1 e 
# 2 i
# 3 u 
# 4 ''

['a', 'e', 'i', 'u', ' ']
['a', 'o', 'e', 'i', 'u']
print(insert(vowels, 2, "l") )