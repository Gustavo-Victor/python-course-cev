my_favorite_languages = ['JavaScript', 'Python', 'PHP', 'Ruby']; 

my_dict = {
    'first_name': 'Gustavo',
    'last_name': 'Victor',
    'hobbies': ['Play guitar', 'Watch TV', 'Animes', 'Exercise'],
    'married': False,  
}; 

print(my_dict.items()); 


for item in my_favorite_languages:
    print(item);
    
 
for key, value in my_dict.items(): 
    print(f'{key}: {value}');