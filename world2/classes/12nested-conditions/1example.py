age = int(input("Enter your age: "));
 
 
if(age < 16): 
    print("Cannot vote");
elif(age <=17 or age > 65):
    print("Vote is optional");
else: 
    print("Vote is required");  
    
