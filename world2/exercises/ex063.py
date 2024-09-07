print("-"*20); 
print("Fibonacci Sequence");
print("-"*20); 


terms = int(input("How many terms would you like to show? ")); 
count = 1; 

    
if(terms == 0):
    print("Invalid value");
    print("Let's show 1 term instead"); 
    print("0 ->", end=' '); 
else: 
    if(terms < 0): 
        print("Invalid value");
        print("Let's consider the opposite of this number"); 
        terms *= -1; 
        
    a = 1; 
    b = 0; 
    c = 0; 

    print("0 -> 1 ->", end=' '); 

    while(count <= terms - 2):
        c = a + b; 
        b = a; 
        a = c; 
        print(c, end = ' -> '); 
        count += 1;
print("the end".upper()); 