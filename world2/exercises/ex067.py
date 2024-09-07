print("Multiplication Table".upper());

while True: 
    print("-"*30)
    print("Only a negative number to stop...");
    num = float(input("Enter a number: ")); 
    print("-"*30)
        
    if(num < 0):
        break; 
    
    for count in range(1,11): 
        print(f"{num} X {count} = {(num * count):.2f}"); 
        
print("the end".upper()); 