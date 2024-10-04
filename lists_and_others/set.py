# Set is a collection of objects not repeated 

# For eliminate elements repeated in a list
numbers = [1,2,3,3,4,3,5]
set(numbers)

# Collection doens't have support for indexing, because of this, we need convert set in a list 
number = {1,2,3,3,4,3,5}
number = list(number)
print(number)

# We can work mathematical rules math with collection 
set_a = {1,2,5}
set_b = {3,4,5}

set_a.union(set_b) # 1,2,5,3,4
set_a.intersection(set_b) # 5
set_a.difference(set_b) # 1,2 
set_b.difference(set_a) # 3,4
set_b.symmetric_difference(set_a) # 1,2,3,4

# checks if one set belongs to another
set_a.issubset(set_b) # true/false
# if both set doens't have elementy in common 
set_a.isdisjoint(set_b) # true/false

# Add, clear, copy, discard, pop, remove, len, in
set_a.add(8)
set_a.pop()
set_a.copy()
set_a.discard(8)
set_a.remove(8)
set_a.clear(8)


