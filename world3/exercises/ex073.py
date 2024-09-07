leaderboard = (
    "Fortaleza", "Botafogo", 
    "Palmeiras", "Flamengo",
    "São Paulo", "Bahia",
    "Cruzeiro", "Atlético-MG",
    "Athletico-PR", "Vasco da Gama",
    "Internacional", "Juventude",
    "Grêmio", "Bragantino", 
    "Criciúma", "Fluminense", 
    "EC Vitória", "Corinthians",
    "Cuiabá", "Chapecoense"
    ); 

print("-"*30);
print(f"Os cinco primeiros colocados são: {leaderboard[:5]}"); 
print("-"*30);
print(f"Os últimos quatro colocados são: {leaderboard[-4:]}");
print("-"*30);
print(f"A tabela em ordem alfabética: {sorted(leaderboard)}"); 
print("-"*30);
print(f"O time 'Chapecoense' está na {leaderboard.index('Chapecoense') + 1}ª posição");
print("-"*30);