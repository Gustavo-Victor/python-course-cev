total = 0;
qtd_numbers = 0;

while True: 
    num = int(input("Enter a number: ")); 
    if(num == 999): 
        break; 
    qtd_numbers +=1;
    total += num; 
    
print(f"\nNumbers entered: {qtd_numbers}"); 
print(f"Total: {total:.2f}"); 
    