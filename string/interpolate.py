# Types for use and concatenete string

name = 'Olga'
age = 22 
vocation = 'Data Engineer'
language =  'Python'

# Don't usually use
print("%")
print('Hi, I am %s and I have %d years, work as %s with %s' % (name, age, vocation, language));

# Method Format                                                        0    1       2       3           (Could print for index)
print(".Format")
print('Hi, I am {} and I have {} years, work as {} with {} '.format(name, age, vocation, language));

# Function f-string
print("F-string")
print(f'Hi, I am {name} and I have {age} years, work as {vocation} with {language} ');
