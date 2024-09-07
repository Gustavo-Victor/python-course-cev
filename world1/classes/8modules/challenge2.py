from math import pow, sqrt; 

opposite_leg = float(input("Opossite leg: ")); 
adjacent_leg = float(input("Adjacent leg: ")); 

aux = pow(opposite_leg, 2) + pow(adjacent_leg, 2); 
hypotenuse = sqrt(aux); 

print(f"\nOpposite leg = {opposite_leg}cm"); 
print(f"Adjacent leg = {adjacent_leg}cm"); 
print(f"Hypotenuse = {hypotenuse}cm"); 