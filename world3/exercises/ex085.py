numbers = [[], []]; 


for count in range(0,7):
    num = int(input(f"Enter the {count+1}° value: ")); 
    
    if(num % 2 == 0): 
        numbers[0].append(num); 
    else: 
        numbers[1].append(num);     
     
numbers[0].sort(); 
numbers[1].sort(); 

print("-="*40);
print(f"Even numbers: {numbers[0]}");  
print(f"Odd numbers: {numbers[1]}");  
