resp = ""; 
values = list(); 

while True: 
    num = int(input("Enter a number: ")); 
    values.append(num); 
    
    
    resp = input("Do you want to continue? [y/n] "); 
    if(resp in "Nn"): 
        break;     
    
    
values.sort(reverse=True); 
print(f"\nThe list has {len(values)} elements"); 
print(f"List in descending order: {values}"); 
print(f"Number 5 is in the list" if 5 in values else "Number 5 was not found in the list");