#Bank management system
'''class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, user_id, initial_balance=0):
        if user_id not in self.accounts:
            self.accounts[user_id] = initial_balance
            print("Account created successfully.")
        else:
            print("User already has an account.")
    def deposit(self, user_id, amount):
        if user_id in self.accounts:
            if amount > 0:
                self.accounts[user_id] += amount
                print(f"Deposited  ₹{amount}.")
            else:
                print("Invalid deposit amount.")
        else:
            print("User does not have an account.")
    def withdraw(self, user_id, amount):
        if user_id in self.accounts:
            if 0 < amount <= self.accounts[user_id]:
                self.accounts[user_id] -= amount
                print(f"Withdrew  ₹{amount}.")
            else:
                print("Insufficient funds or invalid withdrawal amount.")
        else:
            print("User does not have an account.")
    def get_balance(self, user_id):
        if user_id in self.accounts:
            print(f"Current Balance for user {user_id}:  ₹{self.accounts[user_id]}")
        else:
            print("User does not have an account.")
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def deposit(self, bank, amount):
        bank.deposit(self.user_id, amount)
    def withdraw(self, bank, amount):
        bank.withdraw(self.user_id, amount)
    def view_balance(self, bank):
        bank.get_balance(self.user_id)
def main():
    bank = Bank()
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            user_id = input("Enter your user ID: ")
            bank.create_account(user_id)
        elif choice == '2':
            user_id = input("Enter your user ID: ")
            amount = float(input("Enter amount to deposit: "))
            user = User(user_id)
            user.deposit(bank, amount)
        elif choice == '3':
            user_id = input("Enter your user ID: ")
            amount = float(input("Enter amount to withdraw: "))
            user = User(user_id)
            user.withdraw(bank, amount)
        elif choice == '4':
            user_id = input("Enter your user ID: ")
            user = User(user_id)
            user.view_balance(bank)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
main()'''
#Tick tack toe
'''def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)
def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True
    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        row = int(input("Enter row (1, 2, 3): ")) - 1
        col = int(input("Enter column (1, 2, 3): ")) - 1
        if board[row][col] == " ":
            board[row][col] = player
            print_board(board)
            if check_winner(board):
                print(f"Player {player} wins!")
                break
            elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                print("It's a draw!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken. Try again.")
main()'''