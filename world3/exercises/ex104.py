def read_int(question="Enter an integer: "): 
    ok = False; 
    value = 0;
    
    while True: 
        num = str(input(question));
        if num.isnumeric(): 
            value = int(num); 
            ok = True; 
        else: 
            print("\033[0;31mERROR! Enter a valid integer.\033[m"); 
            
        if ok: 
            break; 
        
    return value; 
    


n = read_int("Enter a number: "); 
print(f"\033[0;36mYou entered {n}\033[m"); 
    