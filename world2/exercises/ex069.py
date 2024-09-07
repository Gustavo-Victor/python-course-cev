number_of_people = 0;
adult_people = 0; 
number_of_men = 0; 
women_under_twenty = 0;  

def menu(): 
    print("-"*30); 
    print("Register a person".upper());
    print("-"*30); 
    

while True: 
    menu(); 
    age = int(input("Age: ")); 
    if(age < 0): 
        while age < 0: 
            print("Invalid age");
            age = int(input("Age: ")); 
            
    gender = input("Gender: ").strip().lower()[0]; 
    if(gender not in "MmFf"): 
        while not gender in "MmFf": 
            print("Invalid gender");
            gender = input("Gender: ").strip().lower()[0]; 
    
    number_of_people += 1; 
    
    if(gender in "Mm"):
        number_of_men += 1;
        
    if(age >= 18):
        adult_people += 1;
        
    if(gender in "Ff" and age < 20):
        women_under_twenty += 1;              
    
    print("-"*30); 
    resp = input("Do you want to continue? [y/n]: ").strip().lower();
    if(resp in "Nn"):
        break; 
    
    
print("-"*30); 
print(f"Number of adult people: {adult_people}"); 
print(f"Number of men: {number_of_men}"); 
print(f"Women under 20: {women_under_twenty}"); 
print("-"*30); 
print("\nthe end".upper());