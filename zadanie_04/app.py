import math

if __name__ == '__main__':
    result = 0
    file = open("/config/workspace/adventofcode/zadanie_04/input.txt","r")
    list = file.read().split("\n")
    
    #zadanie 1
    for line in list:
        numbers=line.split(":")[1]
        list1 = numbers.split("|")[0].split()
        list2 = numbers.split("|")[1].split()
        match = [x in list1 for x in list2]
        if sum(match) == 1:
            result += 1
        elif sum(match) > 1:
            result += math.pow(2,sum(match)-1)
    print(int(result)) 
    

    #zadanie 2
    cards_count = [1]*len(list)
    for i,line in enumerate(list):
        numbers=line.split(":")[1]
        list1 = numbers.split("|")[0].split()
        list2 = numbers.split("|")[1].split()
        n_match = sum([x in list1 for x in list2])
        cards_count[i+1:i+n_match+1] = [ele + cards_count[i] for ele in cards_count[i+1:i+n_match+1]]
        #cards_count[i+1:i+n_match+1] = map(lambda x: x + cards_count[i], cards_count[i+1:i+n_match+1])
    print(sum(cards_count))