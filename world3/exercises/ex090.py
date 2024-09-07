student = {}; 

student["name"] = input("Name: "); 
student["average"] = float(input("Average: ")); 

print("-="*30); 
if(student["average"] < 5): 
    student["situation"] = "Failed"; 
elif(student["average"] < 7): 
    student["situation"] = "Recovering"; 
else: 
    student["situation"] = "Approved"; 
    
for key, value in student.items(): 
    print("- {}: {}".format(f"{key}".capitalize(), value)); 