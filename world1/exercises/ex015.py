km_driven = float(input("How many kilometers has the car driven? ")); 
days_qtd = int(input("How many days was the car rented? ")); 

cost_per_day = 60.0;
cost_per_km_driven = 0.15;  

rental_cost = (km_driven * cost_per_km_driven) + (days_qtd * cost_per_day); 

print(f"\nTotal rental cost: ${rental_cost}"); 

