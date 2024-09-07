expression = str(input("Enter the expression: ")).strip(); 
pile = [];


for element in expression: 
    if element == "(":
        pile.append("("); 
    elif element == ")": 
        if len(pile) > 0: 
            pile.pop(); 
        else: 
            pile.append(")"); 
            break; 

print(); 
if len(pile) == 0: 
    print("The expresssion is right"); 
else: 
    print("The expression is wrong"); 