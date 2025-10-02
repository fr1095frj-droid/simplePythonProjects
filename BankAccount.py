
print("* Welcome to Bank Account App *")

balance = 1000

def show_balance(add=0, sub=0):
    global balance
    balance = balance + add - sub
    return balance

def deposit():
    amount = input("Enter amount to deposit: ")
    if not amount.isdigit():
        print("You did not enter a valid amount.")
        return 0
    amount = int(amount)
    show_balance(add=amount)



def withdraw():
    amount = input("Enter amount to withdraw: ")
    if not amount.isdigit():
        print("You did not enter a valid amount.")
        return 0
    amount = int(amount)
    if amount > show_balance():
        print('You don\'t have enough money in your account.')
        return 0
    show_balance(sub=amount)




while True:
    print('Which opperation would you like to do?')
    print('1. Showing Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')
    answer = input('>> ')
    if answer == '1':
        print(f'Your balance is: ${show_balance()}')
    elif answer == '2':
        deposit()
    elif answer == '3':
        withdraw()
    elif answer == '4':
        break
    else:
        print('Please enter a valid answer.')
        continue
    next = input('Do you need to do another opperation? (y / n): ').lower() == 'y'
    if next == 'y':
        continue

print('Have a good day')
