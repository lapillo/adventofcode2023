springs = []
dammaged = []
completed = []
  
def get_end(start, number, i_spring):
    return start + dammaged[i_spring][number]

def can_move(start, number,i_spring):
    return springs[i_spring][start]!="#"

def not_contain(start,end,sign,i_spring):
    return (springs[i_spring][start:end].count(sign)==0)

def generate_options(i_start, number,i_spring):
    spring_len = len(springs[i_spring])
    if number == len(dammaged[i_spring]):
        if (not_contain(i_start-1,len(springs[i_spring]),"#",i_spring)):
            completed.append(1)
            return True
        return False 
    
    for start in range(i_start, spring_len):
        if can_place(start,number, i_spring):
            generate_options(get_end(start, number,i_spring)+1,number+1,i_spring)
        if can_move(start, number,i_spring) is False:
            break


def can_place(start, number,i_spring):
    x1 = start
    x2 = get_end(start, number,i_spring)
    
    if x2 > len(springs[i_spring]):
        return False
    return  all([springs[i_spring][x1:x2].count(".")==0   ,x1 == 0 or springs[i_spring][x1-1] not in ["#"] , x2 == len(springs[i_spring]) or springs[i_spring][x2] not in ["#"] ])
 
 
if __name__ == '__main__': 
 
    file = open("adventofcode2023/zadanie_12/input_example.txt","r")
    map = file.read().split("\n")
    
    
    for l in map:
        springs.append(l.split()[0])
        dammaged.append([int(x) for x in l.split()[1].split(",")])
    
    
    
    
    for i_spring in range(len(springs)):
        generate_options(0,0,i_spring)
        
    print(len(completed))