account_number = "80549061"

def get_balance(account_number: str) -> float:
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                acc_num, balance = line.strip().split(",")
                if acc_num == account_number:
                    return float(balance)
        return 0.0
    except FileNotFoundError:
        print("The accounts file does not exist.")
        return 0.0

def update_account(account_number: str, balance: float):
    lines = []
    account_found = False

    with open("accounts.txt", "r") as file:
        lines = file.readlines()

    with open("accounts.txt", "w") as file:
        for line in lines:
            acc_num, bal = line.strip().split(",")
            if acc_num == account_number:
                file.write(f"{account_number},{balance}\n")
                account_found = True
            else:
                file.write(line)
        if not account_found:
            file.write(f"{account_number},{balance}\n")

def deposit(account_number: str):
    amount = float(input("Enter the deposit amount: "))
    balance = get_balance(account_number)
    new_balance = balance + amount
    update_account(account_number, new_balance)
    print(f"Deposited: Rs{amount:.2f}")

def withdraw(account_number: str):
    amount = float(input("Enter the withdrawal amount: "))
    balance = get_balance(account_number)
    if balance >= amount:
        new_balance = balance - amount
        update_account(account_number, new_balance)
        print(f"Withdrew: Rs{amount:.2f}")
    else:
        print("Insufficient funds for this withdrawal.")

print(f"**************************************")
print(f"You'r Account Number: {account_number}")
print(f"**************************************")

print(f"The Current Amount in you'r Account- Rs:{get_balance(account_number):.2f}")

deposit(account_number)
print(f"Balance for account after deposit- Rs:{get_balance(account_number):.2f}")

withdraw(account_number)
print(f"Balance for account after withdrawal- Rs:{get_balance(account_number):.2f}")
