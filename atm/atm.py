# pin number
# balance
# withdraw
# deposit
# user option

atm=int(input("Enter the pin number"))
balanceAmt=30000
pinNumber=3456

def myfunction(atm,pinNumber,balanceAmt):
    while True:
        if atm==pinNumber:
            account=input("Enter the account Type Current A/c or Savings A/c or exit :")
            if account.lower()=="current a/c" or account.lower()=="savings a/c":
                check=input("Check Balance Amount: enter 1,Withdraw Amount: enter 2,Deposit Amount enter 3:")
                if check=="1":
                    print("Balance Amount",balanceAmt)
                elif check=="2":
                    withdraw=int(input("Enter the withdraw amount"))
                    balanceAmt -=withdraw
                    checkBalance=input("Do you want to check the balance amount yes/no:")
                    if checkBalance=="yes":
                        print(balanceAmt)
                        exit=input("Do you want to exit yes/no")
                        if exit=="yes":
                            break
                        else:
                            continue
                    else:
                        exit=input("Do you want to exit yes/no:")
                        if exit=="yes":
                            break
                        else:
                            continue
                elif check=="3":
                    deposit=int(input("Enter the deposit amount:"))
                    balanceAmt +=deposit
                    checkDepositBalance=input("Do you want to check the balance amount yes/no:")
                    if checkDepositBalance=="yes":
                        print(balanceAmt)
                        exit=input("Do you want to exit yes/no:")
                        if exit=="yes":
                            break
                        else:
                            continue
                    else:
                       exit=input("Do you want to exit yes/no:")
                       if exit=="yes":
                           break
                       else:
                           continue
            else:
                exit=input("Do you want to exit yes/no:")
                if exit=="yes":
                    break
                else:
                    continue
            
        else:
            print("pin number is wrong")

myfunction(atm,pinNumber,balanceAmt)