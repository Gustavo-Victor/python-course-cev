people = [
    ['João', 19],
    ['Pedro', 20],
    ['Thiago', 21],
    ['Jonas', 22],
    ['Miquéias', 23],
]; 

print("-"*20); 
print("Customers: "); 
print("-"*20); 

for person in people:
    print(f"{person[0]:<13} | {person[1]:>4}"); 
    