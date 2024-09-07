def div(a=1, b=1): 
    return a / b; 


def main(): 
    try:
        num1 = float(input("Number 1: ")); 
        num2 = float(input("Number 2: ")); 
        result = div(num1, num2); 
    except (ValueError, TypeError): 
        print(f"Value / type error"); 
    except ZeroDivisionError: 
        print(f"Division by zero");
    except KeyboardInterrupt: 
        print();
        print(f"Program interrupted");  
    except Exception as error: 
        print(f"Error - {error.__cause__}"); 
    else:
        print("OK"); 
        print(f"{num1} / {num2} = {result}"); 
    finally:
        print("-"*30); 
        print("the end".upper()); 


main(); 