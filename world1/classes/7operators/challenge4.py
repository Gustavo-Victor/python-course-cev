meters = float(input("Enter a number: ")); 
kilometers = meters / 1000; 
hectometers = meters / 100; 
decameters = meters / 10; 
decimeters = meters * 10; 
centimeters = meters * 100; 
millimeters = meters * 1000; 

# print("{}m\n{}cm\n{}mm".format(meters, centimeters, millimeters))
print(f"The measurement of {meters}m corresponds to: "); 
print(f"{kilometers}km"); 
print(f"{hectometers}hm"); 
print(f"{decameters}dam"); 
print(f"{decimeters}dm"); 
print(f"{centimeters}cm"); 
print(f"{millimeters}mm"); 