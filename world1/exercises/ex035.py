print("-="*20); 
print("TRIANGLE ANALYZER");
print("-="*20); 

l1 = float(input("1st straight line: ")); 
l2 = float(input("2nd straight line: ")); 
l3 = float(input("3rd straight line: "));

print("");

if(l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2):
    print("The segments informed CAN form a triangle."); 
else: 
    print("The segments informed CANNOT form a triangle."); 
    