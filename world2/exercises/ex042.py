segment1 = float(input("First segment: ")); 
segment2 = float(input("Second segment: ")); 
segment3 = float(input("Third segment: ")); 


if(segment1 < segment2 + segment3 and segment2 < segment1 + segment3 and segment3 < segment1 + segment2): 
    triangle_type = ""; 

    if(segment1 == segment2 == segment3):
        triangle_type = "equilateral"; 
    elif(segment1 != segment2 != segment3 != segment1):
        triangle_type = "scalene"; 
    else: 
        triangle_type = "isosceles"; 
    print(f"The above segments can form a(n) {triangle_type} triangle.");
    
else: 
    print("The above segments cannot form a triangle."); 
     
    