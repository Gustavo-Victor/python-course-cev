print("="*10 + " GUANABARA STORES " + "="*10); 
purchase_price = float(input("Purchase price: R$")); 

if(purchase_price < 0): 
    print("Invalid purchase price."); 
else:  
    print("PAYMEN METHODS");
    print("[ 1 ] Cash or check"); 
    print("[ 2 ] Cash on card"); 
    print("[ 3 ] Installments 2x"); 
    print("[ 4 ] Installments 3x or more"); 
    
    payment_method = int(input("What is your option? ")); 
    print("");
    number_of_installments = 0; 
    installment_price = 0.0;
    interest_on_purchase = 0; 
    discount_on_purchase = 0; 
    final_purchase_price = 0.0; 

    if(payment_method == 1): 
        discount_on_purchase = 10; 
        final_purchase_price = purchase_price * (1 - (discount_on_purchase / 100));
        print("Method: cash / check");
        print("Total: {:.2f}".format(final_purchase_price)); 
    elif(payment_method == 2): 
        discount_on_purchase = 5;
        final_purchase_price = purchase_price * (1 - (discount_on_purchase / 100));
        print("Method: cash on card");
        print("Total: {:.2f}".format(final_purchase_price)); 
    elif(payment_method == 3):
        number_of_installments = 2; 
        final_purchase_price = purchase_price; 
        installment_price = final_purchase_price / number_of_installments; 
        print("Method: installments 2x"); 
        print("Total: {} installments of R${:.2f} totaling R${:.2f}".format(number_of_installments, installment_price, final_purchase_price));  
        print(); 
    elif(payment_method == 4):  
        number_of_installments = int(input("How many installents? "));
        if(number_of_installments < 3 or number_of_installments > 12): 
            print("We accept installments in up to 12 installments..."); 
            number_of_installments = 12;
        
        interest_on_purchase = 20; 
        final_purchase_price = purchase_price * (1 + (interest_on_purchase / 100)); 
        installment_price = final_purchase_price / number_of_installments; 
        print(f"Method: installments {number_of_installments}x"); 
        print("Total: {} installments of R${:.2f} totaling R${:.2f}".format(number_of_installments, installment_price, final_purchase_price));
    else: 
        print("Invalid option. Canceled purchase.");