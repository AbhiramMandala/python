# operations
operation = (
    "1. Balance\n",
    "2. Withdraw\n",
    "3. Deposit\n",
    "4. Transfer\n",
    "5. History\n",
    "6. Logout\n",
)

# account_table
account = {
    12345: "6789",
    12346: "6788"
}

# user_details table
user_details = {
    12345: ["praveen", 1000, "Praveen@praveen.com", []],  # [] for history
    12346: ["naveen", 2000, "naveenveerl@gmail.com", []]
}

# login function
def login(user_name: int, password: str):
    if user_name in account:
        if account[user_name] == password:
            print("Successfully Logged in to Codegnan Online Netbank")
            return True
        else:
            print("Incorrect password")
    else:
        print("User not found")
    return False


# balance function
def balance(user_name: int):
    if user_name in user_details:
        amount = user_details[user_name][1]
        print(f"Current Balance: {amount}")
    else:
        print("User not found")


# withdraw function
def withdraw(user_name: int, withdraw_amount: int):
    if user_name in user_details:
        amount = user_details[user_name][1]
        if withdraw_amount <= amount:
            user_details[user_name][1] -= withdraw_amount
            user_details[user_name][3].append(f"Withdraw: {withdraw_amount}")
            print(f"Successfully withdrawn {withdraw_amount}")
            print(f"Current Balance: {user_details[user_name][1]}")
        else:
            print("Insufficient funds")
    else:
        print("User not found")


# deposit function
def deposit(user_name: int, deposit_amount: int):
    if user_name in user_details:
        user_details[user_name][1] += deposit_amount
        user_details[user_name][3].append(f"Deposit: {deposit_amount}")
        print(f"Successfully deposited {deposit_amount}")
        print(f"Current Balance: {user_details[user_name][1]}")
    else:
        print("User not found")


# transfer function
def transfer(user_name: int, to_account: int, transfer_amount: int):
    if user_name in user_details:
        if to_account in user_details:
            amount = user_details[user_name][1]
            if transfer_amount <= amount:
                user_details[user_name][1] -= transfer_amount
                user_details[to_account][1] += transfer_amount
                user_details[user_name][3].append(f"Transfer to {to_account}: {transfer_amount}")
                user_details[to_account][3].append(f"Received from {user_name}: {transfer_amount}")
                print(f"Successfully transferred {transfer_amount} to {to_account}")
                print(f"Current Balance: {user_details[user_name][1]}")
            else:
                print("Insufficient balance")
        else:
            print(f"Receiver account {to_account} not found")
    else:
        print("User not found")


# history function
def history(user_name: int):
    if user_name in user_details:
        print("Transaction History:")
        for h in user_details[user_name][3]:
            print("-", h)
    else:
        print("User not found")


# logout function
def logout():
    print("You have been logged out.")
    exit()


# main function
if __name__ == "__main__":  # Corrected the typo here
    print("Welcome to Codegnan Online Netbanking App")
    accounts = int(input("Enter your Account Number: "))
    password = input("Enter your Password: ")
    if login(user_name=accounts, password=password):
        while True:
            print(*operation)
            choice = int(input("Please select your operation: "))
            if choice == 1:
                balance(user_name=accounts)
            elif choice == 2:
                amount = int(input("Enter Withdraw Amount: "))
                withdraw(user_name=accounts, withdraw_amount=amount)
            elif choice == 3:
                amount = int(input("Enter Deposit Amount: "))
                deposit(user_name=accounts, deposit_amount=amount)
            elif choice == 4:
                receiver_account = int(input("Enter Receiver Account Number: "))
                amount = int(input("Enter Transfer Amount: "))
                transfer(user_name=accounts, to_account=receiver_account, transfer_amount=amount)
            elif choice == 5:
                history(user_name=accounts)
            elif choice == 6:
                logout()
            else:
                print("Invalid choice! Please enter between 1-6")
