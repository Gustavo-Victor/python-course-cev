sum_result = 0;

for count in range(1, 500):
    if(count % 2 != 0 and count % 3 == 0): 
        sum_result += count;
        
print(f"The sum of all integers between 1 and 500 that are odd and multiples of 3 is: {sum_result}"); 