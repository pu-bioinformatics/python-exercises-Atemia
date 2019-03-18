#!/Users/ATEMIA/miniconda3/bin/python
# ATM DEPOSIT,WITHDRAWAL AND BALANCE CHECK
acountbal = 50000
choice = input("Please enter 'b' to check balance, 'w' to withdraw or 'd' to deposit: ")
while choice != 'q':
    if choice.lower() in ('w','b','d'):
        if choice.lower() == 'b':
            print("Your balance is: %d" % acountbal)
            print("Anything else?")
            choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
        else:
            if choice.lower() == 'd':
                deposit = float(input("Enter amount to deposit: "))
                acountbal = (acountbal + deposit)
                print("your new balance is: %.2f" % acountbal)
                print("Anything else")
                choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
            else:
                withdraw = float(input("Enter amount to withdraw: "))
                if withdraw <= acountbal:
                    print("here is your: %.2f" % withdraw)
                    acountbal = acountbal - withdraw
                    print("Anything else?")
                    choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
                        #choice = 'q' 
                else:
                    print("you have insuficient funds: %.2f" % acountbal)
                    choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
    else:
        print("Bad choice!")
        choice = input("Please enter 'b' to check balance, 'w' to withdraw or 'd' to deposit: ")