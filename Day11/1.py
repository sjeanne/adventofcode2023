import re

input_file = open('1.txt', 'r')

def print_map(galaxy):
    for x in galaxy:
        print("".join(x))

galaxies_map = []

# Read galaxies map
while True:
    line = input_file.readline().strip()
    if not line:
        break
    galaxies_map.append(list(line))


# Expand the universe
empty_lines = []
for index,row in enumerate(galaxies_map):
    if len([x for x in row if x != '.']) == 0:
        empty_lines.append(index)
for index, empty_index in enumerate(empty_lines):
    galaxies_map.insert(empty_index+index, ["."]*len(galaxies_map[0]))

empty_cols = []
for col in range(len(galaxies_map[0])):
    if len([line[col] for line in galaxies_map if line[col] != "."]) == 0:
        empty_cols.append(col)
for index, empty_col in enumerate(empty_cols):
    for line in galaxies_map:
        line.insert(empty_col+index, ".")

print_map(galaxies_map)

galaxies = []
for index, line in enumerate(galaxies_map):
    pos = [m.start() for m in re.finditer('#', "".join(line))]
    for x in pos:
        galaxies.append((index,x))

distances = []

for i,gal in enumerate( galaxies):
    for dist_gal in galaxies[i+1:]:
        distances.append( abs(gal[0]-dist_gal[0]) + abs(gal[1]-dist_gal[1]))


print(sum(distances))
