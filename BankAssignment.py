# Program Title: Bank system
# Program description: This program is a bank system which allows the user to create a checking and savings account.
# It enables them to withdraw, deposit, transfer, check transaction history and account information.
# Author: Harry O'Donnell
# Date 17/12/21
# NOTE: you will need to chnage the file path to compile, it's using my file


#used to get the current date.
from datetime import datetime
#Used to generate random IBAN's, transactions ID's and account numbers
import random as r

class BankAccount(object):
    """
        This class is the super class which is inherited by checking and savings account classes.
    """

    def __init__(self,account_number,IBAN ,funds, transactions=None):
        """ Used to initialise the variables in the super class...
            :args:
                :account_number: account number is a unique identifier for each user (customer)
                :IBAN: The ID for each bank account (checking) or (Saving), also unique
                :funds: The money in the account, has to be set prior to opening an acccount, (opening balance)
                :transactions = None: Is a list of all the transactions, initially set to none. There isn't any transactions passed into the class.
        
        """
        #private variables as information is sensitive, creating using preceeding double underscore.
        # These variables (apart from transactions) cannot be accessed by non subclasses without the getter and setter methods.
        self.__account_number = account_number
        self.__IBAN = IBAN
        self.__funds = funds
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions

    #Found infromation on getter and setter using DataCamp https://www.datacamp.com/community/tutorials/property-getters-setters
    #used so that other classes (Custiomer) can access the information.
    
    def get_account_number(self):
        """ 
        :returns: 
            :int: returning value randomly genertaed by random library.
        """
        return self.__account_number
    def get_IBAN(self):
        """ 
        :returns: 
            :str: returning string IBAN randomly genertaed by random library.
        """
        return self.__IBAN
    def get_funds(self):
        """ 
        :returns: 
            :int: returning balance in account randomly genertaed by random library.
        """
        return self.__funds
  #  def get_transactions(self):
  #      return self.transactions
    

    # create setter method to set private variables with prefix 'set'
    # Way of accessing private variables from outside the method
    def set_account_number(self, account_number):
        """ 
        :args: 
            :account_number(int): Unique account number for each user
        """
        self.__account_number = account_number

    def set_IBAN(self,IBAN):
        """ 
        :args: 
            :IBAN(str): Unique IBAN for each account (savings / checking)
        """
        self.__IBAN = IBAN

    def set_funds(self, funds):
        """ 
        :args: 
            :funds(int): The balance in the account.
        """
        self.__funds = funds

   # def set_transactions(self, transactions):
      #  self.transactions = transactions

    # Withdraw method, purpose is for the user to withdraw money from whatever account they desire.
    # Amount is passed into the withdraw account because the subclasses have different overdraft limits.
    def withdraw(self,amount):
        """
        :args:
            :amount(int): This is the amount the user wishes to withdraw from their selected account. The amount parameter is passed from the main. 
        :return:
            :False: If amount entered is less than or equal to zero, False will be returned, you must return a positive amount.
            :self.__funds: Funds will be returned once the file balance has been updated. 
        """
        # If amount entered is less than or equal to zero, error message outputed and false returned.
        if amount <= 0:
            print("You can only withdraw a positive value")
            return False
        # Otherwise, execute the rest of the code.
        else:
            # Put the balance of that object instance into a varibale 'old_funds'
            old_funds = self.__funds

            # Appends the transaction to the transactions variable at that instance (self.transactions), the appended variable (transaction) 
            # puts the amount and the type of operation into (self.transactions).
            transaction = ("Withdraw", amount)
            self.transactions.append(transaction)

            # The funds at that instance are being subtracted by the amount being withdrawn (amount)
            # That updated balance is then put into a variable (update_funds)
            self.__funds -= amount
            update_funds = self.__funds
            
            # This is operation opens the account.txt file, which stores all the accounts.
            # It iterates through each line, strips each word, and replaces the old funds value (old_funds) with the updated one (update_funds)
            
            
            with open('accounts.txt', 'r') as f:
                new_file_content = ""
                for line in f:
                    stripped_line = line.strip()
                    new_line = stripped_line.replace(str(old_funds), str(update_funds))
                    new_line += "\n"
                    new_file_content += new_line
                f.close()

                # The variable that is assigned to (new_file_content) is then written into the account.txt file, that new line is completely replaced.
                writing_file = open("accounts.txt", "w")
                writing_file.write(new_file_content)
                writing_file.close()
                return self.__funds
                

     #depost method
    def deposit(self):
        """ 
        :return:
            :False: If amount entered is less than or equal to zero, False will be returned, you must return a positive amount.
            :self.__funds: Funds will be returned once the file balance has been updated. 
        """
        # The amount the user wants the deposit into their chosen acccount as an integer is prompted.
        amount = int(input('Enter The Amount To Be Deposit : '))
        # If amount entered is less than or equal to zero, error message outputed and false returned.
       # amount = float(amount)
        if amount <= 0:
            print("You can only deposit a positive value")
            return False
        
        else:
            # Put the balance of that object instance into a varibale 'old_funds'
            old_funds = self.__funds

            # Appends the transaction to the transactions variable at that instance (self.transactions), the appended variable (transaction) 
            # puts the amount and the type of operation into (self.transactions).
            transaction = ("Deposit", amount)
            self.transactions.append(transaction)

            # The funds at that instance are being added to the amount being deposited (amount)
            # That updated balance is then put into a variable (update_funds)
            self.__funds += amount
            update_funds = self.__funds

            # This is operation opens the account.txt file, which stores all the accounts.
            # It iterates through each line, strips each word, and replaces the old funds value (old_funds) with the updated one (update_funds)
            with open('accounts.txt', 'r') as f:
                new_file_content = ""
                for line in f:
                    stripped_line = line.strip()
                    new_line = stripped_line.replace(str(old_funds), str(update_funds))
                    new_line += "\n"
                    new_file_content += new_line
                f.close()

                # The variable that is assigned to (new_file_content) is then written into the account.txt file, that new line is completely replaced.
                writing_file = open("accounts.txt", "w")    
                writing_file.write(new_file_content)
                writing_file.close()
                return self.__funds
        
    # This method allows the user to check the balance of their accounts.
    def available_funds(self): 
        """ 
        :return:
            :self.__funds: Funds will be returned once the balance has been displayed.
        """
        print('-------------------------------------------')
        print("Available funds:€{}".format(self.__funds))
        print('-------------------------------------------')

        return self.__funds

    # The transfer method allows the user to select one of their accounts and pick the account to transfer the money to by inputting their IBAN, the account unique identifier
    def transfer(self):
        """ 
        :return:
            :False: If amount entered is less than or equal to zero, False will be returned, you must return a positive amount.
            :self.__funds: Funds will be returned once the file balance has been updated. 
        """

        # The amount the user wants the deposit into their chosen acccount as an integer is prompted.
        amount = int(input('Enter The Amount To Be Transferred : '))
        
        # The user enters the IBAN that they want to make the transfer.
        receive_iban = input("Enter the receivers IBAN\n")

        # If amount entered is less than or equal to zero, error message outputed and false returned.
        if amount <= 0:
            print("You can only withdraw a positive value")
            return False

        # If the users balance in the selected account is greater than the amount they wish to transfer, then execute the code inside
        if self.__funds >= amount:
            # Put the balance of that object instance into a varibale 'old_funds'
            old_funds = self.__funds

            # Appends the transaction to the transactions variable at that instance (self.transactions), the appended variable (transaction) 
            # puts the amount and the type of operation into (self.transactions).
            transaction = ("transfer", amount)
            self.transactions.append(transaction)

            # The funds at that instance are being subtracted by the amount being transferred (amount)
            # That updated balance is then put into a variable (update_funds)
            self.__funds -= amount
            update_funds = self.__funds

            # This is operation opens the account.txt file, which stores all the accounts.
            # It iterates through each line, strips each word, and replaces the old funds value (old_funds) with the updated one (update_funds)
            with open('accounts.txt', 'r') as f:
                new_file_content = ""
                for line in f:
                    stripped_line = line.strip()
                    new_line = stripped_line.replace(str(old_funds), str(update_funds))
                    new_line += "\n"
                    new_file_content += new_line
                f.close()

                # The variable that is assigned to (new_file_content) is then written into the account.txt file, that new line is completely replaced.
                writing_file = open("accounts.txt", "w")    
                writing_file.write(new_file_content)
                writing_file.close()

            # This is operation opens the account.txt file, which stores all the accounts.
            with open('accounts.txt') as f:
                datafile = f.readlines()
                for line2 in datafile:
                    # Check if the inputted IBAN that's receiving the money is a line in the accounts file. If so execute the code.
                    if receive_iban in line2:
                        # On the line that contains the inputted IBAN (line2), find the funds by slicing
                        # It will be found between ' | funds:€' and '|end', the file funds avribale will contain the balance of the receiver.
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        # This converts it to an integer
                        file_funds = int(file_funds)
                                    
                        # Put the balance of that object instance into a varibale 'old_funds'
                        old_funds = file_funds
                        # The funds at that instance are being added to the amount being transferred (amount)
                        file_funds += amount

                        # This is operation opens the account.txt file and reads it, this is the file that stores all the accounts. 
                        # It iterates through each line, strips each word, and replaces the old funds value (old_funds) with the updated one (update_funds)
                        with open('accounts.txt', 'r') as f:
                            new_file_content = ""
                            for line in f:
                                stripped_line = line.strip()
                                new_line = stripped_line.replace(str(old_funds), str(file_funds))
                                new_line += "\n"
                                new_file_content += new_line
                            f.close()
                            # The variable that is assigned to (new_file_content) is then written into the account.txt file, that new line is completely replaced.
                            writing_file = open("accounts.txt", "w")    
                            writing_file.write(new_file_content)
                            writing_file.close()
                            return self.__funds

        # If the users balance in the selected account is less than the amount they wish to transfer, then print an error message and return False
        else:
            print("Insufficient funds in your account")
            return False

    #This transaction method outputs all the transactions by a selected account
    def transactionsmethod(self, file="/Users/harryodonnell/Documents/OOP/Python/BankSystem/AccountTransactions.txt"):
        """ 
        :args: 
            :file: The account transactions file is passed into the method 
        :return:
            :result: If amount entered is less than or equal to zero, False will be returned, you must return a positive amount.
            :self.__funds: Funds will be returned once the file balance has been updated. 
        """

        result = "" 
        trans_start = "TRX-#"
        last = len(self.transactions)
        first = last - 5
        if first < 0:
            first = 0

        if last == 0:
            return result

        for index in range(last, first, -1):
            result += (trans_start+str(r.randint(10000,19999))+ ":"+"  IBAN: " + self.__IBAN + " Type: " + self.transactions[index-1][0] + ". Amount: " + str(self.transactions[index-1][1]) + "\n")
        f = open(file, "a")
        f.write(result)
        f.close()
        return result

    #The user can create a new account and appened it to the account.txt file
    def add_account(self, file="/Users/harryodonnell/Documents/OOP/Python/BankSystem/accounts.txt"):
        """ 
        :args: 
            :file: The account transactions file is passed into the method 
        """
        #open the file and append the account into the file.
        f = open(file, "a")
        customer_account = "#{} | IBAN:{} | funds:€{}|end".format(self.__account_number,self.__IBAN,self.__funds)
        f.write(customer_account)
        f.close()
    

    def delete_account(self, checking):
        """ 
        :args: 
            :checking:(str) argument which passes the string to differentiate between the checking and savings acount
        """
        customer_account = checking + "#{} | IBAN:{} | funds:€{}|end".format(self.__account_number,self.__IBAN,self.__funds)
        print(customer_account)
        print(" -- Account Deleted --")
        # It reads the file and iterates through the lines in the account file.
        #
        # It re-writes all the lines back into the file apart from the selected one that will be removed 
        with open('accounts.txt', 'r') as f:
            lines = f.readlines()
            f.close()
            writing_file = open("accounts.txt", "w") 
            for line in lines:
                if line.strip("\n") != customer_account:
                    writing_file.write(line)
            writing_file.close()
            

     # create __str__ method to print Account details
    def __str__(self):
        print("Account Number:{}\nBalance: {} \nIBAN: {}\n ".format(self.__account_number, self.__funds, self.__IBAN))
 

class SavingsAccount(BankAccount):
    """ 
       This class is a subclass of BankAccount and inherits BnakAccount.
    """
    # Used to initialise the parameters 
    def __init__(self, account_number, IBAN,funds, transactions=None):
        """
        :args: 
            :account_number: (int) The account number is directly inherited from the super class BankAccount
            :IBAN: (str) The IBAN is directly inherited from the super class BankAccount
            :funds: (int) The funds is directly inherited from the super class BankAccount, they will be the funds in the savings account
            :transactions:(str) The transactions are directly inherited from the super class BankAccount
        """
        super().__init__(account_number, IBAN, funds,transactions)

    def withdraw(self,amount):
        """ 
            It inherits the main structure from the super class BankAccount, except it prevents the savings account from having an overdraft
            :args:
                amount:(int) This is passed in from the main, the amount that will be withdrawn
            :return: 
                False: return falase if the funds goes below zero
        """
        # It gets the funds at that instance using the getter method get_funds()
        # if it's less than zero it will display an error message
        if super().get_funds() - amount < 0:
            print("Insufficient funds available")
            print("Cannot run svaings account into overdraft")
            return False
        # goes into the super class withdraw and passes variable amount
        super().withdraw(amount)
        
        
    def deposit(self):
        """ 
            It inherits the same structure and operations as the super class BankAccount
        """
        super().deposit()

    def delete_account(self,checking):
        """ 
            It inherits the same structure and operations as the super class BankAccount
            :args:
                checking:(str) this variable is used to extract the account from the account file 
        """
        super().delete_account(checking)

    def transfer(self):
        """ 
            It inherits the same structure and operations as the super class BankAccount
        """
        super().transfer()

    def transactionsmethod(self):
        """ 
            It inherits the same structure and operations as the super class BankAccount
        """
        super().transactionsmethod()

    def add_account(self,file="/Users/harryodonnell/Documents/OOP/Python/BankSystem/accounts.txt"):
        """ 
            It inherits the same structure and operations as the super class BankAccount
            :args:
                file:(file) this arg is used to pass the file to the method.
        """
        super().add_account(file)

    def __str__(self):
        """ 
            It inherits the same structure and operations as the super class BankAccount
            :return: 
                super().__str__(): returns the outputted account information from the super class.
        """   
        return super().__str__() 
            
            

    
class CheckingAccount(BankAccount):
    """ 
       This class is a subclass of BankAccount and inherits BnakAccount.
    """
    def __init__(self, account_number, IBAN,funds,transactions=None):
        """
        :args: 
            :account_number: (int) The account number is directly inherited from the super class BankAccount
            :IBAN: (str) The IBAN is directly inherited from the super class BankAccount
            :funds: (int) The funds is directly inherited from the super class BankAccount, they will be the funds in the savings account
            :transactions:(str) The transactions are directly inherited from the super class BankAccount
        """
        super().__init__(account_number, IBAN, funds,transactions)

    # create withdraw method
    def withdraw(self,amount):
        """ 
            It inherits the main structure from the super class BankAccount, except it prevents the cheking accounts overdraft from exceeding €1000
            :args:
                amount:(int) This is passed in from the main, the amount that will be withdrawn
            :return: 
                False: return falase if the funds goes below zero
        """
        # €1000 overdraft on the checking account
        # It gets the funds at that instance using the getter method get_funds()
        # if it's less than zero it will display an error message
        if super().get_funds() - amount < -1000:
            print("Insufficient funds available")
            print("You have ran out of your €1000 overdraft")
            return
        # goes into the super class withdraw and passes variable amount
        super().withdraw(amount)
        

    def deposit(self):
        """ 
            It inherits the same structure and operations as the super class BankAccount
        """
        super().deposit()
       
    def delete_account(self, checking):
        """ 
            It inherits the same structure and operations as the super class BankAccount
            :args:
                checking:(str) this variable is used to extract the account from the account file 
        """
        super().delete_account(checking)

    def transfer(self):
        """ 
            It inherits the same structure and operations as the super class BankAccount
        """
        super().transfer()

    def transactionsmethod(self):
        """ 
            It inherits the same structure and operations as the super class BankAccount
        """
        super().transactionsmethod()
        
    def add_account(self,file="/Users/harryodonnell/Documents/OOP/Python/BankSystem/accounts.txt"):
        """ 
            It inherits the same structure and operations as the super class BankAccount
            :args:
                file:(file) this arg is used to pass the file to the method.
        """
        super().add_account(file)


    def __str__(self):   
        """ 
            It inherits the same structure and operations as the super class BankAccount
            :return: 
                super().__str__(): returns the outputted account information from the super class.
        """   
        return super().__str__()

class Customer(object):
    """ 
       This class contains all the inforamtion about the customer
    """
    def __init__(self, firstname, lastname, address, DOB):
        """ Used to initialise the variables in the customer class
            :args:
                :firstname: The first name of the user is entered 
                :lastname: The last name of the user is entered 
                :address: The user enters their address
                :DOB: Enter the Date of birth in ther format (YYYY-MM-DD)
        """
        #private variables as information is sensitive, creating using preceeding double underscore.
        # These variables (apart from transactions) cannot be accessed by non subclasses without the getter and setter methods.
        self.__firstname = firstname
        self.__lastname = lastname
        self.__address = address
        self.__DOB = datetime.strptime(DOB, '%Y-%m-%d')
        self.__accounts = []
    # create getter methods 
    #used so that other classes can access the information.
    def get_firstname(self):
        return self.__firstname
    def get_lastname(self):
        return self.__lastname
    def get_address(self):
        return self.__address
    def get_DOB(self):
        return self.__DOB
 
    # create setter methods for name, address, phone_number, customer_id
    def set_firstname(self, firstname):
        self.__firstname = firstname
    def set_lastname(self, lastname):
        self.__lastname = lastname
    def set_address(self, address):
        self.__address = address
    def set_DOB(self, DOB):
        self.__DOB = DOB

    #The method to calculate the customers age using the current time
    def cust_age(self):
        """
            This method calculates trhe age by subatrcting the current date from their date of birth
            return:
                age (str): The age is returned once it has been calculated
        """
        # make today the current date/time
        today = datetime.today()
        
        # if born after the current date then return 
        if self.__DOB > today:
            return today.year - self.__DOB.year - 1
        # else return the age of the customer formatted
        else:
            age = today.year - self.__DOB.year
            return "Age: "'{}'.format(today.year - self.__DOB.year)
           

    def fullname(self):
        """
            This method creates the full name of the customer by formattting first and last name
                return:
                fullname (str): one formatted the string will be returned
        """
        return '{} {}'.format(self.__firstname, self.__lastname)

    # this method will create the account
    def Create_Account(self, account):
        """
            This method appends the account to the accounts variable to create a new account
        """
        self.__accounts.append(account)

    # getters method
    def get_Account(self, account_number):
        """
            This method adds the account to thes account list and appedns the customer details to the customer file
                args: file (file) : customer file passed into the method

                return:
                    customer details (str): one formatted the string will be returned
        """
        for account in self.__accounts:
            if account.get_Account()== account_number:
                return account
        return None

    def __str__(self, file="/Users/harryodonnell/Documents/OOP/Python/BankSystem/customer.txt"):
        """
            This method adds the account to thes account list and appedns the customer details to the customer file
                args: file (file) : customer file passed into the method

                return:
                    customer details (str): one formatted the string will be returned
        """
        account_str = ""
        for account in self.__accounts:
            account_str += str(account)
        f = open(file, "a")
        customer_account = "\nCustomer Details:  Name:{} {} Address:{} Accounts:{}".format(self.fullname(), self.cust_age(), self.__address, account_str)
        f.write(customer_account)
        f.close()
        return "\nCustomer Details:\n\nName: {}\nAge: {} \nAddress: {} \nAccounts: {}".format(self.fullname(), self.cust_age(), self.__address, account_str)


def main():
    #The user isasked whether they are a new customer
    print('!-------------Welcome To The Harry ODonnells Bank-------------!')
    select = input("Are you a new customer? (Yes/No)")
    # makes the input lowercase
    select = select.lower()
    # If answered yes, enter the if statement
    if select == 'yes' :
        #User enters their personal information
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        address = input("Enter your address: ")
        DOB = input("what is your date of birth (YYYY-MM-DD): ")
        #object first_cust created, the inputted values will be passed into the class as parameters
        first_cust = Customer(firstname, lastname, address, DOB)
        #Cretaing an account for the customer, an 9 didgit unique account number is created
        first_cust.Create_Account(r.randint(100000000,199999999))
        #print the users personal information
        print(first_cust.__str__())

    #if the user inputs 'no'
    if select == 'no':
        # prompts user to enter their 9 digit account number
        numid = input('\n\nEnter Your account number : ')

        # Retrieving the customer and acccount info of that customer from the files
        with open('customer.txt') as f:
            datafile = f.readlines()
        for line in datafile:
            # This breakes out of the for loop and into the menu when the account number is found   
            if numid in line:
                break

        # This catches all invalid account number input, numid must be 9 digits and must be in the customer file.    
        if len(numid) != 9 or numid not in line:
            print("Invalid Account Number!!")
            return False

        # Choice referenced
        choice = ''
        #if the user enter 10 the program will end, otherwise it will consistently loop
        #Displayed menu table
        while choice != 9:
            print('---------------------------------------------------------------------------')
            print('\n What Do You Want To Do ???\n ')
            print('Select one of the options...\n')
            print('1. Open a checking account\n')
            print('2. Open a saving account\n')
            print('3. WithDraw Money\n')
            print('4. Deposit Money\n')
            print('5. Check recent transactions\n')
            print('6. Check balance\n')
            print('7. Transfer to a new account\n')
            print('8. Delete an account\n')
            print('9. Exit Program\n')
            print('---------------------------------------------------------------------------')
            #Prompts the user to choose what to do 
            choice = int(input('\nPlease Enter Number Corresponding To Your Choice : '))
            #if the user enters 1, this will open a checking account
            if choice == 1:
                #open the customer file, and read all the lines.
                with open('customer.txt') as f:
                        datafile = f.readlines()
                        for line2 in datafile:
                            #find the account number by slicing between the start and end points
                            start = line2.find("Accounts:") + len("Accounts:")
                            end = line2.find(" |")
                            # assign the account number to the variable account_file_num
                            account_file_num = line2[start:end]
                            # if that account number is in the file and numid (previously entered by the user) is equal to the account_file_num, execute if statement
                            if account_file_num in line2 and numid == account_file_num:
                                #display that line it was found
                                print(line2)
                                #Again using slicing to extarct the age of the user from the file.
                                start = line2.find("Age: ") + len("Age: ")
                                end = line2.find(" Address:")
                                age_file = line2[start:end]
                                # converting the file variable into an integer for a comparison
                                age_file =int(age_file)
                                # if the age is less than 18, you cannot make a checking account 
                                # Error messgae will be displayed 
                                # false returned 
                                if age_file < 18:
                                    print("You are not old enough yet to create a checking account!")
                                    print("Start off witha savings account!!")
                                    return False
                #open the accounts file and write account_type into it
                account_type = "\nChecking Account: "
                file = "/Users/harryodonnell/Documents/OOP/Python/BankSystem/accounts.txt"
                f = open(file, "a")
                f.write(account_type)
                f.close()
                #Creates the IBAN for the new checking account, preceding iban_start and then a random number.
                iban_start = "AIBKIE"
                IBAN = iban_start+str(r.randint(100000000,199999999))
                #Prompts user for account opening balance
                funds = int(input("How much would you like to open your account with?"))
                # create object (obj) and create a checking account 
                obj = CheckingAccount(numid,IBAN,funds)
                #Goes to the account in BankAccount class and then to the CheckingAccount class and adds an account
                obj.add_account()

            #if the user enters 2, this will open a Savings account
            elif choice == 2:
                #open the customer file, and read all the lines.
                with open('customer.txt') as f:
                        datafile = f.readlines()
                        for line2 in datafile:
                            #find the account number by slicing between the start and end points
                            start = line2.find("Accounts:") + len("Accounts:")
                            end = line2.find(" |")
                            # assign the account number to the variable account_file_num
                            account_file_num = line2[start:end]
                            # if that account number is in the file and numid (previously entered by the user) is equal to the account_file_num, execute if statement
                            if account_file_num in line2 and numid == account_file_num:
                                #display that line it was found
                                print(line2)
                                #Again using slicing to extarct the age of the user from the file.
                                start = line2.find("Age: ") + len("Age: ")
                                end = line2.find(" Address:")
                                age_file = line2[start:end]
                                # converting the file variable into an integer for a comparison
                                age_file = int(age_file)
                                # if the age is less than 14, you cannot make a savings account as specified in the objectives
                                # Error messgae will be displayed 
                                # false returned
                                if age_file < 14:
                                    print("You are not old enough yet to create a Savings account!")
                                    return False

                # open the accounts file and write account_type into it
                account_type = "\nSavings Account: "
                file = "/Users/harryodonnell/Documents/OOP/Python/BankSystem/accounts.txt"
                f = open(file, "a")
                f.write(account_type)
                f.close()
                #Creates the IBAN for the new savings account, preceding iban_start and then a random number.
                iban_start = "AIBKIE"
                IBAN = iban_start+str(r.randint(100000000,199999999))
                #Prompts user for account opening balance
                funds = int(input("How much would you like to open your account with?"))
                # create object (obj) and create a checking account 
                obj = SavingsAccount(numid,IBAN,funds)
                #Goes to the account in BankAccount class and then to the CheckingAccount class and adds an account
                obj.add_account()

            elif choice == 3:
                # Prompts the user for which account they would like to operate with
                print("Choose which acount type you would like to withdraw from\n")
                print('\nPlease Enter Number Corresponding To Your Choice : ')
                select = int(input("1) Checking Account | 2) Savings Account \n"))
                # 1 is selected, so the cheking account will be used
                if select == 1:
                    #open the accounts file, and read all the lines.
                    with open('accounts.txt') as f:
                        datafile = f.readlines()
                    #iterates through the lines
                    for line2 in datafile:
                        #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside file_IBAN
                        start = line2.find("| IBAN:") + len("| IBAN:")
                        end = line2.find(" | funds:")
                        file_IBAN = line2[start:end]
                        #Using slicing to find the account number, which is located between the start3 and end3 variables the string returned is put inside file_acc_num
                        start3 = line2.find("Checking Account: #") + len("Checking Account: #")
                        end3 = line2.find(" | IBAN:")
                        file_acc_num = line2[start3:end3]
                        #Using slicing to find the balance, which is located between the start and end variables the string returned is put inside file_funds
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        # If the inputted account number (numid is equal to the the account number that was retrieved from the file and the string checking account is also in the line. Enter the if statement
                        if numid == file_acc_num and "Checking Account" in line2:
                            #create the object for checking account using the retrived variables
                            obj = CheckingAccount(numid,file_IBAN,int(file_funds))
                            #Enter the amount that will be withdrawn
                            amount = int(input('Enter The Amount To Be WithDraw : '))
                            #the previously created object will enter the withdraw method in the class checkingAccount, it will also pass the arg amount.
                            obj.withdraw(amount)
                            #the previously created object will enter the transaction method in the class checkingAccount, creates a transaction
                            obj.transactionsmethod()
                            #The object is outputted 
                            obj.__str__()
                            break
                            
                # 2 is selected, so the savings account will be used
                elif select == 2:
                    #open the accounts file, and read all the lines.
                    with open('accounts.txt') as f:
                        datafile = f.readlines()
                    #iterates through the lines
                    for line2 in datafile:
                        #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside file_IBAN
                        start = line2.find("| IBAN:") + len("| IBAN:")
                        end = line2.find(" | funds:")
                        file_IBAN = line2[start:end]
                        #Using slicing to find the balance, which is located between the start and end variables the string returned is put inside file_funds
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        #Using slicing to find the account number, which is located between the start3 and end3 variables the string returned is put inside file_acc_num
                        start3 = line2.find("Savings Account: #") + len("Savings Account: #")
                        end3 = line2.find(" | IBAN:")
                        file_acc_num = line2[start3:end3] 
                        # If the inputted account number (numid is equal to the the account number that was retrieved from the file and the string savings account is also in the line. Enter the if statement
                        if numid == file_acc_num and "Savings Account" in line2:
                            #create the object for savings account using the retrived variables
                            obj = SavingsAccount(numid,file_IBAN,int(file_funds)) #choose which account to withdraw from saving/checking
                            #Enter the amount that will be withdrawn
                            amount = int(input('Enter The Amount To Be WithDraw : '))
                            #the previously created object will enter the withdraw method in the class checkingAccount, it will also pass the arg amount.
                            obj.withdraw(amount)
                            #the previously created object will enter the transaction method in the class checkingAccount, creates a transaction
                            obj.transactionsmethod()
                            #The object is outputted 
                            obj.__str__()
                            break
                #Error checking
                else:
                    print("Must enter option 1 or 2")

                                
            #If 4 is entered, deposit..
            elif choice == 4:
                # Prompts the user for which account they would like to operate with
                print("Choose which acount type ypu would like to deposit into\n")
                print('\nPlease Enter Number Corresponding To Your Choice : ')
                select = int(input("1) Checking Account | 2) Savings Account \n"))                              
                # 1 is selected, so the cheking account will be used
                if select == 1:
                    
                   #open the accounts file, and read all the lines.
                    with open('accounts.txt') as f:
                        datafile = f.readlines()
                    #iterates through the lines
                    for line2 in datafile:
                        #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside file_IBAN
                        start = line2.find("| IBAN:") + len("| IBAN:")
                        end = line2.find(" | funds:")
                        file_IBAN = line2[start:end]
                        #Using slicing to find the account number, which is located between the start3 and end3 variables the string returned is put inside file_acc_num
                        start3 = line2.find("Checking Account: #") + len("Checking Account: #")
                        end3 = line2.find(" | IBAN:")
                        file_acc_num = line2[start3:end3]
                        #Using slicing to find the balance, which is located between the start and end variables the string returned is put inside file_funds
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        # If the inputted account number (numid is equal to the the account number that was retrieved from the file and the string checking account is also in the line. Enter the if statement
                        if numid == file_acc_num and "Checking Account" in line2:
                            #create the object for checking account using the retrived variables
                            obj = CheckingAccount(numid,file_IBAN,int(file_funds))
                            #the previously created object will enter the deposit method in the class checkingAccount
                            obj.deposit()
                            #the previously created object will enter the transaction method in the class checkingAccount, creates a transaction
                            obj.transactionsmethod()
                            #The object is outputted 
                            obj.__str__()
                            break
                            
                      
                # 2 is selected, so the savings account will be used
                elif select == 2:
                    #open the accounts file, and read all the lines.
                    with open('accounts.txt') as f:
                        datafile = f.readlines()
                    #iterates through the lines
                    for line2 in datafile:
                        #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside file_IBAN
                        start = line2.find("| IBAN:") + len("| IBAN:")
                        end = line2.find(" | funds:")
                        file_IBAN = line2[start:end]
                        #Using slicing to find the balance, which is located between the start and end variables the string returned is put inside file_funds
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        #Using slicing to find the account number, which is located between the start3 and end3 variables the string returned is put inside file_acc_num
                        start3 = line2.find("Savings Account: #") + len("Savings Account: #")
                        end3 = line2.find(" | IBAN:")
                        file_acc_num = line2[start3:end3] 
                        # If the inputted account number (numid is equal to the the account number that was retrieved from the file and the string savings account is also in the line. Enter the if statement
                        if numid == file_acc_num and "Savings Account" in line2:
                            #create the object for savings account using the retrived variables
                            obj = SavingsAccount(numid,file_IBAN,int(file_funds)) #choose which account to withdraw from saving/checking
                            #the previously created object will enter the deposit method in the class checkingAccount, it will also pass the arg amount.
                            obj.deposit()
                            #the previously created object will enter the transaction method in the class checkingAccount, creates a transaction
                            obj.transactionsmethod()
                            #The object is outputted 
                            obj.__str__()
                            break

                #Error checking
                else:
                    print("Must enter option 1 or 2")

            #Displays all the transactions by that users account
            elif choice == 5:
                # Prompts the user for which account they would like to operate with
                print("Choose which acount type ypu would like to see the transactions\n")
                print('\nPlease Enter Number Corresponding To Your Choice : ')
                select = int(input("1) Checking Account | 2) Savings Account \n"))
                if select == 1:  
                    #open the accounts file, and read all the lines.
                    with open('accounts.txt') as f:
                        datafile = f.readlines()
                    #iterates through the lines
                    for line2 in datafile:
                        #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside file_IBAN
                        start = line2.find("| IBAN:") + len("| IBAN:")
                        end = line2.find(" | funds:")
                        file_IBAN = line2[start:end]
                        #Using slicing to find the account number, which is located between the start3 and end3 variables the string returned is put inside file_acc_num
                        start3 = line2.find("Checking Account: #") + len("Checking Account: #")
                        end3 = line2.find(" | IBAN:")
                        file_acc_num = line2[start3:end3]
                        #Using slicing to find the balance, which is located between the start and end variables the string returned is put inside file_funds
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        # If the inputted account number (numid is equal to the the account number that was retrieved from the file and the string checking account is also in the line. Enter the if statement
                        if numid == file_acc_num and "Checking Account" in line2:
                            #create the object for checking account using the retrived variables
                            obj = CheckingAccount(numid,file_IBAN,int(file_funds))
                            #open the accounts file, and read all the lines.
                            with open('AccountTransactions.txt') as f:
                                datafile = f.readlines()
                            #iterates through the lines
                            for line in datafile:
                                #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside trans_IBAN, this is found inside the transactions account
                                start = line.find("IBAN: ") + len("IBAN: ")
                                end = line.find(" Type:")
                                trans_IBAN = line[start:end] 
                                #If the Iban from the account is equal to the one in the transactions file print them
                                if file_IBAN == trans_IBAN:
                                    print(line)
                                    obj.transactionsmethod()
                                    
                                               
                elif select == 2:

                    #open the accounts file, and read all the lines.
                    with open('accounts.txt') as f:
                        datafile = f.readlines()
                    #iterates through the lines
                    for line2 in datafile:
                        #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside file_IBAN
                        start = line2.find("| IBAN:") + len("| IBAN:")
                        end = line2.find(" | funds:")
                        file_IBAN = line2[start:end]
                        #Using slicing to find the balance, which is located between the start and end variables the string returned is put inside file_funds
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        #Using slicing to find the account number, which is located between the start3 and end3 variables the string returned is put inside file_acc_num
                        start3 = line2.find("Savings Account: #") + len("Savings Account: #")
                        end3 = line2.find(" | IBAN:")
                        file_acc_num = line2[start3:end3] 
                        # If the inputted account number (numid is equal to the the account number that was retrieved from the file and the string savings account is also in the line. Enter the if statement
                        if numid == file_acc_num and "Savings Account" in line2:
                            #create the object for savings account using the retrived variables
                            obj = SavingsAccount(numid,file_IBAN,int(file_funds)) #choose which account to withdraw from saving/checking
                            #open the accounts file, and read all the lines.
                            with open('AccountTransactions.txt') as f:
                                datafile = f.readlines()
                            #iterates through the lines
                            for line in datafile:
                                #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside trans_IBAN, this is found inside the transactions account
                                start = line.find("IBAN: ") + len("IBAN: ")
                                end = line.find(" Type:")
                                trans_IBAN = line[start:end] 
                                #If the Iban from the account is equal to the one in the transactions file print them
                                if file_IBAN == trans_IBAN:
                                    print(line)
                                    obj.transactionsmethod()
                            
                #Error checking
                else:
                    print("Must enter option 1 or 2")

            #This displays the balance when 6 is entered
            elif choice == 6:
                # Prompts the user for which account they would like to operate with
                print("Choose which acount type ypu would like to see your balance\n")
                print('\nPlease Enter Number Corresponding To Your Choice : ')
                select = int(input("1) Checking Account | 2) Savings Account \n"))
              # 1 is selected, so the cheking account will be used
                if select == 1:
                    
                   #open the accounts file, and read all the lines.
                    with open('accounts.txt') as f:
                        datafile = f.readlines()
                    #iterates through the lines
                    for line2 in datafile:
                        #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside file_IBAN
                        start = line2.find("| IBAN:") + len("| IBAN:")
                        end = line2.find(" | funds:")
                        file_IBAN = line2[start:end]
                        #Using slicing to find the account number, which is located between the start3 and end3 variables the string returned is put inside file_acc_num
                        start3 = line2.find("Checking Account: #") + len("Checking Account: #")
                        end3 = line2.find(" | IBAN:")
                        file_acc_num = line2[start3:end3]
                        #Using slicing to find the balance, which is located between the start and end variables the string returned is put inside file_funds
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        # If the inputted account number (numid is equal to the the account number that was retrieved from the file and the string checking account is also in the line. Enter the if statement
                        if numid == file_acc_num and "Checking Account" in line2:
                            #create the object for checking account using the retrived variables
                            obj = CheckingAccount(numid,file_IBAN,int(file_funds))
                            #method displays the available funds in the checking account
                            obj.available_funds()
                            break
                # 2 is selected, so the savings account will be used
                elif select == 2:
                    #open the accounts file, and read all the lines.
                    with open('accounts.txt') as f:
                        datafile = f.readlines()
                    #iterates through the lines
                    for line2 in datafile:
                        #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside file_IBAN
                        start = line2.find("| IBAN:") + len("| IBAN:")
                        end = line2.find(" | funds:")
                        file_IBAN = line2[start:end]
                        #Using slicing to find the balance, which is located between the start and end variables the string returned is put inside file_funds
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        #Using slicing to find the account number, which is located between the start3 and end3 variables the string returned is put inside file_acc_num
                        start3 = line2.find("Savings Account: #") + len("Savings Account: #")
                        end3 = line2.find(" | IBAN:")
                        file_acc_num = line2[start3:end3] 
                        # If the inputted account number (numid is equal to the the account number that was retrieved from the file and the string savings account is also in the line. Enter the if statement
                        if numid == file_acc_num and "Savings Account" in line2:
                            #create the object for savings account using the retrived variables
                            obj = SavingsAccount(numid,file_IBAN,int(file_funds)) #choose which account to withdraw from saving/checking
                            #method displays the available funds in the savings account
                            obj.available_funds()
                            break
                else:
                    print("Invalid input!")

            #Transfers moneey to a differnt account using the iban
            elif choice == 7:
                # Prompts the user for which account they would like to operate with
                print("Choose which acount type you would like to transfer from\n")
                print('\nPlease Enter Number Corresponding To Your Choice : ')
                select = int(input("1) Checking Account | 2) Savings Account \n"))
                # 1 is selected, so the cheking account will be used
                if select == 1:
                    
                   #open the accounts file, and read all the lines.
                    with open('accounts.txt') as f:
                        datafile = f.readlines()
                    #iterates through the lines
                    for line2 in datafile:
                        #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside file_IBAN
                        start = line2.find("| IBAN:") + len("| IBAN:")
                        end = line2.find(" | funds:")
                        file_IBAN = line2[start:end]
                        #Using slicing to find the account number, which is located between the start3 and end3 variables the string returned is put inside file_acc_num
                        start3 = line2.find("Checking Account: #") + len("Checking Account: #")
                        end3 = line2.find(" | IBAN:")
                        file_acc_num = line2[start3:end3]
                        #Using slicing to find the balance, which is located between the start and end variables the string returned is put inside file_funds
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        # If the inputted account number (numid is equal to the the account number that was retrieved from the file and the string checking account is also in the line. Enter the if statement
                        if numid == file_acc_num and "Checking Account" in line2:
                            #create the object for checking account using the retrived variables
                            obj = CheckingAccount(numid,file_IBAN,int(file_funds))
                            #transfer method used to transfer to a diffferent account using the iban, no parametera passed
                            obj.transfer()
                            #display the information
                            obj.__str__()
                            break
                 # 2 is selected, so the savings account will be used
                elif select == 2:
                    #open the accounts file, and read all the lines.
                    with open('accounts.txt') as f:
                        datafile = f.readlines()
                    #iterates through the lines
                    for line2 in datafile:
                        #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside file_IBAN
                        start = line2.find("| IBAN:") + len("| IBAN:")
                        end = line2.find(" | funds:")
                        file_IBAN = line2[start:end]
                        #Using slicing to find the balance, which is located between the start and end variables the string returned is put inside file_funds
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        #Using slicing to find the account number, which is located between the start3 and end3 variables the string returned is put inside file_acc_num
                        start3 = line2.find("Savings Account: #") + len("Savings Account: #")
                        end3 = line2.find(" | IBAN:")
                        file_acc_num = line2[start3:end3] 
                        # If the inputted account number (numid is equal to the the account number that was retrieved from the file and the string savings account is also in the line. Enter the if statement
                        if numid == file_acc_num and "Savings Account" in line2:
                            #create the object for savings account using the retrived variables
                            obj = SavingsAccount(numid,file_IBAN,int(file_funds)) #choose which account to withdraw from saving/checking
                            #transfer method used to transfer to a diffferent account using the iban, no parametera passed
                            obj.transfer()
                            #display the information
                            obj.__str__()
                            break
                else:
                    print("Invalid input!")


            elif choice == 8:
                  # Prompts the user for which account they would like to operate with
                print("Choose which acount type ypu would like to remove \n")
                print('\nPlease Enter Number Corresponding To Your Choice : ')
                select = int(input("1) Checking Account | 2) Savings Account \n"))
              # 1 is selected, so the cheking account will be used
                if select == 1:
                    
                   #open the accounts file, and read all the lines.
                    with open('accounts.txt') as f:
                        datafile = f.readlines()
                    #iterates through the lines
                    for line2 in datafile:
                        #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside file_IBAN
                        start = line2.find("| IBAN:") + len("| IBAN:")
                        end = line2.find(" | funds:")
                        file_IBAN = line2[start:end]
                        #Using slicing to find the account number, which is located between the start3 and end3 variables the string returned is put inside file_acc_num
                        start3 = line2.find("Checking Account: #") + len("Checking Account: #")
                        end3 = line2.find(" | IBAN:")
                        file_acc_num = line2[start3:end3]
                        #Using slicing to find the balance, which is located between the start and end variables the string returned is put inside file_funds
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        # If the inputted account number (numid is equal to the the account number that was retrieved from the file and the string checking account is also in the line. Enter the if statement
                        if numid == file_acc_num and "Checking Account" in line2:
                            checking = "Checking Account: "
                            #create the object for checking account using the retrived variables
                            obj = CheckingAccount(numid,file_IBAN,int(file_funds))
                            obj.delete_account(checking)
                            break
                # 2 is selected, so the savings account will be used
                elif select == 2:
                    #open the accounts file, and read all the lines.
                    with open('accounts.txt') as f:
                        datafile = f.readlines()
                    #iterates through the lines
                    for line2 in datafile:
                        #Using slicing to find the IBAN, which is located between the start and end variables the string returned is put inside file_IBAN
                        start = line2.find("| IBAN:") + len("| IBAN:")
                        end = line2.find(" | funds:")
                        file_IBAN = line2[start:end]
                        #Using slicing to find the balance, which is located between the start and end variables the string returned is put inside file_funds
                        start = line2.find(" | funds:€") + len(" | funds:€")
                        end = line2.find("|end")
                        file_funds = line2[start:end]
                        #Using slicing to find the account number, which is located between the start3 and end3 variables the string returned is put inside file_acc_num
                        start3 = line2.find("Savings Account: #") + len("Savings Account: #")
                        end3 = line2.find(" | IBAN:")
                        file_acc_num = line2[start3:end3] 
                        # If the inputted account number (numid is equal to the the account number that was retrieved from the file and the string savings account is also in the line. Enter the if statement
                        if numid == file_acc_num and "Savings Account" in line2:
                            checking = "Savings Account: "
                            #create the object for savings account using the retrived variables
                            obj = SavingsAccount(numid,file_IBAN,int(file_funds)) #choose which account to withdraw from saving/checking
                            #method displays the available funds in the savings account
                            obj.delete_account(checking)
                            break
                else:
                    print("Invalid input!")

            else:
                print('**Invalid Input.....')
  
  

if __name__ == "__main__":
    main()
