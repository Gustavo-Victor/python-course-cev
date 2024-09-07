house_price = float(input("What is the price of the house? R$"));
salary = float(input("What is your salary? R$"));
loan_time = int(input("How many years will it take to pay? "));

installment_value = house_price / (loan_time * 12); 
print("Monthly installment: R${:.2f}".format(installment_value)); 

if(installment_value <= salary * 0.3): 
    print("Loan accepted"); 
else: 
    print("Loan denied"); 

