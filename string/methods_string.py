word = 'pyTHon'
word_space = ' Python '

print(word.upper());
print(word.lower());
print(word.title());

# Spaces 
print(word_space.strip());
print(word_space.lstrip());
print(word_space.rstrip());

# Joins
print(word_space.center(10,"#"));
print("|".join(word_space));