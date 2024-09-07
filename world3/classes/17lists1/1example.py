# create list
cars = ["Volvo", "BMW", "Audi", "Chevrolet", "Volkswagen"]; 

# print list 
print(cars); 

# iterate list 
for item in cars: 
    print(item, end=" | "); 
print(); 


# add to the end 
cars.append("Ford"); 
print(cars); 

# add to the beginning 
cars.insert(0, "Peugeot"); 
print(cars); 

# delete item 
del cars[0]; 
print(cars); 

# delete item by index
cars.pop(3); 
print(cars); 

# delete item by element 
cars.remove("Ford"); 
print(cars); 


