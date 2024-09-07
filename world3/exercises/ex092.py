from datetime import date; 

person = {}; 
current_year = date.today().year; 

person["name"] = input("Name: "); 
person["birth_year"] = int(input("Birth year: ")); 

if person["birth_year"] == 0:
    person["birth_year"] = current_year; 
elif(person["birth_year"] < 0): 
    while(person["birth_year"] < 0): 
        print("\nInvalid year"); 
        person["birth_year"] = int(input("Birth year: "));
elif(person["birth_year"] > current_year): 
    while(person["birth_year"] > current_year): 
        print("\nInvalid year"); 
        person["birth_year"] = int(input("Birth year: "));

person["age"] = current_year - person["birth_year"];  
person["ctps"]= int(input("Number Work Card (CTPS): ")); 

if(person["ctps"] == 0): 
    print("-="*30); 
    for key, value in person.items(): 
        if(key == "birth_year"): 
            continue; 
        print(f"{key}: {value}"); 
else: 
    if(person["ctps"] < 0): 
        person["ctps"] *= -1; 

    person["hire_year"] = int(input("Year of hire: ")); 
    if person["hire_year"] == 0:
        person["hire_year"] = current_year; 
    elif(person["hire_year"] < 0): 
        while(person["hire_year"] < 0): 
            print("\nInvalid year"); 
            person["hire_year"] = int(input("Year of hire: "));
    elif(person["birth_year"] > current_year): 
        while(person["hire_year"] > current_year): 
            print("\nInvalid year"); 
            person["hire_year"] = int(input("Year of hire: "));
    
    person["salary"] = float(input("Salary: R$")); 
    if(person["salary"] <0): 
        person['salary'] *= -1;   
    
    time_contributed = current_year - person["hire_year"]; 
    person["years_until_retirement"] = 35 - time_contributed;
    
    print("-="*30); 
    for key, value in person.items(): 
        if(key == "birth_year"): 
            continue; 
        print(f"{key}: {value}"); 
    
    
