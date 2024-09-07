words = (
    "aprender", 
    "programar", 
    "linguagem", 
    "python", 
    "curso", 
    "gratis", 
    "estudar", 
    "praticar",
    "trabalhar", 
    "mercado", 
    "programador", 
    "futuro"
); 

vogals = ("a", "e", "i", "o", "u"); 

for item in words: 
    print(f"Na palavra {item.upper()} temos as vogais: ", end=" "); 
    for letter in item: 
        if(letter.lower() in vogals): 
            print(letter, end=" "); 
    print("")