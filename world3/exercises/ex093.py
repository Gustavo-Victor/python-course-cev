player = {};


player["name"] = input("Player's name: "); 
number_of_matches = int(input("Number of matches: ")); 
player["goals_per_match"] = [];  

for count in range(0,number_of_matches): 
    player["goals_per_match"].append(int(input(f"How many goals in match {count+1}? "))); 

player["total_gols"] = sum(player["goals_per_match"]); 

#print(player); 
print("-="*30);
print(f"{player["name"]} played {len(player["goals_per_match"])} matches"); 
for pos, goals in enumerate(player["goals_per_match"]):
    print(f"  => In Match {pos + 1}, scored {goals} goals");  
print(f"Total of {player['total_gols']} goals"); 