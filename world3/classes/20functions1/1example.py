def add(a=0, b=0): 
    print(f"{a} + {b} = {a + b}"); 
    
def sub(a=0, b=0): 
    print(f"{a} - {b} = {a - b}"); 
    
def mul(a=0, b=0): 
    print(f"{a} * {b} = {a * b}"); 
    
def div(a=0, b=0): 
    print(f"{a} / {b} = {a / b}"); 
      
def mod(a=0, b=1): 
    print(f"{int(a)} % {int(b)} = {int(a) % int(b)}"); 


def header(txt): 
    print("-"*30);
    print(f"{txt:^30}".upper()); 
    print("-"*30);     

num1 = float(input("First number: ")); 
num2 = float(input("Second number: ")); 


header("arithmetic operations"); 
add(num1, num2); 
sub(num1, num2); 
mul(num1, num2); 
div(num1, num2); 
mod(b=num2, a=num1); 
