from datetime import date; 


birth_year = int(input("Enter your birth year: ")); 
current_year = date.today().year; 


if(birth_year > current_year or birth_year < 0): 
    print("Invalid birth year"); 
else: 
    age = current_year - birth_year; 
    print(f"Age: {age}"); 
    
    if(age <=9):
        print("Category: child"); 
    elif(age <= 14):
        print("Category: children's"); 
    elif(age <= 19):
        print("Category: junior"); 
    elif(age <= 25): 
        print("Category: senior"); 
    else: 
        print("Category: master"); 