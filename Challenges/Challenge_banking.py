# Create a bank system with operations withdraw, deposit and view extract

# It must be withdraw positives values
# Don't need worry about accounts and users
# Deposits and withdraw are storage for show in extract
# Have permitted three withdraw with a maximum R$ 500,00

balance = 0;
amount_withdraw = 0;
operations = [];


def breakLine():
    print('-------------------')

def withdraw():
    global balance, amount_withdraw, operations;

    if balance == 0:
        print(f"Balance: R$ {balance}");
        breakLine();
    elif amount_withdraw == 3:
        print("Exceeded the limit of 3 withdrawals");
        breakLine();
    else:
        value = float(input("Value for withdraw: "))

        if (value > 0) and (value <= 500): 
            balance -= value;
            operations.append(['Withdraw:', 'R$ ' + str(value)]);
            amount_withdraw += 1;
            print("Successfully withdrawn!");
            breakLine();
        else: 
            print("Invalid value");

def deposit():
    global balance, operations;

    value = float(input("Value for deposit: "))

    if value > 0:
        balance += value;
        operations.append(['Deposit:', 'R$ ' + str(value)]);
        print("Successfully deposited!");
        breakLine();
    else:
        print("Invalid value");

def extract():
    global balance, operations;

    if balance == 0:
        print("Movement was not carried out");
    else:
        print("-------Extract-------")
        print(" Operation | VALUE ")

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
        if option == 2:
            deposit();
        if option == 3:
            extract();
        if option == 0:
            print("Always come back!");
            breakLine();

# Begin the process  
main();
