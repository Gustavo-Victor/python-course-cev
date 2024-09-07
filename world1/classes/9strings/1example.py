sentence = 'Curso em Vídeo Python'; 
print(sentence); 

print(""" Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
      Pariatur laboriosam molestiae sit aliquid ducimus magnam consectetur illum deleniti commodi delectus quasi quam mollitia asperiores sunt quas, consequatur saepe nulla reiciendis!
      """)


# slicing 
print(sentence[9]); 
print(sentence[9:]); 
print(sentence[::3]); 
print(sentence[:7]); 


# analysis
print(len(sentence)); 
print(sentence.count('o')); 
print(sentence.count('e', 3, 12)); 
print(sentence.find('deo')); 
print('Curso' in sentence); 
print('curso' in sentence); 


# transformation
print(sentence.upper());
print(sentence.lower());
print(sentence.capitalize()); 
print(sentence.title()); 
print(sentence.replace('Python', 'Android'));
print('  Housenka no jutsu   '.strip()); 
print('  Housenka no jutsu   '.rstrip()); 
print('  Housenka no jutsu   '.lstrip()); 


# division
arr = sentence.split(); 
arr2 = sentence.split('Curso'); 
print(arr); 
print(arr2); 
new_string = '-'.join(arr); 
print(new_string);  
