def escreva(msg): 
    line_length = len(msg) + 4; 
    
    print("~"*line_length); 
    print(f"{msg:^{line_length}}");
    print("~"*line_length); 
    
    
escreva("Gustavo Guanabara");
escreva("Curso de Python no Youtube");  
escreva("Cev"); 