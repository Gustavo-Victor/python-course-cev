from currency import format_value, decrease, increase, double, half; 

price = float(input("Enter the price: R$")); 
increase_percentage = 10;
decrease_percentage = 10;  
half_price = half(price); 
double_price = double(price); 
price_increased = increase(price, increase_percentage); 
price_with_discount = decrease(price, decrease_percentage); 

print("-"*30); 
print(f"Half of {format_value(price, "R$")} is {format_value(half_price, "R$")}")
print(f"Double of {format_value(price, "R$")} is {format_value(double_price, "R$")}")
print(f"Increasing {increase_percentage}%, we have {format_value(price_increased, "R$")}"); 
print(f"Decreasing {decrease_percentage}%, we have {format_value(price_with_discount, "R$")}"); 


