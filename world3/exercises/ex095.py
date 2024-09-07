from os import system;

players = []; 
player = {};

while True: 
    system("clear"); 
    player["name"] = input("Player's name: ").strip(); 
    number_of_matches = int(input("Number of matches: ")); 
    player["goals_per_match"] = [];  

    for count in range(0,number_of_matches): 
        player["goals_per_match"].append(int(input(f"How many goals in match {count+1}? "))); 
    player["total_goals"] = sum(player["goals_per_match"]); 
    
    players.append(player.copy()); 
    
    resp = input("Do you want to continue? [y/n]: ").strip().lower(); 
    if(resp in "Nn"):
        break; 


#print(player); 
system("clear");
print("-="*40);
print("id   ", end=""); 
for key in players[0].keys(): 
    print(f"{key:<30}", end=""); 
print("\n" + "-"*30); 
 

for pos, pl in enumerate(players): 
    str_goals = ", ".join(str(goal) for goal in pl["goals_per_match"]); 
    # 
    print(f"{pos}", end="    "); 
    print(f"{pl['name']:<30}{str_goals:<30}{pl['total_goals']:<30}"); 
print("-"*30);

while True: 
    option = int(input("Select a number to show player's info. (999 to exit): "));  
    
    if option == 999: 
        break;
    else: 
        if(option not in range(0, len(players))): 
            while not option in range(0, len(players)): 
                print("-"*30);
                print("Invalid option")
                option = int(input("Select a number to show player's info. (999 to exit): ")); 
                if option == 999: 
                    break; 
        
        if option == 999: 
            break; 
        print(f" -- Data collection of the player called {players[option]["name"]}: "); 
        for pos, goals in enumerate(players[option]["goals_per_match"]): 
            print(f"In Match {pos+1} scored {goals} goals"); 

    print("-"*30);
    
    
print("<<< always come back >>>".upper()); 