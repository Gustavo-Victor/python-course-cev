from currency import format_value, decrease, increase, double, half; 

price = float(input("Enter the price: $")); 
increase_percentage = 10;
decrease_percentage = 10;  
half_price = half(price, True); 
double_price = double(price, True); 
price_increased = increase(price, increase_percentage, True); 
price_with_discount = decrease(price, decrease_percentage, True); 

print("-"*30); 
print(f"Half of {format_value(price)} is {half_price}")
print(f"Double of {format_value(price)} is {double_price}")
print(f"Increasing {increase_percentage}%, we have {price_increased}"); 
print(f"Decreasing {decrease_percentage}%, we have {price_with_discount}"); 



print()
print(increase.__doc__);
print(decrease.__doc__);
print(double.__doc__);
print(half.__doc__);
print(format_value.__doc__);
 