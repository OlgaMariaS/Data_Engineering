## In Python the convention for blocks of code is add : to start and 4 spaces to indent

def is_even(number):

    if (number % 2) == 0:
        ## All the code inside the if block will be executed when have 4 spaces (stay inside if)
        print('Is even');
        return True
    else:
        print('Is not even');
        return False

is_even(10);
is_even(11)