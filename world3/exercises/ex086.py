my_array = []; 
line_array = []; 

for l in range(0,3):
    for c in range(0,3):
        num = int(input(f"Enter a number for [{l}, {c}]: ")); 
        line_array.append(num); 
        
    if(len(line_array) == 3): 
        my_array.append(line_array[:]); 
        line_array.clear(); 

print("-="*30); 
for l in range(0,3): 
    for c in range(0,3): 
        print(f"[{my_array[l][c]:^5}]", end=" ")
    print(); 
    
