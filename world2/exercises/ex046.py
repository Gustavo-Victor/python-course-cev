import time; 

for count in range(10, -1, -1):
    print(count); 
    time.sleep(1); 
    
    if(count == 0):
        print("The End"); 
    
    