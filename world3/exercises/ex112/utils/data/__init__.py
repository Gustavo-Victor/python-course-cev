def input_num(message="Enter a number: "): 
    valid_num = False; 
    result = 0;
    
    while valid_num != True: 
        num = input(message).strip().lower(); 
        
        if("," in num): 
            num = num.replace(",", ".", 1).strip();  
                 
        if (num.isalpha() or "," in num or len(num) == 0): 
            print(f"\033[31mError - {num} is not a valid price\033[m"); 
        else: 
            result = float(num); 
            valid_num = True; 
    return result; 