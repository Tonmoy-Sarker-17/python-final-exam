
from abc import ABC, abstractmethod

class Account(ABC):
    accounts=[]
    loan=True
    def __init__(self,name,email,address,accountNo,password,type):
        self.bankrupt= False

        self.loan_no=0
        self.name=name
        self.email=email
        self.address=address
        self.accountNo = accountNo
        self.passW=password
        self.balance = 0
        self.type=type
        Account.accounts.append(self)

    transaction_history=[]
    def transactions(self,transaction):
        Account.transaction_history.append(transaction)
        
    
    def changeInfo(self,name):
        self.name=name
        print(f"\n--> Name is changed of {self.accounNo}")
    
    #Overloading of method changeInfo
    def changeInfo(self,name,email,address,passW):
        self.name=name
        self.email=email
        self.address=address
        self.passW=passW
        print(f"\n--> Name, Email,Address and Password are changed of {self.accountNo}")
    
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            Bank.totalbalance+=amount
            print(f"\n--> Deposited {amount}. New balance: ${self.balance} in account no: {self.accountNo}")
            self.transactions(f'(Deposited {amount}. New balance: ${self.balance} in account no: {self.accountNo})')
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance and self.bankrupt==False:
            self.balance -= amount
            Bank.totalbalance-=amount
            print(f"\nWithdrew ${amount}. New balance: ${self.balance} from account no: {self.accountNo}")
            self.transactions(f'( Withdrew ${amount}. New balance: ${self.balance} from account no: {self.accountNo})')
        elif self.bankrupt==True:
            print("Bank is Bankrupt")
        else:
            print("\nWithdrawal amount exceeded")

    def transfer_amount(self,amount,fromAccNO,toAccNo):
        # if fromAccNO in Account.accounts:
        #     Account.accounts.balance-=amount
            
        # if toAccNo in Account.accounts:
        #    Account.accounts.balance+=amount
        print(f'/n  (total {amount} is trasferred to account no:{toAccNo} from account no:{fromAccNO})')
        self.transactions(f' (total {amount} is trasferred to account no:{toAccNo} from account no:{fromAccNO})')

    def applyLoan(self,amount):
        Bank.totalbalance-=amount
        Bank.total_loanammount+=amount
        self.loan_no+=1
        if Account.loan==False or self.loan_no>2:
            print("\n ''cannot take more loan''")
        else:
            print("\n --> You can apply for Loan :)")


    def show_available_balance(self):
        print('\nyour balance is : ',self.balance)

    @abstractmethod
    def showInfo(self):
        pass


class SavingsAccount(Account):
    def __init__(self,name,email,address,accountNo,password):
        super().__init__(name,email,address,accountNo,password,"savings")
        self.interestRate = 7
        

    def apply_interest(self):
        interest = self.balance*(self.interestRate/100)
        #msg
        print("\n--> Interest is applied !")
        self.deposit(interest)
    
    def showInfo(self):
        print(f"Infos of {self.type} account of {self.name}:\n")
        print(f'\n\tAccount Type : {self.type}')
        print(f'\tName : {self.name}')
        print(f'\tEmail id: {self.email}')
        print(f'\tAddress: {self.address}')
        print(f'\tAccount No : {self.accountNo}')
        print(f'\tCurrent Balance : {self.balance}\n')

    def changeInfo(self, name,address,email, passW):
        return super().changeInfo(name,address,email, passW)


class CurrentAccount(Account):
    def __init__(self,name,email,address,accountNo,password,limit):
        super().__init__(name,email,address,accountNo,password,"current")
        self.limit=limit
        

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) and self.bankrupt==False >= -self.limit:
            self.balance -= amount
            Bank.totalbalance-=amount
            print(f"\n--> Withdrew ${amount}. New balance: ${self.balance} from account {self.accountNo}")
            Account.transactions('',f'(Withdrew ${amount}. New balance: ${self.balance} from account {self.accountNo})')
        elif self.bankrupt==True:
            print("Bank is Bankrupt")
        else:
            print("\n--> Withdrawal amount exceeded")
            
    def showInfo(self):
        print(f"Infos of {self.type} account of {self.name}:\n")
        print(f'\n\tAccount Type : {self.type}')
        print(f'\tName : {self.name}')
        print(f'\tEmail id: {self.email}')
        print(f'\tAddress: {self.address}')
        print(f'\tAccount No : {self.accountNo}')
        print(f'\tCurrent Balance : {self.balance}\n')

class Bank(Account):
    totalbalance = 0
    total_loanammount=0
          
        
    def offloan_onloan(self,cmd):
        if cmd=='off':
            Account.loan=False
        elif cmd=='on':
            Account.loan=True
    def show_users():
        for acc in Account.accounts:
            print("name:",acc.name,"-->","accNo:",acc.accountNo,"& type:",acc.type,"\n")

    def delete_account(self, account_number):
        for account in Account.accounts:
            if account.accountNo == account_number:
                Account.accounts.remove(account)

    
               
  

# Main program

currentUser=None

while(True):
    if currentUser==None:
        
        print("\n--> No user logged in !")
        ch=input("\n--> Register/Login (R/L/A) : ")
        if ch=="R":
            
            name=input("Name:")
            email=input("Email id:")
            address=input("Address:")
            no=int(input("Ender Acc no: "))
            pa=input("Password:")
            a=input("Savings Account or special Account (sv/cur) :")
            if a=="sv":
                print("\t Interest rate is 7%")
                currentUser=SavingsAccount(name,email,address,no,pa)

            elif a=="cur":
                    lm=int(input("Overdraft Limit:"))
                    currentUser=CurrentAccount(name,email,address,no,pa,lm)
            else:
                print("vul leikho na lav nai")

        elif ch=="A":
            print("1. Creat account")
            print("2. Delete account")
            print("3. Show Account list")
            print("4. Total Bank Balance")
            print("5. Total applied loan amounnt")
            print("6. CAN Off or On loan")
            print("7. Logout\n")
            
            op=int(input("Chhose Option:"))
            if op==1:
                name=input("Name:")
                email=input("Email id:")
                address=input("Address:")
                no=int(input("Ender Acc no: "))
                pa=input("Password:")
                a=input("Savings Account or special Account (sv/cur) :")
                if a=="sv":
                    print("\t Interest rate is 7%")
                    currentUser=SavingsAccount(name,email,address,no,pa)

                elif a=="cur":
                    lm=int(input("Overdraft Limit:"))
                    currentUser=CurrentAccount(name,email,address,no,pa,lm)
                else:
                    print("vul leikho na lav nai")
                
            elif op==2:
                accno=int(input("Enter account number:"))
                Bank.delete_account('',accno)

            elif op==3:
                Bank.show_users()
            elif op==4:
                print("\n '-' negative indicates that bank is on debt that means ''loan chaiyen na !!!''")
                print(Bank.totalbalance)

            elif op==5:
                print(Bank.total_loanammount)

            elif op==6:
                ch=input('Type "on" or "off" :')
                Bank.offloan_onloan('',ch)

            elif op==7:
                currentUser=None
                

        elif ch=="L":
            no=int(input("Account Number:"))
            for account in Account.accounts:
                if no== account.accountNo:
                    currentUser=account
                    break
    
        else:
            print("thik moto type koro -_-")
            break
                
    else:
        print(f"\nWelcome {currentUser.name} !\n")
        
        if currentUser.type=="savings":
            
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show Info")
            print("4. change Info")
            print("5. Apply Interset")
            print("6. Avaiable Balance")
            print("7.Transaction History")
            print('8.Transfer amount')
            print("9. Check Loan Eligibility")
            print("10. Logout\n")
            
            op=int(input("Chhose Option:"))
            
            if op==1:
                amount=int(input("Enter withdraw amount:"))
                currentUser.withdraw(amount)
                
            elif op==2:
                amount=int(input("Enter deposit amount:"))
                currentUser.deposit(amount)
            
            elif op==3:
                currentUser.showInfo()
            
            elif op==4:
                name=input("Name:")
                email=input("Email id:")
                address=input("Address:")
                pa=input("Password:")
                currentUser.changeInfo(name,email,address,pa)

            
            elif op==5:
                currentUser.apply_interest()
            
            elif op==6:
                currentUser.show_available_balance()

            elif op==7:
                print(Account.transaction_history)

            elif op==8:
                frm=int(input('Enter sender acc no:'))
                to=int(input('Enter receiver acc no:'))
                amo=int(input("Enter amount: "))
                for account in Account.accounts:
                    if account.accountNo !=frm or account.accountNo!=to and amo>currentUser.balance:
                        print("Account does not exist")

                    else:
                        currentUser.transfer_amount(amo,frm,to)
            elif op==9:
                amount=int(input("enter loan amount: "))
                currentUser.applyLoan(amount)

            elif op==10:
                currentUser=None

            else:
                print("Invalid Option")
        
        else:
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show Info")
            print("4. change Info")
            print("5. Available Balance")
            print("6. Transactions History")
            print("7.Transfer amount")
            print("8. Check Loan Eligibility")
            print("9. Logout\n")
            
            
            op=int(input("Choose Option:"))
            
            if op==1:
                amount=int(input("Enter withdraw amount:"))
                currentUser.withdraw(amount)
                
            elif op==2:
                amount=int(input("Enter deposit amount:"))
                currentUser.deposit(amount)
            
            elif op==3:
                currentUser.showInfo()
                # print(currentUser.accounts)
            
            elif op==4:
                name=input("Name:")
                email=input("Email id:")
                address=input("Address:")
                pa=input("Password:")
                currentUser.changeInfo(name,email,address,pa)
            
            elif op==5:
                currentUser.show_available_balance()

            elif op==6:
                print(Account.transaction_history)

            elif op==7:
                frm=int(input('Enter sender acc no:'))
                to=int(input('Enter receiver acc no:'))
                amo=int(input("Enter amoun: "))
                for account in Account.accounts:
                    if account.accountNo !=frm or account.accountNo!=to:
                        print("/n Account does not exist")
                    elif amo>currentUser.balance:
                        print('/n amount is larger than balance')

                    else:
                        currentUser.transfer_amount(amo,frm,to)

            elif op==8:
                amount=int(input("Enter loan amount: "))
                currentUser.applyLoan(amount)

            elif op==9:
                currentUser=None
            
            else:
                print("Invalid Option")