resp = ""; 
numbers = [];  

while resp != 'n':     
    num = int(input("\nEnter a number: "));
    
    if(num not in numbers): 
        numbers.append(num); 
    else: 
        print("This number is already registered. Enter another..."); 
    
    resp = input("Do you want to continue? [y/n]").strip().lower(); 
    
numbers.sort(); 
print("-="*30); 
print(f"Numbers in ascending order: {numbers}"); 
