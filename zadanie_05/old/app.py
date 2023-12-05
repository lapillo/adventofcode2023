if __name__ == '__main__':
    result = 0
    file = open("adventofcode2023/zadanie_05/input.txt","r")
    list = file.read().split("\n")
    
    #zadanie 1
    seeds = list[0].split()
    seeds = [int(i) for i in seeds[1:]]
    print ([1 in range (1,10)])
    
    for line in list:
        if len(line)>0:
            if line.startswith("seeds:"):
                #zadanie 1
                seeds = line.split()
                seeds = [int(i) for i in seeds[1:]]
                #########

                
                #######
            elif line[0].isalpha():                   
                print ("Parsing" + line)
                skip_seed=[]
            elif line[0].isnumeric():
                #print(line)
                map = [int(i) for i in line.split()]
                for i,seed in enumerate(seeds):
                    if seed in range(map[1], map[1]+map[2]) and i not in skip_seed:
                        seed  = seed + map[0]-map[1]
                        seeds[i] = seed
                        #print ("Yessss: ", seed)
                        skip_seed.append(i)
    #print(seeds)
    print(min(seeds))
    
    

    
    

         