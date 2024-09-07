value1 = float(input("Enter a number: ")); 
value2 = float(input("Enter another number: ")); 

sum_result = value1 + value2;
sub_result = value1 - value2; 
mult_result = value1 * value2; 
div_result = value1 / value2; 
integer_div_result = int(value1) // int(value2); 
rest_result = int(value1) % int(value2); 
pow_result = value1 ** value2; 

print("{} + {} = {}".format(value1, value2, sum_result)); 
print("{} - {} = {}".format(value1, value2, sub_result)); 
print("{} * {} = {}".format(value1, value2, mult_result)); 
print("{} / {} = {}".format(value1, value2, div_result)); 
print("{} // {} = {}".format(int(value1), int(value2), integer_div_result)); 
print("{} % {} = {}".format(int(value1), int(value2), rest_result)); 
print("{} ** {} = {}".format(value1, value2, pow_result)); 
