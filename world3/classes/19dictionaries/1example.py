person = {
	'name': 'Pedro',
	'age': 25, 
	'gender': 'M'
}; 

print(person['name']); 
print(person['age']); 
print(person['gender']); 

del person['age'] ; 

print(person.values()); 
print(person.keys()); 
print(person.items()); 

person['age'] = 28; 

for key, value in person.items(): 
    print(f"{key}: {value}"); 