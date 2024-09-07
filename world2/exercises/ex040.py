grade1 = float(input("First grade: ")); 
grade2 = float(input("Second grade: "));
average = (grade1 + grade2) / 2; 

print("\nAverage: {:.2f}".format(average)); 

if(average < 5):
    print("Failed student");
elif(average < 7): 
    print("Recovering student"); 
else:
    print("Approved student"); 
    
    