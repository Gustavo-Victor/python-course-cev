movies = [
    {"id": 1, "title": "Star Wars - IV", "year": 1977}, 
    {"id": 2, "title": "Avengers", "year": 2012}, 
    {"id": 3, "title": "Matrix", "year": 1999}, 
]; 


for movie in movies: 
    for key, value in movie.items(): 
        print(f"{key}: {value}", end=" | ");
    print("\n"+"-"*30);  