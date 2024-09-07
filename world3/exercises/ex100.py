from random import randint;
from time import sleep; 

numbers = []; 

def draw_values(list): 
    print("Drawing 5 values of the list: ", end=""); 
    for count in range(0,5): 
        random_num = randint(0,9);
        if(random_num in list):
            while random_num in numbers: 
                random_num = randint(0,9);             
        print(random_num, end=" ", flush=True);
        sleep(0.2); 
        list.append(random_num);
    print("DONE!"); 
        
        
def sum_even_values(list): 
    s = 0;
    for item in list: 
        if item % 2 == 0: 
            s += item; 
    sleep(0.2);             
    print(f"Adding the even values in the list {list}, the sum is {s}", flush=True); 
        
# print(numbers); 
draw_values(numbers); 
sum_even_values(numbers); 
