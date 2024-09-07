distance = int(input("How far is your trip? ")); 
total_price = 0; 
price_per_km = 0; 

if(distance <= 200): 
    price_per_km = 0.50; 
else: 
    price_per_km = 0.45; 
    
total_price = distance * price_per_km; 

print(f"You're about to start a 150 km journey."); 
print("And the price of ticket will be R$ {:.2f}".format(total_price)); 