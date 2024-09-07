from os import system; 

people = []; 
person_data = [];


for count in range(0,3): 
    person_data.append(input("Name: ")); 
    person_data.append(int(input("Age: "))); 
    people.append(person_data[:]); 
    person_data.clear(); 
    system('clear'); 
    
    
print("Registered people: ");  
print(people);  