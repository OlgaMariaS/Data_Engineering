# While Structure 

option = 1

while option != 0:
    option = int(input("Enter an option: "))

    if option == 0:
        print('Bye')
    elif option == 1:
        print('Continue...')
    else:
        print('Invalid option')

# Have break (stop execution) and continue (jump execution)