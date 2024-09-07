def increase(price=1, percentage=10): 
    return price * (1 + (percentage / 100));
    
def decrease(price=1, percentage=10): 
    return price * (1 - (percentage / 100));
        
def double(price=1): 
    return price * 2;

def half(price=1): 
    return price / 2;

def format_value(price=1, currency="$"): 
    #price = str(price);
    return f"{currency}{price:.2f}".replace(".", ",");
    
     

