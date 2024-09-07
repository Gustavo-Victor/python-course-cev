def create_player_record(name="", total_goals='0'):
    if(not total_goals.isnumeric()):
        total_goals = 0; 
    else: 
        total_goals = int(total_goals);    
        
    if(len(name) == 0 or name == ""): 
        name = "<unknown>";   
    return f"The player called {name} scored {total_goals} goal(s) in the championship."; 
    
    
print("-="*30); 
name = input("Name: ").strip(); 
goals = input("Goals: ").strip(); 

print(create_player_record(name, goals)); 