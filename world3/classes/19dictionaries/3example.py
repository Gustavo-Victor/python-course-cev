state = dict(); 
country = list(); 


for count in range(0,3): 
    state['fu'] = input("Federative Unit: ").strip().title();
    state["acronym"] = input("Acronym: ").strip().lower(); 
    country.append(state.copy()); 
    
print(country); 
     