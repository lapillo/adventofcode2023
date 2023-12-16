def get_rocks_columns(AR):
    AR_IND={}
    for r in AR:
        x,y,c = r
        if x in AR_IND:
            AR_IND[x].append(r)
        else:
            AR_IND[x] = [r]    
    for i in AR_IND:
        AR_IND[i]=sorted(AR_IND[i],key=lambda x: x[1],reverse=False)
    return AR_IND



def move_rocks(AR_IND):
    for i in AR_IND:
        poz = 0
        for j, (x,y,char) in enumerate(AR_IND[i]):
            if char == "#":
                poz=y+1
            else:
                AR_IND[i][j][1]=poz
                poz+=1 
    return AR_IND
    

def rotate_rocks(AR,size):
    #AR = list(map(lambda r: [ size - r[1] -1 , r[0] , r[2]], AR))
    for r in AR:
        o_x=r[0]
        o_y=r[1]
        r[0] = size - o_y -1
        r[1]=o_x
    return AR
    
if __name__ == '__main__': 
 
    file = open("adventofcode2023/zadanie_14/in.txt","r")
    area = [x for x in file.read().split('\n')]
    AR = []
    size = len(area)
    AR.extend( sum([[[x,y,char] for x,char in enumerate(row) if char in ["O","#"]] for y,row in enumerate(area)],[]) )
    test = AR[2]
    # AR_IND = get_rocks_columns(AR)
    # for i in AR_IND.values():
    #     print (i)
    # print()
    
    # AR=rotate_rocks(AR,size)
    # AR_IND = get_rocks_columns(AR)
    # for i in AR_IND.values():
    #     print (i)
       
    skip_rot = True
    for i in range(1000000000):
        for j in range(4):
            if not skip_rot: AR=rotate_rocks(AR,size)  
            AR_IND = get_rocks_columns(AR)
            AR_IND = move_rocks(AR_IND)
            skip_rot = False
        n = i%10000000
        if n == 0:
            print(i/10000000)
        #print(test)
        # for i in (AR_IND):
        #     print(i, " ", AR_IND[i])
        # print()

    sum=0
    for y in AR_IND.values():
        for j in y:
            if j[2]=="O": sum+= (len(area) - j[1])
    print(sum)
    