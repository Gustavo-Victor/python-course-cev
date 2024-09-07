full_name = input("Enter your full name: ").strip();
 
full_name_arr = full_name.split(); 
first_name = full_name_arr[0].capitalize();
last_name = full_name_arr[len(full_name_arr) - 1].capitalize();  

print("Nice to meet you!"); 
print(f"Your first name is {first_name}"); 
print(f"Your last name is {last_name}"); 