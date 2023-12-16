import sys


directions = {"N": (0,-1), "E":(1,0),"S":(0,1),"W":(-1,0)}
pipes = {"|":"NS", "-":"EW", "L":"NE", "J":"NW","7":"SW","F":"SE"}
connections = {"N":"S", "E":"W", "S":"N", "W":"E"}
start_symbol="S"
pipes_corners = ("L","J","F","7")

def get_start(pipe_map):
    for y,line in enumerate(pipe_map):
        if start_symbol in line:
            return(line.index(start_symbol),y)


def move_next(pipe_map,current_poz,direction):
    steps=0
    new_poz = (current_poz[0]+directions[direction][0],current_poz[1]+directions[direction][1])
    new_pipe = pipe_map[new_poz[1]][new_poz[0]]
    
    if (new_pipe in pipes):
        if pipes[new_pipe].count(connections[direction])>0:
            steps+=1
            return (pipes[new_pipe].replace(connections[direction],""),new_poz,new_pipe)
    return(False)
    
        
def point_in_polygon(x, y, polygon):
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y) and y <= max(p1y, p2y) and x <= max(p1x, p2x):
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if p1x == p2x or x <= xinters:
                    inside = not inside
        p1x, p1y = p2x, p2y

    return inside    
    
    
#direction, next point, poly points    
start_paths = [["N",[],[]],["E",[],[]],["S",[],[]],["W",[],[]]]


if __name__ == '__main__':
    
    file = open("adventofcode2023/zadanie_10/input.txt","r")
    pipe_map = file.read().split("\n")
    
    for i,l in enumerate(pipe_map):
        pipe_map[i] = [x for x in l]
        
    start_poz = get_start(pipe_map)
    
    #set starting poz for all starting paths
    for x in start_paths:
        x[1]= start_poz
        x[2].append(start_poz)
    
    #navigate pipes, change them to 'x' and build poly with corners
    for i,direction in enumerate(start_paths):
        while True:
            result = move_next(pipe_map,direction[1],direction[0])
            pipe_map[direction[1][1]][direction[1][0]]= "x"
            if result is not False:
                if (result[2] in pipes_corners):
                    start_paths[i][2].append(result[1])
                direction[1]= result[1]
                direction[0]= result[0]
            else:
                break

    #generate results
    result = 0
    for y,l in enumerate(pipe_map):
        for x,char in enumerate(l):
            if char !="x":
                for path in start_paths :
                    if len(path[2])>1 and point_in_polygon(x,y,path[2]):
                        print("in:", (x,y))
                        result+=1                
    print(result)

                
    
            
