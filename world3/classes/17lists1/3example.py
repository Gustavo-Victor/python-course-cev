num = [2,5,9,1];
print(num);
  
num[2] = 3; 
print(num); 

num.append(7); 
print(num); 

num.sort(reverse=True); 
print(num); 

num.insert(2, 0); 
print(num); 

num.pop(2);
print(num);  

print(f"That list has {len(num)} elements"); 


for position, item in enumerate(num): 
    print(f"[{position}]: {item}...");
    
a = [2,3,4,5]; 
#b = a - in this cse, b is connected to a, and changing b chages a 
b = a[:]; 
b[2] = 8; 
print(a); 
print(b); 

