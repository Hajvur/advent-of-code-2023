def multiply(list):
    nums = 1
    for x in list:
        nums = nums * x
    return nums

def day2(input):
    
    sum = 0
    with open(input) as file:
        counter = 1
        for line in file:
            num_cubes = {
                "blue" : 0,
                "red" : 0,
                "green" : 0
                }
            line_game_count = line.split(": ")
            
            for x in line_game_count[1].split("; "):
                for k in x.split(", "):
                    elements = k.split()
                    if num_cubes[elements[1]] < int(elements[0]):
                        num_cubes[elements[1]] = int(elements[0])
            

            sum = sum + multiply([x for x in num_cubes.values()])    
            print("")
            
    print(f"sum = {sum}")
            


day2("input.txt")