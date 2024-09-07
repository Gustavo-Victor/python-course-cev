from datetime import date;


print("Enter the year of birth of 7 people: \n"); 
age_list = [];
current_year = date.today().year; 
number_of_adults = 0; 
number_of_minors = 0;

for count in range(1, 8): 
    year_of_birth = int(input(f"{count} year: "));
    
    if(year_of_birth <=0):
        print("Invalid year :(");
        print("Let's consider the current year"); 
        year_of_birth = current_year;  
    
    if(year_of_birth > current_year):
        while(year_of_birth > current_year):
            print("Invalid year :("); 
            year_of_birth = int(input(f"{count} year: "));
            
    age = current_year - year_of_birth; 
    
    if(age < 21): 
        number_of_minors += 1;
    else: 
        number_of_adults += 1;

print(); 
print(f"Adults: {number_of_adults}"); 
print(f"Minors: {number_of_minors}"); 