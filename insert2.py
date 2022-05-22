vowels = ['a', 'e', 'i', 'u']

def insert(vowels, index, value): 
    vowels.append("")
    #['a', 'e', 'i', 'u', " "]
    prev = vowels[index] # = "e" 
    for i in range(len(vowels)-1, index, -1): #c шагом в обратную сторону
        vowels[i] = vowels[i-1]
    vowels[index] = value
    return(vowels)

print(insert(vowels, 0, "p") )