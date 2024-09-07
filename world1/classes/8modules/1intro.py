# import math;
from math import sqrt, ceil, floor; 


num = float(input("Enter a number: ")); 
sqrt_result = sqrt(num); 
sqrt_ceil_result = ceil(sqrt_result); 
sqrt_floor_result = floor(sqrt_result); 

print(f"The square root of {num} = {sqrt_result}"); 
print(f"Ceil: {sqrt_ceil_result}"); 
print(f"Floor: {sqrt_floor_result}"); 
 