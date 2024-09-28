# Parameters for positional or nameade


# Only for keywords
def create_car(*, model, year, plate, mark, engine, fuel):
    print(model, year, plate, mark, engine, fuel);

# Before / is accepted arguments for position, and after / are optional (position or keyword)
def create_car(model, year, plate, /, mark, engine, fuel):
    print(model, year, plate, mark, engine, fuel);

# Before / is accepted arguments for position, and after / for Keyword (*)
def create_car(model, year, plate, /, *, mark, engine, fuel):
    print(model, year, plate, mark, engine, fuel);

create_car("Argo", 2018,  "BCE-1D34", mark="Fiat", engine="1.3", fuel="Flex");

# Objectives in firts order
def sum(a, b):
    return a + b

def show_result(x, y):
    print(f"{x} + {y} = {sum(x, y)} ");

show_result(10,20);

# Scopes
salary = 2000;

def salary_more_bonus(bonus):
    global salary
    salary += bonus
    return salary

print(salary_more_bonus(150));