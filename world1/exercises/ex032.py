from datetime import date; 

year = int(input("What year are we currently in? \nEnter 0(zero) to analyse the current year: ")); 

if(year == 0): 
    year = date.today().year;  

if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year."); 
else: 
    print(f"{year} is not a leap year."); 