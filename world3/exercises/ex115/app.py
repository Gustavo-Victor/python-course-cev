import lib.interface as interface; 
import lib.file as file; 
from time import sleep; 
from lib.input import read_int; 

filename = "people.txt"; 

if(not file.file_exists(filename)):
    file.create_file(filename); 


while True: 
    resp = interface.menu(["show people", "new person", "exit"]); 
    sleep(0.5); 

    if resp == 1: 
        file.read_file(filename); 
    elif resp == 2: 
        interface.header("new registration"); 
        person = {}; 
        person['name'] = input("Name: ").strip(); 
        person['age'] = read_int("Age: "); 
        file.insert(filename, person); 
    elif resp == 3: 
        print("\033[34m{}\033[m".format("the end".upper())); 
        break; 
    else: 
        print(f"\033[31mEnter a valid option\033[m"); 