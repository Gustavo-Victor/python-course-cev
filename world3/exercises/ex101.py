from datetime import date; 


def vote_status(birth_year: 1990): 
    current_year = date.today().year;
    
    if birth_year <=0 or birth_year > current_year: 
        birth_year = current_year;  
    
    user_age = current_year - birth_year;
    
    if user_age < 16:
       return  "{} years - vote denied".format(user_age); 
    elif user_age <=17 or user_age >= 65: 
        return  "{} years - vote is optional".format(user_age);  
    else:
        return  "{} years - vote is required".format(user_age); 
    
    

print("-"*30); 
year_of_birth = int(input("What year were you born in? ")); 
print(vote_status(year_of_birth)); 
