print('Aritmetic Operators');

## Plus (Sum)
print(1 + 1);

## Minus
print(10 - 1);

## Multiplication
print(10 * 2);

## Divided by or // for integer
print(10 / 2);

## Modulo (rest of division)
print(10 % 3);

## Exponent
print(2 ** 3);

#######################
print('Comparison Operators');

a = 10;
b = 99;

print(a > b);
print(a < b);
print(a >= b); # <=
print(a == b);
print(a != b);

#######################
print('Atribuition Operators');
value = 150;

value += 10; # value = value + 10
value -= 10; # value = value - 10
value *= 10; # value = value * 10
value %= 10; # value = value % 10

print(value);

#######################
print('Logical Operators');

c = 55;

print(a > b and a < c);
print(a > c or c < b);
print(not a > b);

#######################
print('Identity Operators');

curse = 'Data Engineering';
name_curse = curse;
d, e = 10, 10;

print(curse is name_curse);
print(curse is not name_curse);
print(d is e);

#######################
print('Association Operators');

fruits = ['apple', 'banana', 'orange'];

print('apple' in fruits);
print('apple' not in fruits);

#######################
