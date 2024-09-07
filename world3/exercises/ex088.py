from random import randint; 

print("-"*30); 
print("{:^30}".format("mega sena game").upper()); 
print("-"*30); 


games_array = [];
game = [];  
games_qtd = int(input("How many games would you like to generate? ")); 

if(games_qtd <=0): 
    while(games_qtd <=0): 
        print("Invalid value"); 
        games_qtd = int(input("How many games would you like to generate? ")); 


for count in range(0, games_qtd): 
    while True:
        if(len(game) == 6): 
            games_array.append(game[:]); 
            game.clear(); 
            break; 
        
        random_num = randint(1, 60);  
        
        if random_num in game: 
            while random_num in game: 
                random_num = randint(1, 60);
        else:       
            game.append(random_num); 

    
        
    
        
        
print("-="*3 + f" Drawing {games_qtd} games ".upper() + "-="*3); 
for pos, game in enumerate(games_array): 
    print(f"Game {pos + 1}: {game}"); 
print("-="*5 + " < good luck! > ".upper() + "-="*5); 