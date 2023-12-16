import re

def get_LR(data):

    dir=data[1:-1].split(",")
    print (dir)
    return {"L":dir[0].strip(), "R":dir[1].strip()}

if __name__ == '__main__':
    result = 0
    file = open("adventofcode2023/zadanie_08/input.txt","r")
    list = file.read().split("\n")
    
    navigate=list[0]
    
    #create map{path: map{L:x, R:y}}
    data={l.split("=")[0].strip() : get_LR(l.split("=")[1].strip()) for l in list[2:]}

    print(data)
    
    step=0
    
    list_of_starting=
    
    poz="AAA"
    while poz!="ZZZ":
        poz = data[poz][navigate[(step % len(navigate))]]
        step+=1
    print("result: ", step)
    
    



         