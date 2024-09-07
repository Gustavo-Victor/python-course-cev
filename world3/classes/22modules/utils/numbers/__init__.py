def factorial(n): 
    if n < 0: 
        n *= -1;
        
    f = 1; 
    for count in range(1, n+1): 
        f *= count; 
    return f;


def double(n): 
    return n * 2; 


def triple(n): 
    return n * 3; 