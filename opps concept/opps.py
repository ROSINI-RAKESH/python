users ={123:{"name":"kaja", "balance":100000},
        234:{"name":"rose", "balance":20000}}

class Sample():
    def __init__(self):
        print('''Welcome to Canara Bank
Please insert your card''')
        
    def atm(self,users):
        pin =  int(input("Please Enter Your Pin:"))
        if pin in users:
            userData = users[pin]
            print("Select Your Account Type")
            accounttype=int(input('''(1.Savings A/c 
2.Current A/c'''))
            
        if accounttype== 1 or accounttype== 2:
            option=int(input('''1.Balance 
2.Withdrawal 
3.Deposit 
4.Exit'''))    
            if option== 1:
                print(userData["balance"])

            elif option== 2:
                withdraw=int(input("Enter the withdrawal amount: "))
                userData["balance"] -=withdraw
                print("Your withdrawal amount: ",withdraw)
                print("Your current balance is",userData["balance"] )
                
            elif option== 3:
                deposit=int(input("Enter the deposit amount: "))
                userData["balance"] +=deposit
                print("Your deposit amount: ",deposit)
                print("Your current balance is",userData["balance"] )

            elif option ==4:
                exit=input("Do you want to exit yes/no")
                if exit=="yes":
                    print("exit successful...")
                else:
                    print("continue") 
                # elif option ==1:
                #     checkBalance=input("Do you want to check balance yes/no:")
                #     if checkBalance=="yes":
                #         print(balance)

                    # else:
                    #     exit=input("Do you want to exit yes/no")
                    #     if exit=="yes":
                    #         return 
                    #     else:
                    #         self.atm()
                # elif option=="3":
                #     deposit=int(input("Enter the Deposit amount: "))
                #     balance +=deposit
                #     checkBalance=input("Do you want to check balance yes/no:")
                #     if checkBalance=="yes":
                #         print(balance)
                        
          
execute=Sample()
execute.atm(users)






                
                              
