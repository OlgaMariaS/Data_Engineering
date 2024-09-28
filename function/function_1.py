# Basic 
def show_message(message):
    print(f" {message} ");

test = 'Olga'
word = "Python"
msg = 'I am learning right now'

show_message(test);
show_message(word);
show_message(msg);

# Arguments names
def profile(name, age, high):
    print(f'Your name is {name}, have {age} and high {high}');

profile("Python",35, None);
profile(name = "Olga", age = 22, high = 1.50);
profile(**{"name":"Jose", "age":30, "high":1.85});

# *args(tuple) and **kwargs(dictionary)