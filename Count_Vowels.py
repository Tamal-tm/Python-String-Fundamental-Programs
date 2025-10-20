# Using dictionary. 

a="Harry Potter and the Prisoner of Azkaban" 
vowels="aeiou"
a=a.casefold()
print(a)

count={}.fromkeys(vowels,0) # {a:0,e:0,i:0,o:0,i:0} A dictionary is made. 

for char in a:
    if char in count:
        count[char] +=1
        
print(count)

# Using list and dictionary comprehension. 

a="Harry Potter and the Goblet of Fire" 
vowels="aeiou"
a=a.casefold()
print(a)

count={key:sum([1 for char in a if char == key]) for key in vowels} # for loop created if character is matching with the keys which are vowels, added to sum.  


print(count)











