snack = ("Burger", "Orange juice", "Pizza", "Pudding");
print(snack[0]); 
print(snack[0:2]); 
print(snack[1:]); 
print(snack[-1]); 

# snack[4] = "Ice cream" error

for item in snack:
    print(item); 
    
for cont in range(0, len(snack)): 
    print(f"[{cont}] => {snack[cont]}"); 

for pos, item in enumerate(snack): 
    print(f"({pos}): {item}"); 
 
print(enumerate(snack))