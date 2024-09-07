from datetime import date; 

current_year = int(date.today().year); 
birth_year = int(input("What year were you born? ")); 
age = current_year - birth_year; 
year_of_enlistment = 0; 
years_to_enlist = 0; 
missing_enlistment_in_years = 0;

if(birth_year > current_year):
   print(f"Invalid year of birth.");
elif(age < 0 or age > 120): 
    print(f"Invalid or impossible age."); 
else:
    print(f"Anyone born in {birth_year} turns {age} in {current_year}.");   
    if(age < 18):
        years_to_enlist = 18 - age; 
        year_of_enlistment = current_year + years_to_enlist; 
        print(f"There are still {years_to_enlist} years left until your military enlistment.");
        print(f"Your enlistment will be in {year_of_enlistment}."); 
    elif(age > 18):
        missing_enlistment_in_years = age - 18; 
        year_of_enlistment = current_year - missing_enlistment_in_years; 
        print(f"You should have already enlisted {missing_enlistment_in_years} years ago.");
        print(f"Your enlistment was in {year_of_enlistment}."); 
    else:
        print("You have to enlist emmediately!");