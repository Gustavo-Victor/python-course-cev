from random import shuffle; 

student1 = str(input("First student: ")); 
student2 = str(input("Second student: ")); 
student3 = str(input("Third student: ")); 
student4 = str(input("Fourth student: ")); 

student_list = [student1, student2, student3, student4]; 
shuffle(student_list); 

print(f"\nOrder of presentation of works: "); 
# print(student_list); 
for student in student_list: 
    print(f"{student}"); 

