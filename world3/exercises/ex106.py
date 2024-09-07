from time import sleep; 

command = ""; 
colors = {
    "black": "\033[m", 
    "red": "\033[0;30;41m",
    "green": "\033[0;30;42m",
    "yellow": "\033[0;30;31m",
    "blue": "\033[0;30;44m",
    "purple": "\033[0;30;45m",
    "white": "\033[7;30m", 
} 

def command_help(command):
    heading(f"Accessing the manual of the command called '{command}'", "blue");  
    print(colors["white"], end=""); 
    help(command); 
    print(colors["white"], end=""); 
    sleep(1); 
    
    
    
def heading(message, color="black"): 
    length = len(message) + 4; 
    
    print(colors[color], end=""); 
    print("~"*length); 
    print(f"{message:^{length}}".upper()); 
    print("~"*length); 
    print(colors[color], end=""); 
    sleep(0.4); 
    
    
    
while True: 
    heading("python help system", "green"); 
    command = input("Command or library > ").strip().lower(); 
    
    if command.lower() == "end": 
        break;
    else: 
        command_help(command); 
        

heading("see you", "red"); 
