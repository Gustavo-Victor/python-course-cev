print("="*30); 
print("{:^30}".format('Banco Cev'.upper())); 
print("="*30);
 
num = int(input("Which value would you like to withdraw? ")); 
total = num; 
current_banknote = 50; 
qtd_banknotes = 0;
 

while True: 
    if(total >= current_banknote):
        total -= current_banknote; 
        qtd_banknotes += 1; 
    else: 
        if(qtd_banknotes > 0):
            print(f"Total of {qtd_banknotes} bills of R$ {current_banknote}"); 
            
        if(current_banknote == 50): 
            current_banknote = 20; 
        elif(current_banknote == 20):
            current_banknote = 10; 
        elif(current_banknote == 10):
            current_banknote = 5;
        elif(current_banknote == 5): 
            current_banknote = 2;
        elif(current_banknote == 2):
            current_banknote = 1;
        qtd_banknotes = 0;
        if(total == 0): 
            break;