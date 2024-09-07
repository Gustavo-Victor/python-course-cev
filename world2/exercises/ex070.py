print("-"*30); 
print("very cheap store".upper()); 
print("-"*30);

cheapest_product = "";  
lowest_price = 1000000000000; 
products_over_1000_brl = 0;
total_purchase = 0;

while True: 
    product = input("\nName of the product: ").strip(); 
    if(not product): 
        while not product: 
            print("Invalid name"); 
            product = input("Name of the product: ").strip();

    
    price = float(input("Price: R$"));    
    if(price <= 0):
        while price <= 0: 
            print("Invalid price"); 
            price = float(input("Price: R$"));
            
    if(price > 1000): 
        products_over_1000_brl += 1; 
        
    if(price < lowest_price):
        lowest_price = price;
        cheapest_product = product;  
    
    total_purchase += price;     
    
    resp = input("Do you want to continue? [y/n]: "); 
    if(resp in "Nn"):
        break; 
    
print("-"*30); 
print("the end".upper()); 
print("-"*30);
print(f"Total purchase: {total_purchase:.2f}"); 
print(f"Number of products over R$ 1000: {products_over_1000_brl}"); 
print(f"The cheapest product is '{cheapest_product}' costing R$ {lowest_price:.2f}"); 
