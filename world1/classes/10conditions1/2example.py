grade1 = float(input("First grade: ")); 
grade2 = float(input("Second grade: ")); 
average = (grade1 + grade2) / 2; 

print("Average: {:.2f}".format(average)); 
if(average >=6):
    print("Your average is good, congratulations!"); 
else: 
    print("Your average is not good, try harder"); 
# print("Approved" if average >=7 else "Failed");




