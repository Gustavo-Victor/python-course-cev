def add_many(*numbers): 
    print(numbers, type(numbers))
    print(list(numbers)); 
    print(f"Sum = {sum(list(numbers))}"); 
    
    
add_many(1,2,3,4,5,6); 