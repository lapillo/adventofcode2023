import math 
       
def get_empty_line_index(map):
    ind=[]
    poz = 0    
    for poz in range(len(map)):
        if map[poz].count(".") == len(map[poz]):
            ind.append(poz)
    return (ind)


if __name__ == '__main__':
    
    file = open("adventofcode2023/zadanie_11/input.txt","r")
    map = file.read().split("\n")
    
    for i,l in enumerate(map):
        map[i] = [x for x in l]
        
    
    #append lines and transform
    row_indexes = get_empty_line_index(map)
    map = [list(row) for row in zip(*map)]
    col_indexes = get_empty_line_index(map)
    map = [list(row) for row in zip(*map)]
    

        
    #replace # to number - build points map
    points=[]
    nr=1
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "#":
                map[y][x] = nr
                points.append((x,y))   
                nr+=1

    space_size=1000000-1
    sum = 0
    for p1 in range(len(points)):
        for p2 in range(p1+1, len(points)):
            x1,y1 = points[p1]
            x2,y2 = points[p2]
            x_spaces = len(set([x for x in range(min(x1,x2), max(x1,x2))]).intersection(col_indexes)) * space_size
            y_spaces = len(set([y for y in range(min(y1,y2), max(y1,y2))]).intersection(row_indexes)) * space_size
            
            dist = abs(x1 - x2) + x_spaces + abs(y1 - y2) + y_spaces
            print("point p1,p2 ", p1+1," ",p2+1, " spaces x,y ", x_spaces, " ", y_spaces, " dist ",dist )
            sum+=dist
    print("result: ", sum)