# - przejdz do pola i wyjmij soczewke z podana etykiete
#   przesum soczewki do przodu bez zmiany ich kolejnosci
# = jezeli jest tam taka etykieta, zmien jej wartosc
#   jezeli nie ma to dodaj
 
def calculate_hash(str):
    val = 0
    for c in str:
        val+=ord(c)
        val*=17
        val = val % 256
    return val
 
if __name__ == '__main__': 
 
    file = open("adventofcode2023/zadanie_15/in.txt","r")
    labels = file.read().split(",")
    
    sum=0
    boxes={i:{} for i in range(256)}

    for label in labels:
        ind_op = min(label.find(char) for char in ("-", "=") if char in label)
        key = label[0:ind_op]
        box_id = calculate_hash(key)
        op = label[ind_op:ind_op+1]
        v = label[ind_op+1:len(label)]
        
        if op == "=":
            boxes[box_id].update({key:v})
        if op == "-":
            if key in boxes[box_id]:
                del boxes[box_id][key]
    res=0    
    for i,box in enumerate(boxes):
        for j,lens in enumerate(boxes[box]):
            res+=(box+1) * (j+1) * int(boxes[box][lens])    
    print(res)
    

            
            
    
    
    