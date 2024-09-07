resp = ""; 
numbers = list(); 
odd_numbers = []; 
even_numbers = []; 

while True: 
    num = int(input("Enter a number: ")); 
    numbers.append(num); 
    
    
    resp = input("Do you want to continue? [y/n] "); 
    if(resp in "Nn"): 
        break;     
    
for number in numbers: 
    if number % 2 == 0: 
        even_numbers.append(number); 
    else: 
        odd_numbers.append(number); 
        
print(f"\nNumbers: {numbers}"); 
print(f"Even numbers: {even_numbers}"); 
print(f"Odd numbers: {odd_numbers}"); 