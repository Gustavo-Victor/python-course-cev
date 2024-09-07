person = list(); 
person.append('Gustavo'); 
person.append(40); 
print(person); 


people = []; 
people.append(person[:]); # people.append(person) - connected variables - bugs
people.append(['Guilherme', 42]); 
# person[0] = 'Maria'; // connected variables - it can generate bugs
# people.append(person); 
person[0] = 'Maria'; 
person[1] = 39; 
people.append(person[:]); 
print(people); 