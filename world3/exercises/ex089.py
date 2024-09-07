students = [];


while True: 
    student_data = []; 
    grades = []; 
    
    name = input("Name: ");
    student_data.append(name); 
     
    for count in range(0, 2): 
        grades.append(float(input(f"Grade {count + 1}: "))); 
    
    student_data.append(grades[:]);
    students.append(student_data[:]); 
    
    # if(len(grades) == 2):
    #     grades.clear(); 
    #     student_data.clear();   

    resp = input("Do you want to continue? [y/n] ").strip().lower();
    if(resp in "Nn"): 
        break; 
    

print("-="*40); 
print("{} {:<14} {}".format("No.", "name".upper(), "average".upper())); 
    
print("-"*30); 
for pos, student in enumerate(students): 
    print("{:<3} {:<14} {:.2f}".format(pos, student[0], (sum(student[1]) / len(student[1])))); 


while True: 
    print("-"*30); 
    option = int(input("Select a student to show information. 999 to exit: "));
    
    if(option == 999): 
        break; 
    
    if(option not in range(0, len(students))): 
        while not option in range(0, len(students)): 
            print("Invalid number"); 
            option = int(input("Select a student to show information: "));

    print(f"{students[option][0]}'s grades: {students[option][1]}"); 
    
    
print("\nthe end".upper()); 