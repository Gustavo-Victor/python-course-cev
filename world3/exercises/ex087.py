from os import system; 

my_array = []; 
line_array = []; 
even_numbers_sum = 0; 
third_column_sum = 0;


for l in range(0,3):
    for c in range(0,3):
        num = float(input(f"Enter a number for [{l}, {c}]: ")); 
        line_array.append(num); 
        
        if num % 2 == 0: 
            even_numbers_sum += num; 
        
        if c == 2: 
            third_column_sum += num;
        
    if(len(line_array) == 3): 
        my_array.append(line_array[:]); 
        line_array.clear(); 
        
highest_in_second_line = max(my_array[1]); 

system("clear"); 
print("-="*30); 
for l in range(0,3): 
    for c in range(0,3): 
        print(f"[{my_array[l][c]:^7}]", end=" ")
    print(); 
print("-="*30);
print(f"The sum of the values in the third column is {third_column_sum:.2f}"); 
print(f"The sum of all even values is {even_numbers_sum:.2f}"); 
print(f"The highest value in second line is {highest_in_second_line:.2f}");


    
