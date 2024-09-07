salary = float(input("What is your salary? R$")); 
increase_percentage = 15; 

if(salary > 1250): 
    increase_percentage = 10; 
    
new_salary = salary * (1 + (increase_percentage / 100)); 
print("Whoever earns R$ {:.2f} now earns R$ {:.2f}".format(salary, new_salary)); 