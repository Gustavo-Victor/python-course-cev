person = {
    'first_name': 'Gustavo',
    'last_name': 'Victor',
    'age': 21, 
    'married': False, 
    'hobbies': ['Watch animes', 'Play guitar', 'Soccer', 'Basketball']
}; 

print(f"My name is {person['first_name']:=^20} and I'm {person['age']} years old"); 

print("\nPrint dictionary: \n"); 
for key in person.keys(): 
    if(key == 'hobbies'): 
        print("Hobbies: "); 
        for item in person['hobbies']: 
            print(item, end='|'); 
    else: 
        print(f'{key}: {person[key]}'); 
