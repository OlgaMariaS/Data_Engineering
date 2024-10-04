number = [0,1,2,3,4,3,3,2]

# Add an element in the list
number.append(1)
print(number)

# Make copy of list 
list_copy = number.copy()
print(id(list_copy), id(number))

# Count the number of occurrences in the list 
print(number.count(3))

# Extend this elements in the list 
number2 = [10,11,12]

number.extend(number2)
print(number)

# Remove all elements of list 
# number.clear()
# print(number)

# Which the first index of value 
number.index(10)

# The List could work like a stack 

# Stack up -  Last In, First Out (LIFO) principle
#number.push(15) # add 15 in the end

# Unstack
number.pop() # remove 12
number.pop(0) # remove the elementy in the index 0

# Remove 
number.remove(4)

# Inverter
number.reverse()
print(number)

# Order the list
number.sort() # Or have the function sorted()
print(number)

# Order by length when be string
# list.sort(key=lambda x: len(x)) 

# Length
len(number)

