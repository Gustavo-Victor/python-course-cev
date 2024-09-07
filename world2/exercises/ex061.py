print("arithmetic progression generator".upper()); 
print("-="*20); 
first_term = int(input("First term: ")); 
reason = int(input("Reason: ")); 


count = first_term; 
# tenth_term = first_term + (10 - 1) * reason; 
n_term = first_term; 

while(count <= 10): 
    print(n_term, end=' -> ')
    n_term += reason; 
    count += 1; 

print("the end".upper()); 