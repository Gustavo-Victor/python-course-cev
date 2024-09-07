import os; 
from random import randint; 

resp = ''; 
student_list = []; 

while(resp != "n"):
    os.system("clear"); 
    student = input("Enter the name of the student: "); 
    student_list.append(student); 
    resp = input("\nWould you like to continue? [y/n] ");
    
 
random_index = randint(0, len(student_list) - 1); 
random_student = student_list[random_index]; 
print(f"The chosen student is: {random_student}"); 
# print(student_list); 