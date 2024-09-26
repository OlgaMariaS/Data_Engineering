## In Python the convention for blocks of code is add : to start and 4 spaces to indent

def is_even(number):

    ## All the code inside the if block will be executed when have 4 spaces (stay inside if)
    if number == 0:
        print('Is zero');
        return False
    elif (number % 2) == 0:
        print('Is even');
        return True
    else:
        print('Is not even');
        return False

is_even(0);
is_even(1);
is_even(2);

## If and else ternary 

def is_even_ternary(number):
    'Is even' if (number % 2) == 0 else 'Is not even';
##  return       if is true        if is false do else, return this