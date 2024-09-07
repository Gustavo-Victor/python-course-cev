print("Heaviest and lowest weight among 5 people");
print(); 

highest_weight = 0; 
lowest_weight = 800;


for count in range(1, 6): 
    weight = float(input(f"{count}° weight: "));
    
    if(weight < 0):
        while(weight < 0):
            print("Invalid weight"); 
            weight = float(input(f"{count}° weight: ")); 
        
    if(weight > highest_weight):
        highest_weight = weight; 
        
    if(weight < lowest_weight):
        lowest_weight = weight; 
        
        
print("\nHighest weight: {:.2f}kg".format(highest_weight)); 
print("Lowest weight: {:.2f}kg".format(lowest_weight))