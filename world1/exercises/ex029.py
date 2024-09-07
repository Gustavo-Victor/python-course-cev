car_speed = int(input("What is the speed of the car? ")); 


if(car_speed > 80): 
    permitted_speed = 80; 
    fine_per_kilometer = 7;
    speed_diff = car_speed - permitted_speed; 
    total_fine = speed_diff * fine_per_kilometer; 
    print(f"FINED! You exceeded the permitted limit of {permitted_speed} km/h"); 
    print(f"You must pay a fine of R$ {total_fine}"); 

print("Have a nice day and drive safely!"); 
