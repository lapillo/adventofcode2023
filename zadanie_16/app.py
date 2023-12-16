# - przejdz do pola i wyjmij soczewke z podana etykiete
#   przesum soczewki do przodu bez zmiany ich kolejnosci
# = jezeli jest tam taka etykieta, zmien jej wartosc
#   jezeli nie ma to dodaj

def beam_outside(x,y):
    return ( any( [x<0, y<0, x>=len(land[0]), y>=len(land)] ))

def move_beam(beam, v):
    x=beam[0] + v[0]
    y=beam[1] + v[1]
    
    if (beam_outside(x,y)):
        return False
    beam[0] = x
    beam[1] = y
    return True

def save_beam(beam, land):
    x=beam[0]
    y=beam[1]
    land[y][x] = "#"
    
def paint_land(land):
    for i in land:
        print(''.join(i))
 
def mirror_beam(beam, v):
    x=beam[0]
    y=beam[1]
    
    vx = v[0]
    vy = v[1]
    
    mirror = land[y][x]
    if (mirror in ["\\"]):
        v[0] = vy
        v[1] = vx
        
    elif (mirror in ["/"]):
        v[0] = vy*-1
        v[1] = vx*-1
    elif (mirror in ["-"] and vx==0):
        if tuple(beam) not in mirrors:
            v[0] = 1
            v[1] = 0
            mirrors.add(tuple(beam))
            navigate_beam([x,y], [-1,0],i)
        else:
            return False
    elif (mirror in ["|"] and vy==0):
        if tuple(beam) not in mirrors:
            v[0] = 0
            v[1] = 1
            mirrors.add(tuple(beam))
            navigate_beam([x,y], [0,-1],i)  
        else:
            return False 
    return True     

i=0

def navigate_beam(beam, v,i):
    while True:
        if not move_beam(beam,v):
            return
        if not mirror_beam(beam,v):
            return
        save_beam(beam, land_copy)
        # if i % 10000000 == 0:
        #     paint_land(land_copy)
        #     print()
        # i+=1  

    
    

if __name__ == '__main__': 
    file = open("adventofcode2023/zadanie_16/in.txt","r")
    land = [list(x) for x in file.read().split("\n")]
    land_copy = [["." for x in range(len(land[0]))] for y in range(len(land))]
    
    #mirrors = mirrors.extend( sum([[(x,y,char) for x,char in enumerate(row) if char=="#"] for y,row in enumerate(area)],[]) )
    mirrors = set()
    beam = [-1,0]
    v = [1,0]

    navigate_beam(beam,v,i)
                
paint_land(land_copy)
       
res=0    
for i in land_copy:
    res+=i.count("#")
print(res)
    