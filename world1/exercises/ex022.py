full_name = input("Enter your full name: ").strip(); 

full_name_upper = full_name.upper(); 
full_name_lower = full_name.lower(); 
full_name_length = len(full_name); 
first_name = full_name.split()[0]; 
first_name_length = len(first_name); 

print("Analysing your name..."); 
print(f"Your name in uppercase letters is {full_name_upper}"); 
print(f"Your name in lowercase letters is {full_name_lower}"); 
print(f"Your full name has {full_name_length} leters"); 
print(f"Your first name is {first_name} and has {first_name_length} letters"); 

