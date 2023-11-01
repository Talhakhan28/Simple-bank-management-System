print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(" Welcome TO Talha TK BANK MANAGEMENT SYSTEM")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
login=int(input("ENTER Your Pin Code To Login:\n"))
if(login<1):

    print("Enter Correct Pin")
else:
    print("Welcome To your ACCOUNT\n")

checkbalance=int(input("PRESS 1 To Check BALANCE:\n"))
if(checkbalance<1):
    print("Press Correct number")
else:
    print("Your Balance is:\n 10000000\n")

sendmoney=int(input("Enter AMOUNT TO send:\n"))   
if(sendmoney<500):
    print("Enter Amount Greater than 500")
else:
    print("MONEY Transfer Successfull\n")

getloan=int(input("Enter Amount For Loan (Maximum Loan(5000)):\n"))
if(getloan>5000):
    print("Maximum Loan is 5000, you cant get loan more than 5000")
else:
    print("Loan Successfull\n")

changepincode=int(input("ENTER 1 to change pin code "))
if(changepincode<=2):
    
    print("You have Successfully Changed the Pin code\n")

exit=int(input("Press 0 to Logout:\n"))
if(exit<=0):
    print("you have been Logout\n")
    

