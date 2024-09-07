def calc_average(*numbers, show=False): 
    grades_sum = 0;  
    statistics_dict = {};
    
    for number in numbers: 
        grades_sum += number; 
    
    statistics_dict["total"] = len(numbers); 
    statistics_dict["highest_grade"] = max(numbers); 
    statistics_dict["lowest_grade"] = min(numbers); 
    statistics_dict["average"] = (grades_sum / len(numbers)); 
    
    if show:    
        if (statistics_dict["average"] < 5): 
            statistics_dict["situation"] = "bad"; 
        elif (statistics_dict["average"] < 7): 
            statistics_dict["situation"] = "regular"; 
        else: 
            statistics_dict["situation"] = "good"; 
        statistics_dict["situation"] = statistics_dict["situation"].upper();
    
    return statistics_dict; 


print("-"*30); 
resp = calc_average(5.5, 8, 7, 10, show=True);
resp2 = calc_average(4, 3, show=True); 
resp3= calc_average(4, 3, 5, 8);
print(resp); 
print(resp2); 
print(resp3); 