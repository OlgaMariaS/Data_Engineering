# List are defined with word list or [,,,]
# e.g

fruits = ['orange', 'apple', 'banana', 'cramberry', 'grape', 'pineapple', 'watermelon']
letters = list('abcd')

# Direct access

print(fruits[1]);
print(letters[2]);
# Last item
print(fruits[-1]);
print(letters[-1]);

# Nested List (list inside list, like table)
score = [
    ['a', 10, 20],
    ['b', 30, 40],
    ['c', 50, 60]
]

score[0] # ['a', 10, 20]
score[0][2] # 10
score[-1][-2] # 50

# Slicing

print(fruits[0]);
print(fruits[:4]);    # Takes only untill index 4
print(fruits[2:]);    # Takes from index 2
print(fruits[2:5]);   # Takes index 2 until index 5
print(fruits[0:7:2]); # Takes every two starting 0 until 7
print(fruits[:]);     # Takes all
print(fruits[::-1]);  # Inverse

# Traverse a list
i = 0
for fruit in fruits:
    print(f"{i}: {fruit}")
    i+=1

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Comprerending
numbers = [1,2,3,4,5,6,7,8,9,10]

even = [number for number in numbers if number % 2 == 0]

print(even);