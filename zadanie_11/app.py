
def append_line(pipe_map):
    poz = 0    
    while poz < len(map):
        if map[poz].count(".") == len(map[poz]):
            for i in range(1000000-1):
                map.insert(poz,["." for x in range(len(map[0]))])
                poz=poz+1
        poz=poz+1

if __name__ == '__main__':
    
    file = open("adventofcode2023/zadanie_11/input_example.txt","r")
    map = file.read().split("\n")
    
    for i,l in enumerate(map):
        map[i] = [x for x in l]
        
    
    #append lines and transform
    append_line(map)
    map = [list(row) for row in zip(*map)]
    append_line(map)
    map = [list(row) for row in zip(*map)]
    
    points=[]
        
    #replace # to number - build points map
    nr=1
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "#":
                map[y][x] = nr
                points.append((x,y))   
                nr+=1

    
     
    for i,l in enumerate(map):
        print(' '.join(str(e) for e in l))        
        
    print(points)

    sum = 0
    for p1 in range(len(points)):
        for p2 in range(p1+1, len(points)):
            dist = abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])
            print ("points p1,p2", p1, " ", p2, " dist: ", dist)
            sum+=dist
    print("result: ", sum)