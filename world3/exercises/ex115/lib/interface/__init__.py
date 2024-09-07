import lib.input as input; 


def line(len=42): 
    return ("-"*len); 


def header(txt="menu", size=42):
    txt = txt.upper();  
    print(line(size));  
    print(f"\033[34m{txt:^{size}}"); 
    print("\033[m", end="")
    print(line(size));  
    

def menu(list): 
    header("main menu"); 
    for pos, item in enumerate(list): 
        print(f"\033[36m{pos + 1} - {str(item).title()}"); 
    
    print("\033[m", end="");    
    print(line()); 
    resp = input.read_int("Your option: ");
    print("\033[m", end="");
    print(line()); 
    return resp;  