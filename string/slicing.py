# Slicing of string --> return parts of original string 

name = 'Olga Maria'

print(name[0]);
print(name[:4]);    # Takes from index 4
print(name[5:]);    # Takes until index 5
print(name[2:7]);   # Takes index 0 until index 5
print(name[0:9:2]); # Takes every two starting 0 until 9
print(name[:]);     # Takes all
print(name[::-1]);  # Inverse