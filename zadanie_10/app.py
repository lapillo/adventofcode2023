
directions = {"N": (0,-1), "E":(1,0),"S":(0,1),"W":(-1,0)}
pipes = {"|":"NS", "-":"EW", "L":"NE", "J":"NW","7":"SW","F":"SE"}
connections = {"N":"S", "E":"W", "S":"N", "W":"E"}
start_symbol="S"

def get_start(pipe_map):
    for y,line in enumerate(pipe_map):
        if line.count("S")>0:
            return(line.index(start_symbol),y)

# def move_next(pipe_map,current_poz,direction):
#     steps=0
#     new_poz = (current_poz[0]+directions[direction][0],current_poz[1]+directions[direction][1])
#     new_pipe = pipe_map[new_poz[1]][new_poz[0]]
    
#     if (new_pipe in pipes):
#         if pipes[new_pipe].count(connections[direction])>0:
#             steps+=1
#             steps +=move_next(pipe_map, new_poz,pipes[new_pipe].replace(connections[direction],""))
#     return (steps)


def move_next(pipe_map,current_poz,direction):
    steps=0
    new_poz = (current_poz[0]+directions[direction][0],current_poz[1]+directions[direction][1])
    new_pipe = pipe_map[new_poz[1]][new_poz[0]]
    
    if (new_pipe in pipes):
        if pipes[new_pipe].count(connections[direction])>0:
            steps+=1
            return (pipes[new_pipe].replace(connections[direction],""),new_poz)
    return(False)


start_paths = [["N",[],0],["E",[],0],["S",[],0],["W",[],0]]

if __name__ == '__main__':
    
    file = open("adventofcode2023/zadanie_10/input.txt","r")
    pipe_map = file.read().split("\n")
    

    #create map{path: map{L:x, R:y}}
    #numbers_list=[[list(reversed([int(n) for n in x.split()]))] for x in list_numbers]    
    
    
    start_poz = get_start(pipe_map)
    
    #set starting poz for all starting paths
    for x in start_paths:
        x[1]= start_poz
    
    print (start_paths)
    
    ended=0
    while ended < 4:
        ended=0
        for i,direction in enumerate(start_paths):
            #print(start_direction)
            result = move_next(pipe_map,direction[1],direction[0])
            if result is not False:
                direction[2]+=1
                direction[1]= result[1]
                direction[0]= result[0]
                #print(steps)
            else:
                ended+=1
        print(ended)
    
    
    
    
    
    print(start_paths)
                
    
            
