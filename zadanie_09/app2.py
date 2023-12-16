
if __name__ == '__main__':
    
    file = open("adventofcode2023/zadanie_09/input.txt","r")
    list_numbers = file.read().split("\n")
    

    numbers_list=[[[int(n) for n in x.split()]] for x in list_numbers]    
    
    result = 0
    for numbers in numbers_list:
        ind = 0 
        last_added=0
        while True:
            for j in range(1,ind+2): 
                if len(numbers)<j+1:
                    numbers.append([])
                last_added = numbers[j-1][len(numbers[j])+1] - numbers[j-1][len(numbers[j])]
                numbers[j].append(last_added)
            ind+=1
            if len(numbers) == len(numbers[0]):
                break
        sum = 0
        for i in list(reversed(range(0,len(numbers)-2))):
            sum = numbers[i][0] - sum 
        result+=sum
    print(result)


