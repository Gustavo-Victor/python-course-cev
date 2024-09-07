resp = "";
total = 0; 
qtd_numbers = 0;
average = 0;
highest_number = 0;
lowest_number = 5000; 

while resp != 'n': 
    num = float(input("\nEnter a number: ")); 
    total += num; 
    qtd_numbers +=1;
    
    if(num > highest_number):
        highest_number = num; 
        
    if(num < lowest_number):
        lowest_number = num;
        
    resp = input("Do you want to continue? [y/n]").strip().lower(); 
    
    
average = total / qtd_numbers; 
print("\nYou entered {} numbers and the average is {:.2f}".format(qtd_numbers, average)); 
print("The highest value was {:.2f} and the lowest value was {:.2f}".format(highest_number, lowest_number)); 


    