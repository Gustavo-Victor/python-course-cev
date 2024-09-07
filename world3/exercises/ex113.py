def read_int(message="Enter an integer: "): 
    valid_num = False;
    result = 0; 
    
    while valid_num != True: 
        try: 
            num = input(message).lower().strip();
            
            if "," in num or "." in num: 
                ValueError("Invalid data type"); 
             
            result = int(num); 
        except (ValueError, TypeError): 
            print(f"\033[31mError - Invalid data type\033[m"); 
        except KeyboardInterrupt: 
            print(); 
            print(f"\033[31mError - Program interrupted\033[m"); 
        except Exception as error: 
            print(f"\033[31mError - {error.__cause__}\033[m");
        else: 
            valid_num = True;
    return result;  


def read_float(message="Enter a float number: "): 
    valid_num = False;
    result = 0; 
    
    while valid_num != True: 
        try: 
            num = input(message).lower().strip(); 
            
            if "," in num: 
                num = num.replace(",", "."); 
            
            result = float(num); 
        except (ValueError, TypeError): 
            print(f"\033[31mError - Invalid data type\033[m"); 
        except KeyboardInterrupt: 
            print(f"\033[31mError - Program interrupted\033[m"); 
        except Exception as error: 
            print(f"\033[31mError - {error.__cause__}\033[m");
        else: 
            valid_num = True;
        finally: 
            print(); 
    return result;  

    
num1 = read_int(); 
num2 = read_float(); 

print(f"Integer value entered: {num1}"); 
print(f"Float value entered: {num2}"); 