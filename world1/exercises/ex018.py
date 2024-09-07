from math import radians, sin, cos, tan; 

angle = float(input("Enter the value of the angle: ")); 
sin_value = sin(radians(angle));
cos_value = cos(radians(angle)); 
tan_value = tan(radians(angle)); 

print("Sin = {:.2f}".format(sin_value));  
print("Cos = {:.2f}".format(cos_value));  
print("Tan = {:.2f}".format(tan_value));  
