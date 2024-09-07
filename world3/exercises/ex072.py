# from num2words import num2words; 

# num = int(input("Digite um número entre 0 e 20: "));

# if(num not in range (0, 21)): 
#     while not num in range(0, 21):
#         print("Número inválido");  
#         num = int(input("Digite um número entre 0 e 20: "));
    

# num_ptbr = num2words(num, lang='pt-br');
# num_en = num2words(num, lang="en-us"); 
# print(f"\nVocê digitou o número: {num_ptbr}") 
# print(f"You entered the number: {num_en}"); 

numbers_in_full = ("zero", "um", "dois", "três", "quatro",
                  "cinco", "seis", "sete", "oito", "nove",
                  "dez", "onze", "doze", "treze", "quatorze",
                  "quinze", "dezesseis", "dezessete", "dezoito", "dezenove",
                  "vinte"); 

num = int(input("Digite um número inteiro entre 0 e 20: ")); 

if(num not in range(0, 21)): 
    while not num in range(0, 21): 
        num = int(input("Digite um número inteiro entre 0 e 20: ")); 

number_in_full = numbers_in_full[num]; 
print(f"\n Você digitou: {number_in_full}");