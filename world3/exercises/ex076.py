product_list = (
    ("Pencil", 1.75), 
    ("Eraser", 2.00), 
    ("Notebook", 15.90), 
    ("Pencil Case", 25.00), 
    ("Protractor", 4.20),
    ("Compass", 9.99),
    ("Backpack", 120.32), 
    ("Pens", 22.30), 
    ("Book", 34.90)
); 


print("-"*40);
print("{:^40}".format("list of prices".upper())); 
print("-"*40);

for product in product_list: 
    for item in product: 
        if(product.index(item) == 0): 
            print(f"{item:.<32}", end="");
        else: 
            print(f"${item:>6.2f}", end=""); 
    print(""); 