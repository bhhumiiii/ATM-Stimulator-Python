import sys #needed for sys.exit extension 

print("welcome to our ATM")


correct_pin="1234"
attempts=0
max_attempts=3

#while condition is used as atm works on loop that is infinte time
while attempts<max_attempts :#limited attempts for the login 
    pin=input("Enter your 4-digit PIN:")
    if pin==correct_pin:
      print("login sucessful!\n")
      break #to exit the loop of while

#elif attempts += 1(not vaild+= in elif ) # += means attempts +1 which is attempts=0 so 1+0 which is 1


    else :
       attempts+=1
     
       if attempts==max_attempts:
         print("No more tries left. your card has been blocked.")
         sys.exit()
       else:
        print(f"Incorrect PIN entered , Attempts left :{max_attempts-attempts}\n")



 # if it is sucessfully logined then 
balance= 10000 #starting balance.#{no coma in number.}

while True:# true in python means to run a code
     print("\n----------ATM MENU----------")
     print("1.Current balance")
     print("2.Deposit Money")
     print("3.Withdraw Money ")
     print("4.Exit")

     choice=input("enter options from (1-4))") # int not use and here 1,2,3,4 are in string .
     

     #CHOICE 1
     if choice=="1":
        print(f"your current balance is :₹{balance}")

        #CHOICE 2
     elif choice=="2":
      deposit_money=int(input("Enter the amount to deposit:₹ "))
      if deposit_money>0:
       balance+=deposit_money  # means balance+ deposit money
       print(f"₹{deposit_money} deposited sucessfully")
       print(f"updated balance;₹{balance}")#this balance is of the if condition written and give sum of total deposit +balance earlier.
      elif deposit_money<0:
        print("Invalid deposit!")
        print("Try again")
      else:
        print("Invalid deposit amount")

        #CHOICE 3
     elif choice=="3":  
      withdraw_money=int(input("Enter the amount:₹"))
      if withdraw_money<=0:# <=0 is written despite of 0 beacuse then a negative number input will be given which is not valid in ATM.
        print("Invalid amount entered")
      if withdraw_money>balance: # this Balance is the starting balance
        print("Insuficient Balance!")
      else:
         balance-=withdraw_money
         print(f"Remaining Balance:₹{balance}")

         #CHOICE 4
     elif choice == "4":
        print("👋 Thank you for using Python ATM. Goodbye!")
        break
     else:
       print("Invalid choice please enter a number from 1 to 4")
         







     



    