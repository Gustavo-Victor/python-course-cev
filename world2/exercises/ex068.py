from random import randint; 

print("-="*30); 
print("Let's play odd or even"); 
print("-="*30); 

qtd_win = 0; 

while True: 
    sum_result = 0;
    random_num = randint(0, 9); 
    
    user_num = int(input("Enter an integer (0-9): ")); 
    if(user_num not in range(0,9)):
        while not user_num in range(0,9):
            print("Invalid number");
            user_num = int(input("Enter an integer (0-9): "));  
        
    choice = input("Even or Odd? [E/O] ").strip().lower();   
    if(choice not in "EeOo"): 
        while not choice in "EeOo": 
            print("Invalid choice"); 
            choice = input("Even or Odd? [E/O] ").strip().lower();

    sum_result = user_num + random_num; 
    result = "EVEN" if sum_result % 2 == 0 else "ODD"; 
    print("-"*30)
    print(f"You played {user_num} and the computer played {random_num}\nResult: {sum_result} ({result})"); 
    print("-"*30)
    
    if(result == "EVEN"):
        if(choice in "Ee"): 
             print("YOU WIN"); 
             print("Let's play again..."); 
             print("-="*30); 
             qtd_win += 1;
        else: 
            print("YOU LOSE");
            break;  
    else: 
        if(choice in "Oo"): 
             print("YOU WIN"); 
             print("Let's play again..."); 
             print("-="*30); 
             qtd_win += 1;
        else: 
            print("YOU LOSE");
            break; 
        
print(f"\nYou won {qtd_win} time(s)"); 
print("the end".upper()); 