def double_list(list): 
    pos = 0; 
    list_copy = list[:];
    
    while pos < len(list_copy): 
        list_copy[pos] *= 2; 
        pos+=1;
        
    return list_copy; 


result = double_list([1,2,3,4,5]); 
print(result);   
    