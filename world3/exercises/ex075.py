my_numbers = (
    int(input("Enter a number: ")), 
    int(input("Enter a number: ")), 
    int(input("Enter a number: ")), 
    int(input("Enter a number: ")), 
    ); 

print(f"\nYou entered: {my_numbers}"); 
print(f"The number 9 appeared {my_numbers.count(9)} time(s) in the tuple");
if(3 in my_numbers):  
    print(f"The number 3 is on position [{my_numbers.index(3) + 1}]"); 
else: 
    print(f"No number 3 was entered"); 

print("Even numbers: ", end=" "); 
for item in my_numbers: 
    if item % 2 == 0:
        print(item, end=" "); 


