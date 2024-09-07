sum_of_ages = 0;
average_age = 0;
oldest_man = ""; 
age_of_oldest_man = 0;
women_under_twenty = 0;


for count in range(1,5):
    print("-"*5 + f" {count}° PEOPLE " + "-"*5); 
    name = str(input("Name: ")).strip(); 
    age = int(input("Age: ")); 
    gender = str(input("Gender [M/F]: ")).strip().lower();
    
    if(not name or len(name) == 0): 
        while(len(name) == 0): 
            print("Name is required"); 
            name = str(input("Name: ")).strip(); 
    
    if(not str(age) or len(str(age)) == 0): 
        while(not str(age)): 
            print("Age is required"); 
            age = int(input("Age: "));
    
    if(gender not in ['m', 'f']): 
         while(gender not in ['m', 'f']): 
            print("Gender is invalid"); 
            gender = str(input("Gender: ")).strip().lower();
            
    sum_of_ages += age;
    
    if(gender == 'm' and int(age) > int(age_of_oldest_man)):
        age_of_oldest_man = age; 
        oldest_man = name; 
        
    if(gender == "f" and int(age) < 20): 
        women_under_twenty += 1;
            

average_age = sum_of_ages / 4; 

print("\nAverage age of the group: {:.2f}".format(average_age)); 
print(f"The oldest man is {age_of_oldest_man} years old and calls {oldest_man}");
print(f"In total there are {women_under_twenty} women under 20"); 