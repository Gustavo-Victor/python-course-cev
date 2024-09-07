from urllib import request, error; 


def main(): 
    try: 
        website_url = input("URL: ").lower().strip(); 
    except KeyboardInterrupt: 
        print(f"\033[31mProgram interrupted\033[m");  
    except Exception as e: 
        print(f"\033[31mError - {e.__cause__}\033[m");   
    else: 
        request_url(website_url); 


def request_url(url): 
    try: 
        res = request.urlopen(url); 
        print(res); 
    except error.URLError: 
        print(f"\033[31mURL is not available\033[m"); 
    except Exception as e: 
        print(f"\033[31mError - ({e.__cause__})\033[m"); 
    else: 
        print(f"\033[32mURL is available\033[m"); 
        

main(); 
 
