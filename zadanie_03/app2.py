import re
import math

def find_all_in_text(pattern, txt):
    result = []
    for number in re.finditer(pattern,txt):
        result.append([number.group(0),number.span()])
    print (result)
    return result

def find_special_signs_poz(patetrn,txt):
    result = []
    for number in re.finditer(patetrn,txt):
        result.append(number.start())
    print (result)
    return result

def parse_all_lines_from_input(file):
    with open(file) as file:
        parsed_engine_lines = []
        for engine_line in file:
            engine_line = engine_line.strip()
            print(engine_line)
            number = find_all_in_text("\d+", engine_line)
            special = find_special_signs_poz("[*]",engine_line)
            parsed_engine_lines.append([engine_line,number,special])
            print("")
    return parsed_engine_lines
    
def verify_line(line_number, parsed_engine_lines):
    sum = 0
    line_to_check = parsed_engine_lines[i]
    lines_to_check = []
    if i > 0:
        lines_to_check.append(parsed_engine_lines[i-1])
    lines_to_check.append(parsed_engine_lines[i])
    if i < len(parsed_engine_lines)-1:
        lines_to_check.append(parsed_engine_lines[i+1])
        
    for line in lines_to_check:
        print (line[0])
    print (line_to_check[1])
    print (line_to_check[2])  
    print ("")
    for char_poz in line_to_check[2]:
        #print (char_poz)
        matched_numbers = []
        for line in lines_to_check:
            for number in line[1]:
                #print(number)
                if char_poz in range(number[1][0]-1,number[1][1]+1):
                    print ("Yes!!!!!!!!!!")
                    matched_numbers.append(int(number[0]))
        print ("Matched: " + str(matched_numbers))
        if (len(matched_numbers) == 2):
            sum += math.prod(matched_numbers)
    return sum

if __name__ == '__main__':
    result = 0
    parsed_engine_lines = parse_all_lines_from_input("adventofcode2023/zadanie_03/input.txt") 
    for i in range(len(parsed_engine_lines)):
        result += verify_line(i, parsed_engine_lines)
    print(result) 