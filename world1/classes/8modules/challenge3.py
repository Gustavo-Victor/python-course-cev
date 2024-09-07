from math import sin, cos, tan, radians; 

angle = float(input("Enter the value of the angle: "));
angle_in_radians = radians(angle); 
sin_value = sin(angle_in_radians); 
cos_value = cos(angle_in_radians); 
tan_value = tan(angle_in_radians); 

print(f"\n{angle}° = {angle_in_radians} radians"); 
print(f"Sin {angle}° = {sin_value}");
print(f"Cos {angle}° = {cos_value}");
print(f"Tan {angle}° = {tan_value}"); 