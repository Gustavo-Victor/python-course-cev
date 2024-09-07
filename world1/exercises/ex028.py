from random import randint; 

random_num = randint(0, 5); 

print("-" + "=--"*18 + "=-"); 
print("I will think of a number from 0 to 5. Try to guess...");
print("-" + "=--"*18 + "=-"); 

user_num = int(input("What number did I just think of? ")); 
print(f"\nPROCESSING..."); 

if(user_num == random_num):
    print("CONGRATULATIONS, You win!"); 
else: 
    print(f"I WIN! I thought of number {random_num} and not {user_num}"); 
# print(random_num);
 

