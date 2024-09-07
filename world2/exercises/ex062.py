print("arithmetic progression generator".upper()); 
print("-="*20); 
first_term = int(input("First term: ")); 
reason = int(input("Reason: ")); 

count = 1; 
n_term = first_term; 
resp = 1; 
terms_qtd = 0;
nth_term = 10;  

while resp != 0:   
    while(count <= nth_term): 
        print(n_term, end=' -> ')
        n_term += reason; 
        count += 1; 
        terms_qtd += 1;
        
    print("PAUSE");
    resp = int(input("\nHow many more terms do you want to show? ")); 
    nth_term += resp; 

print(f"\nIn total, {terms_qtd} terms were displayed");
print("the end".upper()); 