def factorial(num = 1, show=False): 
    print("-="*30);
    
    fat = 1;
    result = ""; 
    
    if num == 0 or num == 1: 
        result = 1;
    
    if num < 0: 
        num *= -1; 
    
    if show: 
        for count in range(num, 0, -1): 
            if count == 1: 
                result += "{} = ".format(count);
            else: 
                result += "{} x ".format(count);
            fat *= count;  
        result += "{}".format(fat); 
    else: 
        for count in range(num, 0, -1): 
            fat *= count;  
        result = fat; 
        
    return result; 

 
print(factorial(3, True)); 
print(factorial(2, True)); 
print(factorial(5)); 
print(factorial(3, False)); 
print(factorial(6, False)); 

factorial.__doc__ = """
    -> Calculates the factorial of an integer. 
    :param num: the number to be calculated the factorial
    :param show (optional): show or not the process 
    :return: a string containing the number or process until reaching the factorial
"""; 

print(factorial.__doc__); 