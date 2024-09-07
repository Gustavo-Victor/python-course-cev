n1 = int(input("First number: ")); 
n2 = int(input("Second number: ")); 
n3 = int(input("Third number: ")); 

smallest = n1;  
if n2 < n1 and n2 < n3: 
    smallest = n2; 
if n3 < n1 and n3 < n2: 
    smallest = n3;  

greatest = n1; 
if n2 > n1 and n2 > n3: 
    greatest = n2; 
if n3 > n1 and n3 > n2:
    greatest = n3; 

print(""); 
print(f"Smallest: {smallest}"); 
print(f"Greatest: {greatest}"); 