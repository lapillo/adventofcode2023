def get_mirror_lines(tablica,vertical=False):
    
    if vertical: tablica = rotate_tab(tablica)
    
    ind = [i for i in range(len(tablica)-1) if tablica[i+1].count(tablica[i])>0 ]
    if len(ind) == 0: return (0,0)
    
    res=[]   
    for i in ind:
        off=0
        ind
        for t1,t2 in zip(tablica[0:i+1][::-1],tablica[i+1:]):
            if t1!=t2: break
            off+=1
        if any([off+i==len(tablica)-1, i-off+1 == 0]): res.append((off, i))
    if len(res) == 0: return (0,0)    
    off, ind = max(res)       

    return off, ((ind+1)*100 if not vertical else (ind+1))

def rotate_tab(tablica):
    return [''.join(list(x)) for x in zip(*tablica)]


if __name__ == '__main__': 
 
    file = open("adventofcode2023/zadanie_13/in.txt","r")
    maps = [x.split("\n") for x in file.read().split('\n\n')]
    
    res=[]    
    for map in maps:
        res.append(max(get_mirror_lines(map),get_mirror_lines(map,True)))
    res = sum([v for i,v in res])
    
    print(res)
    

    
    