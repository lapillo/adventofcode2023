import re

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
            special = find_special_signs_poz("[^0-9\.]",engine_line)
            #special = find_all_in_text("[^0-9\.]", engine_line)
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
    #get all numbers and its position

    for number in line_to_check[1]:
        #print (number[0])
        #print (number[1])
        #check if special sign is near number
        for line in lines_to_check:
            if any(x in line[2] for x in range(number[1][0]-1, number[1][1]+1)):
                print('yes:' + number[0])
                sum += int(number[0])
                break
    return sum
# end def

if __name__ == '__main__':
    result = 0
    parsed_engine_lines = parse_all_lines_from_input("/config/workspace/adventofcode/zadanie_03/input.txt")

    #iterate all parsed lines
    for i in range(len(parsed_engine_lines)):
        result += verify_line(i, parsed_engine_lines)
        
    
    
       
    print(result) 