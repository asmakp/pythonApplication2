# This is the bank account program with following function                      Date:2020/09/25
import json

from datetime import datetime, timedelta

with open('mydata.json') as file:
    accountBook = json.load(file)


def Main_menu():
    print("\t\t WELLCOME TO THE VASA BANK  ")
    print("*****MAINMENU*****\n")
    print("1. CREATE ACCOUNT")
    print("2. LOGIN")
    print("3. FINISH")
   

def create_account():
      kontoNum = input("Enter Account Number: ")  # Gets the  account number
      if kontoNum  in accountBook.keys():
          print ("Account exist\n")
      else: 
        password = input("Create a password: ")     # creat a new Account/Dictionary
        accountBook[kontoNum] = {"password":password,"balance":float(),"date":[],"trx" :[]}
        with open('mydata.json') as f:              
          data = json.load(f)
          data.update(accountBook)                   #appending to existing file    
        with open('mydata.json', 'w') as f:
         json.dump(data, f, indent = 4)

# Method for updating deposit and withdrawal balance
def update_balance(kontoNum,amount,trx,trxdate):        
    with open("mydata.json", "r") as jsonFile:
        data = json.load(jsonFile)
        
        data[kontoNum]["balance"] = amount
        data[kontoNum]["trx"].append(trx)
        data[kontoNum]["date"].append(trxdate)

    with open("mydata.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent = 4)
        print("your current balance is:",data[kontoNum]["balance"])                           
        

def withdraw(KontoNum):
    today = datetime.now() 
    with open("mydata.json", "r") as jsonFile:
        data = json.load(jsonFile)

    amountToDraw= float(input("enter the amount: "))     
    bal = data[KontoNum]["balance"]             
    if amountToDraw > float(bal) :
        print("Not enough balance")
    elif amountToDraw <= 0:
        print("Invalid input")
    else:
       
       amount = bal- amountToDraw                   # Deducting entered amount and from  balance
       trx = - amountToDraw
       trxdate = today.strftime("%Y.%m.%d")
       update_balance(KontoNum,amount,trx,trxdate)      
       
   
def deposit(kontoNum):
    today = datetime.now() 
    with open("mydata.json", "r") as jsonFile:
        data = json.load(jsonFile)
    try:
        while True:
            Addamount = float(input("Enter the amount to be deposited: "))
            if Addamount <= 0:
                print(" \nEnter valid Amount\n")
                continue
            else:
             bal = data[kontoNum]["balance"]               
             amount = Addamount + float(bal )           #Adding the entered amount to existing balance  
             trx = Addamount
             trxdate = today.strftime("%Y.%m.%d")
   
            update_balance(kontoNum,amount,trx,trxdate)
            break
    except ValueError:
         print (" Enter valid input \n")

   
def balance_rest(KontoNum):
     with open("mydata.json", "r") as jsonFile:
        data = json.load(jsonFile)
  
     print(f"your current balance is:",data[KontoNum]["balance"])  

def transaction(KontoNum):  
    with open("mydata.json", "r") as jsonFile:
       data = json.load(jsonFile)
    if  data[KontoNum]["trx"] == []:
        print("\nNo transaction to show\n")
    else:
        for d,t in zip(data[KontoNum]["date"],data[KontoNum]["trx"]):
            print(f'Date: {d} -->{ t} Kr')

def menuB(kontoNum):
       
    while True:
        
        try:
            print(f"\n****Account Menu****    Account Number {kontoNum}")
            print("1.Withdraw")
            print("2.Deposit")
            print("3.Show Transaction")
            print("4.Show Balance")
            print("5.Finish")
    
            val1 = int(input("Enter your choice: "))              
            if val1 == 1:
                withdraw(kontoNum)

            elif val1 == 2:
                deposit(kontoNum)

            elif val1 == 3:
                transaction(kontoNum)

            elif val1 == 4:
                balance_rest(kontoNum)
          
            elif val1 == 5:
                break
       
            else:
             print (" Enter valid input \n")
        except ValueError:
         print (" Enter valid input \n")
    

def Get_login():                                           
      
      kontoNum = input("Enter account number: ")
                           
      if kontoNum  in accountBook.keys(): 
            password =str (input("Enter the password: "))          
           
            if password == str(accountBook[kontoNum]["password"]):
                 menuB(kontoNum)
            else:
                print("wrong password\n")
      else:
          print("Account does not exist\n")     

while True:
                                                            # The program starts here
    Main_menu()                                             # calling main menu
    try:
        val = int(input("Enter your choice : "))
        if  val == 1:
            create_account()
            
        elif val == 2:
            Get_login()
        
        elif val == 3:
            print("\nTHANK YOU FOR USING VASA BANK \n HAVE A NICE DAY\n")
            break
        else:
            print("Enter valid input \n")
    except ValueError:
        print (" Enter valid input \n")
      