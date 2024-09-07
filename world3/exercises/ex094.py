person = {};
people = []; 
ages_sum = 0;
only_women = []; 
above_average_age = [];


while True: 
    person["name"] = input("Name: ").strip(); 
    person["age"] = int(input("Age: ")); 

    if(person["age"] < 0): 
        person["age"] *= -1;
    ages_sum += person["age"]; 
    
    person["gender"] = input("Gender: [M/F] ").strip().lower(); 
    if(person["gender"] not in "MmFf"): 
        while not person["gender"] in "MmFf": 
            print("Invalid gender. Please, just type M or F"); 
            person["gender"] = input("Gender: [M/F] ").strip().lower(); 
    
    people.append(person.copy()); 
    
    if(person["gender"] in "Ff"): 
        only_women.append(person.copy()); 

    
    resp = input("Do you want to continue? [Y/N]: ").strip().lower(); 
    if(resp in "Nn"):
        break; 
    
average_age = ages_sum / len(people);  

for p in people: 
    if(p["age"] > average_age): 
        above_average_age.append(p); 
        
    
print("-="*30); 
print(f"A) In Total, we have {len(people)} people"); 
print(f"B) The average age is {average_age}");
print(f"C) Registered Women: ", end=""); 
for woman in only_women: 
    print(f"{woman["name"]}", end=", "); 
print(f"\nD) List of people who are above average age: "); 
for p in above_average_age: 
    print(f"{p["name"]} - {p["age"]} years"); 