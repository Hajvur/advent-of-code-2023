def day1(input):
    final_list = []
    zamiana_jebanego_edge_case = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "4",
    "five": "5e",
    "six": "6",
    "seven": "7n",
    "eight": "e8t",
    "nine": "n9e"}
    
    with open(input) as file:
        for line in file:
            for word in zamiana_jebanego_edge_case:
                line = line.replace(word,zamiana_jebanego_edge_case[word])
            placeholder = []
            for char in line:
                if char.isnumeric():
                    placeholder.append(char)
            
            if placeholder != []: 
                final_list.append((int(placeholder[0])*10)+int(placeholder[-1]))
            else:
                continue
            
            
    print(sum(final_list))
        
day1("input.txt") 
        

        
        
        

                
 