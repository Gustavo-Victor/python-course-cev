total = 0; 
flag = 999; 
qtd_numbers = 0;
num = 0;

while(not num == flag): 
    num = float(input("Enter a number: ")); 
    
    if(num != flag):
        qtd_numbers +=1;
        total += num; 

print(f"\nYou entered {qtd_numbers} numbers and the sum of all them is {total}"); 