def counter(i=0, e=10, s=1): 
    c = i;
    
    if (s < 0): 
        s *= -1; 
    elif s == 0: 
        s = 1;
    
    if i < e:        
        while c <= e:
            print(f"{c}", end="..");  
            c+=s; 
    else:
        while c >= e:
            print(f"{c}", end="..");  
            c-=s; 
    print("the end".upper()); 
        
        

counter.__doc__ = """ 
    -> Function that counts from an initial number to a final number with a custom jump number.
    :param i: init of the count 
    :param e: end of the count 
    :param s: step of the count
    :return: None
""";
print(counter.__doc__); 

counter(1, 10, 2); 
counter(10, 0, 2); 
counter();
print(help(counter))