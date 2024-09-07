user_num = int(input("Enter a number: "));

units = user_num // 1 % 10; 
tens = user_num // 10 % 10;  
hundreds = user_num // 100 % 10;  
thousands = user_num // 1000 % 10;  

print(f"Units: {units}"); 
print(f"Tens: {tens}"); 
print(f"Hundreds: {hundreds}"); 
print(f"Thousands: {thousands}"); 


# if(len(user_num) != 4): 
#     print("Number must contain 4 digits"); 
# else:  
#     units = user_num[3];
#     tens = user_num[2];
#     hundreds = user_num[1];
#     thousands = user_num[0];
    
#     print(f"Units: {units}"); 
#     print(f"Tens: {tens}"); 
#     print(f"Hundreds: {hundreds}"); 
#     print(f"Thousands: {thousands}"); 

