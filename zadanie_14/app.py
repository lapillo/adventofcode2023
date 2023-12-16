def group_rocks(O_ROCKS,v,s):
    
    
    return


if __name__ == '__main__': 
 
    file = open("adventofcode2023/zadanie_14/ex01.txt","r")
    area = [x for x in file.read().split('\n')]
    S_ROCKS = []
    O_ROCKS = []
    
    S_ROCKS.extend( sum([[(x,y) for x,char in enumerate(row) if char=="#"] for y,row in enumerate(area)],[]) )
    O_ROCKS.extend( sum([[[x,y] for x,char in enumerate(row) if char=="O"] for y,row in enumerate(area)],[]) )
    #print(area)
    
    for o in O_ROCKS:
        #print(o) 
        
        v = (0,1)
        s = (0,1)
        group_rocks(O_ROCKS,v,s)
        
        r_above = [(x,y) for x,y in S_ROCKS+O_ROCKS if x==o[0] and y<o[1]]  
        r_above = max(r_above, key = lambda t: t[1]) if r_above else (o[0],-1)
        
        o[1]=r_above[1]+1
            
        #print("rocks: ", r_above)
       
    print() 
    sum=0
    
    
    for o in O_ROCKS:
        sum+= (len(area) - o[1])
        #print(o)#print(S_ROCKS)
    print(sum)

    
    