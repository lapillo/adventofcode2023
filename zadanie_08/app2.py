import re

def get_LR(data):

    dir=data[1:-1].split(",")
    return {"L":dir[0].strip(), "R":dir[1].strip()}


def get_steps_for_list(list_of_starting,navigate,data):
    step=0
    while True:
        count_z=0
        new_poz=[]
        for i,poz in enumerate(list_of_starting):
            new_poz.append(data[poz][navigate[(step % len(navigate))]])
            if new_poz[-1][2]=="Z":
                count_z+=1
        step+=12
        list_of_starting=new_poz
        if count_z == len(list_of_starting):
            break
    return(step)

def print_nl(list):
    for i in list:
        print(i)

if __name__ == '__main__':
    result = 0
    file = open("adventofcode2023/zadanie_08/input.txt","r")
    list = file.read().split("\n")
    
    navigate=list[0]
    
    #create map{path: map{L:x, R:y}}
    data={l.split("=")[0].strip() : get_LR(l.split("=")[1].strip()) for l in list[2:]}

  
    list_of_starting=[[x] for x in data.keys() if x[2]=="A"]
    #list_of_starting=[x for x in data.keys() if x[2]=="A"]
    #list_of_starting = [list_of_starting[i] for i in (0,1,2,3)]
    
    #print (list_of_starting)
    # result = get_steps_for_list(list_of_starting,navigate,data)
    # print("test 2: ", result)
    
    steps_list=[]
    for i,key in enumerate(list_of_starting):
        steps_list.append([get_steps_for_list(key,navigate,data),i])
    print("counting...")
    
    steps_list.sort()
    i=0
    result = 0
    start= steps_list[-1][0]*steps_list[-2][0]*281
    while True:
        i=i+1 
        good_number=0
        result = i* start     
        for j in steps_list:
            #print(j[0])
            if result%j[0] == 0:
                good_number+=1
        #print(result)
        if good_number>4:
            print(good_number)
        if good_number==len(steps_list):
            break
        
    print(result)  
    
    
    
    
    



         