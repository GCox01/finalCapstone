import math #imports the math function
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
calculation = str(input("Either enter 'investment' or 'bond' from the menu above to proceed: " )) #determines which type of calculation is required from the user
if calculation=="investment" or calculation=="Investment" or calculation=="INVESTMENT": #checks all entries for 'investment' by user
    deposit = float(input("Please enter your deposit: "))
    interest = float(input("Please enter your interest rate: "))
    interest = interest/100 #finds interest percentage
    years = float(input("Please enter the number of years you plan on investing: "))
    interest_type = str(input("Please enter if you want simple or compound interest: "))
    total = 0
    if interest_type=="simple" or interest_type=="Simple" or interest_type=="SIMPLE": #checks if user input for 'simple' interest
        total = deposit*(1+interest*years) #performs calculation for the total interest
        print("Your total is: ", total) #gives result
    elif interest_type=="compound" or interest_type=="Compound" or interest_type=="COMPOUND": #checks if user input for 'compound' interest
        total = deposit * math.pow((1+interest), years) #performs calculation for total interest
        print("Your total is: " , total) #gives user the result
    else:
        print("You have not entered a correct value. Please try again.") #error message if user does not enter correct interest type


elif calculation=="bond" or calculation=="Bond" or calculation=="BOND": #checks if user input for 'bond'
    repayment = 0
    house_value = float(input("Please enter the value of the house: "))
    interest = float(input("Please enter your interest rate: "))
    interest = (interest/100)/12 #finds interest per month
    months = int(input("Please enter the number of months you plan to take to repay the bond: "))
    repayment = (interest*house_value)/(1-(1+interest)**(-months)) #calculates monthly repayment
    print("Your repayment per month is: ", repayment) #gives monthly repayment to user

else:
    print("You have not entered a valid input. Please try again.") #error message if user does not enter 'investment' or 'bond'