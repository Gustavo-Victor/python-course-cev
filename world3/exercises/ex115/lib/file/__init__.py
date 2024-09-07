import lib.interface as interface; 


def file_exists(filename): 
    try: 
        f = open(filename, "rt"); 
        f.close(); 
    except FileNotFoundError:
       return False; 
    else: 
        return True;  
    
    
def create_file(filename, content=""): 
    try: 
        with open(filename, "wt+") as f: 
            f.write(content); 
    except Exception as err: 
        print(f"\033[31mError to create file - {err}\033[m");
    else: 
        print(f"\033[32mFile successfully created");  
        
        
def read_file(filename): 
    try: 
        f = open(filename, "rt");
    except FileNotFoundError: 
        print(f"\033[31mFile not found\033[m");
    else: 
        interface.header("registered people"); 
        # content = f.read(); 
        
        for line in f: 
            data = line.split(";"); 
            data[1] = data[1].replace('\n', ''); 
            print(f"{data[0]:<30}{data[1]:>3} years"); 
                
    finally: 
        f.close();
    
        
def insert(filename, data={}): 
    if(len(data.keys()) == 0): 
        data['name'] = "unknown"; 
        data["age"] = 21; 
    
    try: 
        with open(filename, "at") as f: 
            f.write(f"{data['name']};{data['age']}\n"); 
    except Exception as err: 
        print(f"\033[31mError to insert data - {err}\033[m");
    else: 
        print(f"\033[32m'{data["name"]}' registered\033[m");
    