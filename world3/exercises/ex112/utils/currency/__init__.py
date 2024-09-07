def increase(price=1, percentage=10, format=False): 
    result = price * (1 + (percentage / 100));
    if format: 
        result = format_value(result); 
    return result; 

    
def decrease(price=1, percentage=10, format=False): 
    result = price * (1 - (percentage / 100));
    if format: 
        result = format_value(result); 
    return result; 

        
def double(price=1, format=False): 
    result = price * 2;
    if format: 
        result = format_value(result); 
    return result; 


def half(price=1, format=False): 
    result = price / 2;
    if format: 
        result = format_value(result); 
    return result; 


def format_value(price=1, currency="$"): 
    return f"{currency}{price:.2f}".replace(".", ",");

def summary(price=1, inc=10, dec=10): 
    print("-"*30);
    print("{:^30}".format("value summary".upper()));  
    print("-"*30);  
    
    print(f"Price: {format_value(price)}"); 
    print(f"Double price: {double(price, True)}"); 
    print(f"Half price: {half(price, True)}"); 
    print(f"{inc}% percentage increase: {increase(price, inc, True)}"); 
    print(f"{dec}% percentage decrease: {decrease(price, dec, True)}"); 

# DOC(s)
# increase
increase.__doc__ = """
    increase(price=1, percentage=10, format=False)
    
    -> Function that calculates the price of something with a percentage increase and formatting option

    price
        float or int value
    
    percentage 
        float or int value
        
    format
        boolean value
    
    return 
        float or str, depending on format parameter 
"""; 


# decrease
decrease.__doc__ = """
    decrease(price=1, percentage=10, format=False)
    
    -> Function that calculates the price of something with a percentage discount and formatting option

    price
        float or int value
    
    percentage 
        float or int value
        
    format
        boolean value
    
    return 
        float or str, depending on format parameter 
"""; 


#double
double.__doc__ = """
    double(price=1, format=False)
    
    Function that calculates the double of a number with a formatting option
    
    price
        float value
        
    format
        boolean value
        
    return 
        float or int value
"""; 


#half
half.__doc__ = """
    half(price=1, format=False)
    
    Function that calculates half of a number with a formatting option
    
    price
        float value
        
    format
        boolean value
        
    return 
        float or int value
"""; 


# format_value
format_value.__doc__ = """
    format(price=1, currency='$')
    
    Funciont that formats a price based on the amount and currency type
    
    price
        float value
        
    currency
        string value - "$" (dolar sign) is the default value
        
    return 
        string value
"""

# summary
summary.__doc__ = """
    summary(price=1, inc=10, dec=10)
    
    -> Creates a summary about a value entered
    
    price
        int or float value 
        
    inc
        percentage increase in value; int or float value
        
    dec
        percentage decrease in value; int or float value
    
    Return: string value (summary menu)
"""; 
