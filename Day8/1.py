input_file = open('1.txt', 'r')

maps = {}

directions = list(input_file.readline().strip())
input_file.readline()

while True:
    line = input_file.readline().strip()
    if not line:
        break
    root, nodes = line.split(' = ')
    maps[root] = list(map(str.strip, nodes[1:-1].split(',')))

current_node = "AAA"
step = 0
while True:
    current_node = maps[current_node][0 if directions[step % len(directions)] == 'L' else 1  ]
    step += 1
    if current_node == "ZZZ":
        break
print(step)
