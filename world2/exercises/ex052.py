num = int(input("Enter a number: ")); 
print(); 

def print_list(list): 
    for item in list: 
        print(f"{item}", end=" "); 

def check_if_num_is_prime(num): 
    divisors = []; 
    qtd_div = 0; 
    if (num == 0): 
        print("0 is not a prime number");  
        return ; 
    elif(num == 1): 
        print(f"{num} is a prime number"); 
        print(f"Divisors: {num}");   
        return;
    elif(num < 0):
        print("There is no negative prime number");
        return ; 
    else:
        for count in range(1, num + 1): 
            if(num % count == 0):
                divisors.append(count); 
                qtd_div += 1; 

    if(qtd_div == 2): 
        print(f"{num} is a prime number");          
    else: 
        print(f"{num} is not a prime number"); 
    print("Divisors: ", end=""); 
    print_list(divisors); 
    
check_if_num_is_prime(num); 

