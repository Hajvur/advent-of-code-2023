
def day2(input):
    sum = 0
    with open(input) as file:
        counter = 1
        for line in file:
            flag = 1 
            line_game_count = line.split(": ")
            
            for x in line_game_count[1].split("; "):
                for k in x.split(", "):
                    elements = k.split()
                    if elements[1] == "blue" and int(elements[0]) > 14:
                        flag = -1
                        break
                    if elements[1] == "red" and int(elements[0]) > 12:
                        flag = -1
                        break
                    if elements[1] == "green" and int(elements[0]) > 13:
                        flag = -1
                        break
            if flag ==1:
                sum += counter 
            counter += 1
            print(f"sum = {sum}")

day2("input.txt")