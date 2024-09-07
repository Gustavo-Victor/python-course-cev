print("="*15);
print("10 terms of an AP"); 
print("="*15);


first_term = int(input("Firts term: ")); 
reason = int(input("Reason: "));
tenth_term = first_term + (10 - 1) * reason; 


for count in range(first_term, tenth_term + reason, reason):
    print(f" {count}", end=' ->'); 
print(" The End"); 
    
    
