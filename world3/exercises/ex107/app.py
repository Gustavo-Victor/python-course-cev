import currency; 

price = float(input("Enter the price: R$")); 
increase_percentage = 10;
decrease_percentage = 10;  

print("-"*30); 
print(f"Half of R${price} is R${currency.half(price)}")
print(f"Double of R${price} is R${currency.double(price)}")
print(f"Increasing {increase_percentage}%, we have R${currency.increase(price, increase_percentage)}"); 
print(f"Decreasing {decrease_percentage}%, we have R${currency.decrease(price, decrease_percentage)}"); 


