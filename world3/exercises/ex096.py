def header(msg): 
    print(f"{msg}".title()); 
    print("-"*20); 
    

def calculate_area(w, l): 
    area = w * l; 
    print(f"The area of a {w:.2f}m x {l:.2f}m plot is {area:.2f}m^2")

header("land control"); 
width = float(input("Width: ")); 
length = float(input("Length: ")); 

calculate_area(width, length); 
