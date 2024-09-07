def highest_value(*numbers): 
    highest = 0; 
    
    print("-="*30); 
    print("Analysing past values..."); 
    for count in range(0, len(numbers)): 
        print(f"{numbers[count]}", end=" ")
        if(numbers[count] > highest): 
            highest = numbers[count]; 
    print(f"-> {len(numbers)} values were reported in total"); 
    print(f"The highest value is {highest}"); 
    
    
highest_value(2,9,4,5,7,1); 
highest_value(4,7,0); 
highest_value(1,2); 
highest_value(6); 
highest_value(); 