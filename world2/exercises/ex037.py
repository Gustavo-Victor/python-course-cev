# from os import system; 
user_num = int(input("Enter an integer: "));

print("Choose a number base for conversion: "); 
print("[ 1 ] Binary");
print("[ 2 ] Octal");
print("[ 3 ] Hexadecimal"); 
user_option = int(input("Your option: "));  
result = ""; 


if(user_option == 1): 
    result = bin(user_num); 
elif(user_option == 2): 
    result = oct(user_num); 
elif(user_option == 3): 
    result = hex(user_num); 
else: 
    print("Invalid option."); 
    

if(result): 
    result = result[2:]; 
    print(f"\nResult: {result}"); 
    