

if __name__ == '__main__': 
 
    file = open("adventofcode2023/zadanie_14/ex01.txt","r")
    area = [x for x in file.read().split('\n')]
    S_ROCKS = []
    O_ROCKS = []
    
    S_ROCKS.extend( sum([[(x,y) for x,char in enumerate(row) if char=="#"] for y,row in enumerate(area)],[]) )
    O_ROCKS.extend( sum([[[x,y] for x,char in enumerate(row) if char=="O"] for y,row in enumerate(area)],[]) )
    #print(area)
    
    for i in range(1000000000):
        for dir in ("N", "W", "S", "E"):
            
            
            
            
            for o in O_ROCKS:
                #print(o) 
                rock_x=o[0]
                rock_y=o[1]
                
                if dir=="N":
                    r_on_way = [(x,y) for x,y in S_ROCKS+O_ROCKS if x==rock_x and y<rock_y]  
                    r_on_way = max(r_on_way, key = lambda t: t[1]) if r_on_way else (rock_x,-1)
                    o[1]=r_on_way[1]+1
                    
                if dir=="W":
                    r_on_way = [(x,y) for x,y in S_ROCKS+O_ROCKS if y==rock_y and x<rock_x]  
                    r_on_way = max(r_on_way, key = lambda t: t[0]) if r_on_way else (-1,rock_y)
                    o[0]=r_on_way[0]+1
                
                if dir=="S":
                    r_on_way = [(x,y) for x,y in S_ROCKS+O_ROCKS if x==rock_x and y>rock_y]  
                    r_on_way = min(r_on_way, key = lambda t: t[1]) if r_on_way else (rock_x,len(area))
                    o[1]=r_on_way[1]-1
                    
                if dir=="E":
                    r_on_way = [(x,y) for x,y in S_ROCKS+O_ROCKS if y==rock_y and x>rock_x]  
                    r_on_way = min(r_on_way, key = lambda t: t[0]) if r_on_way else (len(area[0]),rock_y)
                    o[0]=r_on_way[0]-1
                    
       
        #print() 
    
        sum=0
        for o in O_ROCKS:
            sum+= (len(area) - o[1])
            #print(o)#print(S_ROCKS)
    print(sum)

    
    