
if __name__ == '__main__':
    
    file = open("adventofcode2023/zadanie_09/input_example.txt","r")
    list_numbers = file.read().split("\n")
    
    #create map{path: map{L:x, R:y}}
    numbers_list=[[list(reversed([int(n) for n in x.split()]))] for x in list_numbers]    
    
    result = 0
    for numbers in numbers_list:
        ind = 0 
        last_added=0
        while True:
            #print("i ", ind)

            for j in range(1,ind+2): 
                #print("j ", j)
                if len(numbers)<j+1:
                    numbers.append([])
                last_added = numbers[j-1][len(numbers[j])] - numbers[j-1][len(numbers[j])+1]
                numbers[j].append(last_added)
            ind+=1
            if last_added == 0:
                break

        print(numbers)

        #for i in list(range(len(numbers)-1,-1,-1)):
        sum = 0
        for i in list(reversed(range(len(numbers)-1))):
            sum = sum + numbers[i][0]  
        result+=sum
        
    print(result)
            
        #print(list(range(len(numbers),0,-1)))


