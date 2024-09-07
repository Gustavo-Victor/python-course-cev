total = 0;
even_numbers_qtd = 0;

for count in range(1, 6+1):
    num = int(input(f"{count}° number: "));
    
    if(num % 2 == 0):
        even_numbers_qtd += 1;
        total += num; 
        
        
print(f"\nQuantity of even numbers: {even_numbers_qtd}"); 
print(f"Total sum of even numbers: {total}"); 