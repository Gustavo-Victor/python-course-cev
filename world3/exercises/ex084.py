from os import system;

person = []; 
people = []; 
weights = []; 

while True: 
    system("clear"); 
    
    name = input("Name: "); 
    if(not name or len(name) == 0):
        while(not name): 
            print("Invalid value"); 
            name = input("Name: "); 
    person.append(name);
    
    weight = float(input("Weight: ")); 
    if(not str(weight) or len(str(weight)) == 0): 
        while(not(str(weight))): 
            print("Invalid value"); 
            weight = float(input("Weight: ")); 
            
    
    person.append(weight); 
    weights.append(weight); 
    people.append(person[:]);
    person.clear(); 
    
    resp = input("Do you want to continue? [y/n] ")
    if(resp in "Nn"): 
        break; 


heaviest_people = []; 
lightest_people = []; 


for person in people: 
    if(person[1] == max(weights)): 
        heaviest_people.append(person[:]); 
        
    if(person[1] == min(weights)): 
        lightest_people.append(person[:]); 

print("-="*40); 
print(f"In total, you registered {len(people)} people"); 
print(f"The biggest weight was {max(weights)}. Weight of: ", end=" "); 
for person in heaviest_people: 
    print(person[0], end=" | "); 
    
print(f"\nThe lowest weight was {min(weights)}. Weight of: ", end=" "); 
for person in lightest_people: 
    print(person[0], end=" | "); 


        
