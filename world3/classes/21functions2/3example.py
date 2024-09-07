def factorial(num=1): 
    fat = 0; 
    
    if num < 0: 
        num *= -1;     
    
    if num == 1 or num == 0: 
        fat = 1; 
    else: 
        count = num;
        fat = 1; 
        while count >=1: 
            fat *= count;
            count -= 1; 
            
    return fat; 

num = int(input("Enter a number: ")); 
print(f"{num}! = {factorial(num)}"); 


# print(f"5! = {factorial(5)}"); 
# print(f"4! = {factorial(-4)}"); 
# print(f"3! = {factorial(3)}"); 
# print(f"8! = {factorial(8)}");
# print(f"9! = {factorial(9)}");  
# print(f"0! = {factorial(0)}");  
# print(f"1! = {factorial(1)}");  
        
    