
# Online Python - IDE, Editor, Compiler, Interpreter
import re

arr = [["one",1], ["two", 2], ["three", 3], ["four", 4], ["five", 5], ["six", 6], ["seven", 7], ["eight", 8], ["nine",9]]

def replace_word_to_digit2(input):
    output = input
    for x in arr:
        output = re.sub(x[0], str(x[1]), output)
    return output    

def replace_word_to_digit3(input):
    output = input
    #replace first`
    for x in arr:
        output = re.sub(x[0], str(x[1]), output,1)
    #replace last    
    output=output[::-1]
    for x in arr:
        output = re.sub(x[0][::-1], str(x[1]), output,1)
    output=output[::-1]
    return output  

def replace_word_to_digit1(input):
    output = input
    #find first
    first_winner = 0
    last_winner = 0
    first_poz = -1
    last_poz = -1
    for x in arr:
       first_tmp_poz = output.find(x[0])
       if first_tmp_poz != -1 and (first_tmp_poz < first_poz or first_poz == -1 ):
         first_poz = first_tmp_poz
         first_winner = x
       last_tmp_poz = output.rfind(x[0])
       if last_tmp_poz != -1 and last_tmp_poz > last_poz:
         last_poz = last_tmp_poz
         last_winner = x
    
    
    if first_winner !=0:
         output = output.replace(first_winner[0],str(first_winner[1]),1)
    if last_winner !=0:
         output = output.replace(last_winner[0],str(last_winner[1]),last_poz)
         
    return output

def replace_word_to_digit4(input):
    output = input
    
    #find first
    first_winner = 0
    last_winner = 0
    first_poz = -1
    last_poz = -1
    for x in arr:
       first_tmp_poz = output.find(x[0])
       if first_tmp_poz != -1 and (first_tmp_poz < first_poz or first_poz == -1 ):
         first_poz = first_tmp_poz
         first_winner = x
       last_tmp_poz = output.rfind(x[0])
       if last_tmp_poz != -1 and last_tmp_poz > last_poz:
         last_poz = last_tmp_poz
         last_winner = x
    
    
    if first_winner !=0:
         print(first_winner)
         output = output[:first_poz] + str(first_winner[1]) + output[first_poz+1:]
         print(output)
    if last_winner !=0 and last_winner != first_winner:
         output = output[:last_poz] + str(last_winner[1]) + output[last_poz+1:]
    return output



def replace_word_to_digit5(input):
    output = input
    for x in arr:
        poz = 0
        while poz>=0:
            poz = input.find(x[0],poz)
            if poz != -1:
               output = output[:poz] + str(x[1]) + output[poz+1:]
               poz = poz + 1
    return output







def generate_number(line):

    item = line.strip()
    item2 = replace_word_to_digit5(item)
    #print(item)
    numbers= re.sub(r'\D+', '', item2)
    
    length = len(numbers)
    if length==1:
        numbers = numbers+numbers
    else:
        numbers = numbers[0] + numbers[-1]
    print(item + " = " + item2 + " = " + numbers)
    return numbers

if __name__ == '__main__':
    result = 0
    with open("/config/workspace/adventofcode/zadanie_01/input_01.txt") as file:
        for item in file:
            #print(item) 
            result = result + int(generate_number(item))    
    print (result)