from random import randint; 
from operator import itemgetter; 
from time import sleep; 

players = []; 
player = {}; 

print("\nDrawn values: "); 
for count in range(0,4):
    player["name"] = "player" + (str(count+1));
    player["move"] = randint(1,6); 
    sleep(0.8); 
    print(f"{player['name']} rolled dice number {player['move']}"); 
    players.append(player.copy()); 
    
    
    
#sorted_players = sorted(players, key=lambda d: d['move'], reverse=True); 
sorted_players = sorted(players, key=itemgetter("move"), reverse=True); 
 
#print(players); 
print("-="*15);
print("  == {} ==".format("Players Ranking".upper())); 
for pos, item in enumerate(sorted_players):
    print(f"  {pos + 1}° place: {item['name']} ({item["move"]})");     
#print(sorted_players); 