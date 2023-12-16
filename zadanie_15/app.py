# - przejdz do pola i wyjmij soczewke z podana etykiete
#   przesum soczewki do przodu bez zmiany ich kolejnosci
# = jezeli jest tam taka etykieta, zmien jej wartosc
#   jezeli nie ma to dodaj
 
if __name__ == '__main__': 
 
    file = open("adventofcode2023/zadanie_15/in.txt","r")
    input = file.read().split(",")
    
    sum=0
    
    for l in input:
        val = 0
        for c in l:
            val+=ord(c)
            val*=17
            val = val % 256
        #print(val)
        sum+=val
        
    print(sum)

            
            
    
    
    