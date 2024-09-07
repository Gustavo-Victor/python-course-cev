sentence = input("Enter a sentence: ").upper().strip();
print(); 


def is_a_palindrome(sentence = "arara"): 
    sentence_array = sentence.split(); 
    new_sentence = "".join(sentence_array); 
    inverted_sentence = ""; 

    for count in range(len(new_sentence) - 1, -1, -1):
        inverted_sentence += new_sentence[count]; 
                
    if(new_sentence == inverted_sentence):
        return True;
    else: 
        return False;


print(f"The sentence: {sentence}"); 
print(f"is a palindrome " if is_a_palindrome(sentence) else "is not a palindrome"); 



# print(new_sentence);
# print(sentence); 
# print(sentence_array);


