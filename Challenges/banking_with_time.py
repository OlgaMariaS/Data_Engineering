import datetime

# Create a bank system with operations withdraw, deposit and view extract

# It must be withdraw positives values
# Don't need worry about accounts and users
# Deposits and withdraw are storage for show in extract
# Have permitted ten transations, being withdraw with a maximum R$ 500,00

balance = 0;
amount_transations = 0;
operations = [];
limit_transations = 10;


def breakLine():
    print('______________________________')

def withdraw():
    global balance, amount_transations, operations, limit_transations

    if balance == 0:
        print(f"Balance: R$ {balance}");
        breakLine();
    elif amount_transations == limit_transations:
        print(f"Exceeded the limit of {limit_transations} transations");
        breakLine();
    else:
        value = float(input("Value for withdraw: "))

        if (value > 0) and (value <= 500): 
            # Catching the current date and time and put in the brazilian pattern 
            current_date = datetime.datetime.now()
            current_date = current_date.strftime("%d/%m/%Y as %H:%M")

            balance -= value;
            operations.append(['Withdraw:', 'R$ ' + str(value), current_date]);
            amount_transations += 1;
            print("Successfully withdrawn!");
            breakLine();
        else: 
            print("Invalid value");

def deposit():
    global balance, amount_transations, operations, limit_transations

    if amount_transations == limit_transations:
        print(f"Exceeded the limit of {limit_transations} transations");
        breakLine();
    else: 
        value = float(input("Value for deposit: "))

        if value > 0:
            # Catching the current date and time and put in the brazilian pattern 
            current_date = datetime.datetime.now()
            current_date = current_date.strftime("%d/%m/%Y as %H:%M")

            balance += value;
            operations.append(['Deposit:', 'R$ ' + str(value), current_date]);
            amount_transations += 1;
            print("Successfully deposited!");
            breakLine();
        else:
            print("Invalid value");

def extract():
    global balance, operations;

    if balance == 0:
        print("Movement was not carried out");
    else:
        print("---------Extract---------")
        print(" Operation   |     VALUE   |     Date ")

        for operation in operations:
            print(" ".join(operation) + "\n");

        print(f"\nBalance: R$ {balance}");
        breakLine();

def main():
    option = -1;
    message = f"""
    Choose an option:
        [1] Withdraw
        [2] Deposit
        [3] Extract
        [0] Go Out
    """;
    
    while option != 0:
        option = int(input(message));

        if option == 1:
            withdraw();
        elif option == 2:
            deposit();
        elif option == 3:
            extract();
        elif option == 0:
            print("Always come back!");
            breakLine();
        else: 
            print("Wrong choice, choose again");

# Begin the process  
main();
