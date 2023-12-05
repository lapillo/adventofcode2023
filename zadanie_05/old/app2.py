import math

if __name__ == '__main__':
    result = 0
    file = open("adventofcode2023/zadanie_05/input.txt","r")
    list = file.read().split("\n")
    
    #zadanie 1
    pat_seeds = list[0].split()
    pat_seeds = [int(i) for i in pat_seeds[1:]]
    mins = []
    
    for i in range(0, len(pat_seeds),2):
        seeds = [x for x in range(pat_seeds[i],pat_seeds[i]+pat_seeds[i+1])]
        for line in list:
            if len(line)>0:
                if line.startswith("seeds:"):
                    continue
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
                            print ("Yessss: ", seed)
                            skip_seed.append(i)
        mins.append(min(seeds))
    #print(seeds)
    print(min(mins))


    
    

         