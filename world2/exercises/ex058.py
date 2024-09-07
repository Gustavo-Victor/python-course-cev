from random import randint; 

game_over = False; 
random_number = randint(0, 10); 
attempts = 1;

print("I am your computer"); 
print("I thought of a number from 0 to 10\nCan you guess which one it was? "); 
guess = int(input("\nWhat is your guess? ")); 

while not game_over: 
    print(); 
    if(random_number > guess): 
        print("More. Try one more time..."); 
    elif(random_number < guess): 
        print("Less. Try one more time..."); 
    else: 
        game_over = True; 
    
    guess = int(input("What is your guess? ")); 
    attempts += 1;

print("\nCongratulations, you got it right!"); 
print(f"It took {attempts} attempts"); 

