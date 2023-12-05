
def is_union(range1, range2):
    return range1[0]<=range2[1] and range1[1]>=range2[0]


def divide_ranges (range1, range2):
    union = []
    rest = []
    if range1[0]<range2[0] and range1[1]>range2[1]:
        #3 punkty
        union.extend(range2)
        rest.append([range1[0],range2[0]-1])
        rest.append([range2[1]+1,range1[1]])
    elif range1[0]<range2[0]:
        union.extend([range2[0],range1[1]])
        rest.append([range1[0],range2[0]-1])
    elif range1[1]>range2[1]:
        union.extend([range1[0],range2[1]])
        rest.append([range2[1]+1,range1[1]])
    else:
        union.extend(range1)
    return union, rest

if __name__ == '__main__':
    result = 0
    file = open("adventofcode2023/zadanie_05/input.txt","r")
    list = file.read().split("\n")
    process = []
    process_part = []
    #zadanie 1
    seeds = []
    for line in list:
        if len(line)>0:
            if line.startswith("seeds:"):
                print(line)
                seeds_tmp = line.split()
                seeds_tmp = [int(i) for i in seeds_tmp[1:]]
                for i in range(0, len(seeds_tmp)-1,2):
                    seeds.append([seeds_tmp[i],seeds_tmp[i]+seeds_tmp[i+1]-1 ])
            elif line[0].isalpha():                   
                print(line)
                if len(process_part) > 0: 
                    process.append(process_part)
                process_part = []
                #print(len(process_part))
            elif line[0].isnumeric():
                process_part.append([int(x) for x in line.split()])
                #print (process_part)
                #print(len(process_part))
                process_part[len(process_part)-1][0] -= process_part[len(process_part)-1][1]
                process_part[len(process_part)-1][2] += process_part[len(process_part)-1][1]-1
        #add latest
    process.append(process_part)
    print()  
    print(seeds) 
    print()   
    for proc in process:
        print (proc)
        
    for proc in process:
        print ("process: " , proc)
        seeds_for_next_proc = []
        for step in proc:
            print("\tstep: ", step)
            seeds_for_next_step = []
            for seed in seeds:
                print("\t\tseed: ", seed)
                print("\t\trang: ", step[-2:])
                if (is_union(seed,step[-2:])):
                    union, rest=divide_ranges(seed,step[-2:])
                    print("\t\t\tdivided: ",union, rest)
                    union[0]+=step[0]
                    union[1]+=step[0]
                    print("\t\t\tadded: ",union)
                    seeds_for_next_proc.append(union)
                    seeds_for_next_step.extend(rest)
                    #print("seeds_for_next_proc: ", seeds_for_next_proc)
                else:
                    seeds_for_next_step.append(seed)
                    #print("seeds_for_next_step: ", seeds_for_next_step)
            seeds=seeds_for_next_step
        seeds.extend(seeds_for_next_proc)
        #print("new seeds: ", seeds )
       

    res = min([i for i,j in seeds]) 
    print("result: ", res) 
          
    
    
    
    

         