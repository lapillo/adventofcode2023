import math

def combination(n, k):
    result = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return result

def find_dammeged(spr, dammaged):
    
    print ("spr: ", spr, " dam: ", dammaged) 
    separates = spr.split(".")
        #print(spr," ", dam)
    
    dam_buckets = 0
    for sep in separates:
        if sep.count("#") > 0:
            dam_buckets+=1
    
    possible_sets = []
    for sep in separates:
        if len(sep)>0:
            #all ? fit max dam sprinmgs
            x1=0
            x2=0
            added = 0
            capacity = len(sep)
            normalization = 0
            if (sep.count("#") == 0):
                normalization = 0    
                for i, dam in enumerate(dammaged):
                    if i > 0:
                        separator = 1
                    else: 
                        separator=0 
                    if x2 + dam + separator <= capacity:
                        x2+=dam + separator
                        added += 1
                        normalization += dam - 1 + separator
                        if (dam_buckets == len(dammaged)-added):
                            break               
                if (added > 0):
                    #print ("sep: ", sep, " dam: ", dammaged) 
                    #print("w: ", sep, " zmiescilem: ", added)
                    dammaged = dammaged[added:]
                    #print ("dam -: ", dammaged) 
                    
        
            #all #
            elif (sep.count("?") == 0):
                if capacity == dammaged[0]:
                    added+=1
                    #print ("sep: ", sep, " dam: ", dammaged) 
                    #print("w: ", sep, " zmiescilem: ", added)
                    normalization += dammaged[0] - 1
                    dammaged = dammaged[1:]
                    
            elif (sep.count("?") > 0 and sep.count("#") > 0):
                
                x1 = 0
                #x2 = len(sep)
#                for i, dam in enumerate(dammaged):
                dam = dammaged[0]
                if dam == capacity:
                    added+=1
                    normalization += dammaged[0] - 1
                    dammaged = dammaged[1:]
                    break
                else:
                    while sep[x1 + dam] != "?":
                        x1+=1
                        if (x1 + dam) == capacity:
                            break
                    if (x1+dam+1) > capacity:
                        #MOZE DODAC WARIACJE?
                        #possible_sets+=1
                        print("end")
                    else:
                        possible_sets.append(find_dammeged(sep[x1+dam+1:],dammaged[1:]))
                    print("nie wiem co zrobic z: ", sep, " res: ")
                    dammaged = dammaged[1:]
                                   

            if (added > 0):
                
                possible_sets.append(combination(capacity - normalization, added))
                #print("kombinacje: ", possible_sets) 
    result = 1
    for i in possible_sets:
        result *=i
    print("kombinacje: ", result)    
    return result 




if __name__ == '__main__':
    
    file = open("adventofcode2023/zadanie_12/input_example.txt","r")
    map = file.read().split("\n")
    
    springs = []
    dammaged = []
    
    for l in map:
        springs.append(l.split()[0])
        dammaged.append([int(x) for x in l.split()[1].split(",")])
        
    
    for i in range(len(springs)):
        print(springs[i], " ", dammaged[i])
        
    print()
    
    res = 0
    for i,spr in enumerate(springs):
        res+= find_dammeged(spr, dammaged[i])
           
    print (res)
    # ?##?        
    