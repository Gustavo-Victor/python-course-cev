from random import randint; 

random_numbers = (
    randint(1,10), 
    randint(1,10), 
    randint(1,10), 
    randint(1,10), 
    randint(1,10), 
); 

# highest_value = 0; 
# lowest_value = 10; 
highest_value = max(random_numbers); 
lowest_value = min(random_numbers); 

print("Generated numbers: ", end=" "); 
for item in random_numbers: 
    print(f"{item}", end=" "); 
    
print(f"\nHighest value: {highest_value}"); 
print(f"Lowest value: {lowest_value}"); 
# highest_value = 5; 
# lowest_value = 9; 
# list_of_numbers = []; 

# for count in range(0, 5): 
#     random_num = randint(1, 10);
#     list_of_numbers.append(random_num); 
    
#     if(random_num > highest_value): 
#         highest_value = random_num; 
        
#     if(random_num < lowest_value):
#         lowest_value = random_num;    
        
         
#     #print(random_num);  
# tuple_of_numbers = tuple(list_of_numbers); 
# print(f"\nNumbers created: {tuple_of_numbers}"); 
# print(f"Highest value: {highest_value}"); 
# print(f"Lowest value: {lowest_value}"); 


    
