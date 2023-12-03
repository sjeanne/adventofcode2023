schematic_file = open('1.txt', 'r')


def is_special_char(char:str):
    return char != '.' and not char.isdigit()

def find_number(line_to_parse:str, index:int):
    num_start = index
    num_end = index
    while num_start-1 >= 0 and line_to_parse[num_start-1].isdigit():
        num_start-=1
    while num_end+1 < len(line_to_parse) and line_to_parse[num_end+1].isdigit():
        num_end+=1
    return int("".join(line_to_parse[num_start:num_end+1]))


schematic_map = []
schematic_sum = 0
while True:
    schema_line = schematic_file.readline().strip()
    if not schema_line:
        break
    schematic_map.append(list(schema_line))

for line_index, line in enumerate(schematic_map):
    for char_index, char_line in enumerate(line):
        if is_special_char(char_line):
            num_found = set()
            for y in [line_index-1,line_index, line_index+1]:
                for x in [char_index-1,char_index,char_index+1]:
                    if y >= 0 and y < len(schematic_map) and x >= 0 and x < len(line):
                        if schematic_map[y][x].isdigit():
                            found_number = find_number(schematic_map[y], x)
                            num_found.add(found_number)
            print(char_line, line_index, char_index, num_found)
            schematic_sum += sum(num_found)
print(schematic_sum)

            