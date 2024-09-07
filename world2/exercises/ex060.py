num = int(input("Enter an integer: ")); 

def calc_factorial(num):  
    if(num == 1 or num == 0): 
        return 1
    elif(num < 0): 
        return False; 
    else:     
        count = num; 
        factorial = 1;
        while(count >= 1): 
            factorial *= count; 
            count -= 1; 
            
        return factorial; 

if(calc_factorial(num) != False): 
    print(f"Factorial: {calc_factorial(num)}"); 
else: 
    print("There is no factorial of a negative number"); 