from random import randint, choice; 

student1 = input("First student: "); 
student2 = input("Second student: "); 
student3 = input("Third student: "); 
student4 = input("Fourth student: "); 

student_list = [student1, student2, student3, student4]; 
# random_index = randint(0, (len(student_list) - 1)); 
# random_student = student_list[random_index]; 
random_student = choice(student_list); 

print(f"The chosen student is: {random_student}"); 

# print(student_list);
# print(len(student_list));  
# print(student_list[0]); 
# print(student_list[1]); 