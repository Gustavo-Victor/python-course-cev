from time import sleep; 

def counter(start=0, end=10, step=1): 
    if(step < 0): 
        step *= -1;
    elif(step == 0): 
        step = 1; 
       
    print("-="*30); 
    print(f"From {start} to {end} going from {step} to {step}"); 
    
    if start < end:
        for count in range(start, end+1, step): 
            print(count, end=' ', flush=True); 
            sleep(0.5); 
    elif start > end:  
        for count in range(start, end-1, -step): 
            print(count, end=' ', flush=True); 
            sleep(0.5); 
    else: 
        print("Cannot make count"); 
    print("the end!".upper());                     


counter(1, 10, 1); 
counter(10, 0, 2); 

print("Now it's your turn!"); 
start = int(input("Start: ")); 
end = int(input("End: ")); 
step = int(input("Step: ")); 

counter(start, end, step); 








