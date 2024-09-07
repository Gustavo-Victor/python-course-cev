sentence = input("Enter a sentence: ").lower().strip(); 

letter_a_qtd = sentence.count('a'); 
first_a_position = sentence.find('a') + 1; 
last_a_position = sentence.rfind('a') + 1; 

print(f"Analysing the sentence..."); 
print(f"The letter 'A' appears {letter_a_qtd} time(s)."); 
print(f"The letter 'A' first appears in position {first_a_position}"); 
print(f"The letter 'A' last appears in position {last_a_position}"); 


