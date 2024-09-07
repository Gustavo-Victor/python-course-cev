gender = input("Enter your gender [M/F]: ").strip().upper(); 


if(gender not in ["M", "F"]): 
    while(gender not in ["M", "F"]): 
        print("Invalid gender"); 
        gender = input("Enter your gender [M/F]: ").strip().upper(); 

if(gender == "M"): 
    print(f"Gender 'Male' successfully registered");
else: 
    print(f"Gender 'Female' successfully registered");  
    
           
