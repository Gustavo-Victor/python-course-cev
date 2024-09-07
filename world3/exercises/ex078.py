numbers = [];

for count in range(0,5): 
    num = int(input("Enter a number: ")); 
    numbers.append(num); 

highest_value = max(numbers); 
lowest_value = min(numbers); 

highest_value_positions = []; 
lowest_value_positions = []; 

for pos, item in enumerate(numbers): 
    if(item == highest_value): 
        highest_value_positions.append(pos); 
    
    if(item == lowest_value): 
        lowest_value_positions.append(pos); 

print(f"\nYou entered the values: {numbers}"); 
print(f"The highest value entered is {highest_value} in positions: {highest_value_positions}"); 
print(f"The lowest value entered is {lowest_value} in positions: {lowest_value_positions}"); 