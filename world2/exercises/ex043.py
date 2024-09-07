weight = float(input("What is your weight in kilograms? ")); 
height = float(input("What is your height in meters? ")); 
bmi = weight / (height ** 2);

print(f"\nBMI: {bmi}");

if(bmi < 18.5): 
    print("Result: underweight"); 
elif(bmi < 25): 
    print("Result: normal weight"); 
elif(bmi < 30): 
    print("Result: overweight"); 
elif(bmi < 40):
    print("Result: obesity"); 
else: 
    print("Result: morbid obesity"); 