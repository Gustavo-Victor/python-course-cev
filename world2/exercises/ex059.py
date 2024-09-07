resp = 0; 
first_value = int(input("First value: ")); 
second_value = int(input("Second value: "));  

def menu():
    print("[ 1 ] Add"); 
    print("[ 2 ] Multiply");
    print("[ 3 ] Highest value");
    print("[ 4 ] New numbers")
    print("[ 5 ] Exit\n");

while resp != 5: 
    menu();
    resp = int(input("What is your option? ")); 
    
    if(resp == 1): 
        sum_result = first_value + second_value;
        print(f"{first_value} + {second_value} = {sum_result}"); 
    elif(resp == 2): 
        multiplication_result = first_value * second_value;
        print(f"{first_value} x {second_value} = {multiplication_result}"); 
    elif(resp == 3):
        highest_value = first_value; 
        if(second_value > first_value): 
            highest_value = second_value;
        print(f"Higest value: {highest_value}");
    elif(resp == 4): 
        first_value = int(input("First value: ")); 
        second_value = int(input("Second value: "));    
    elif(resp == 5):
        break; 
    else: 
        print("Invalid option");
        continue;        

print("\nThe end"); 