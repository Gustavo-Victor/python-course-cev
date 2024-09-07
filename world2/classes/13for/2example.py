init = int(input("Init: "));
end = int(input("End: ")); 
step = int(input("Step: ")); 

if step == 0:
    print("Invalid step. Cannot count.");
else: 
    if(init < end): 
        if step < 0: 
            step *= -1; 
        for count in range(init, end+1, step):
            print(count); 
    elif(init > end):
        if(step > 0):
            step *= -1;
        for count in range(init, end-1, step): 
            print(count); 
    else: 
        print("Init and end are the same. Cannot count."); 
    
    