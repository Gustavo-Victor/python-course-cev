numbers = []; 
highest_value = lowest_value = 0;

for count in range(0,5): 
    num = int(input("Enter a number: ")); 
    
    if(count == 0 or num > numbers[-1]): 
        numbers.append(num); 
    else: 
        pos = 0; 
        while pos < len(numbers): 
            if(num <= numbers[pos]): 
                numbers.insert(pos, num); 
                break; 
            pos += 1;
            
print("\nNumbers in ascending order: "); 
print(numbers);
        
   
    