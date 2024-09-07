# local scope
def my_function(): 
    n1 = 4; 
    print(f"n1 inside = {n1}");
    
    
# global scope
n1 = 5; 
print(f"n1 outside = {n1}"); 
my_function(); 
print("-"*20)


# local scope getting global var
def my_funcion2(): 
    global n1; 
    n1 = 1; 
    print(f"n1 inside = {n1}");
    

# global scope
my_funcion2();
print(f"n1 outside = {n1}"); 