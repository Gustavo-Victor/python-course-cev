from random import randint; 

print("Your options: "); 
print("[ 0 ] ROCK"); 
print("[ 1 ] PAPER"); 
print("[ 2 ] SCISSORS");
user_move = int(input("What's your move? ")); 
possible_options = ["ROCK", "PAPER", "SCISSORS"]; 
print(); 

if(user_move not in [0, 1, 2] or not user_move): 
    print("Invalid option. Game canceled."); 
else:  
    computer_move = randint(0, 2);
    result = ""; 
    
    print("JO");
    print("KEN");
    print("PO!!!");
    print("-="*15);
        
    if(user_move == computer_move + 1 or user_move == 0 and computer_move == 2):
        result = "Player Win"; 
    elif(computer_move == user_move + 1 or computer_move == 0 and user_move == 2):
        result = "Computer Win"; 
    else: 
        result = "Tie"; 
    
    print(f"Player: {possible_options[user_move]}"); 
    print(f"Computer: {possible_options[computer_move]}"); 
    print(f"Result: {result}"); 
    
    print("-="*15);
    
    
    




