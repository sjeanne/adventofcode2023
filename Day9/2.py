input_file = open('1.txt', 'r')

add_umbers = []

while True:
    line = input_file.readline().strip()
    if not line:
        break
    row = list(map(int,line.split()))
    pyramid = [row]
    zero_line = False
    while not zero_line:
        previous_line = pyramid[-1]
        new_line = []
        for index in range(len(previous_line)-1):
            new_line.append(previous_line[index+1]- previous_line[index])
        pyramid.append(new_line)
        zero_line = sum(new_line) == 0
    
    last_inc = pyramid[-2][-1]
    
    for i in range(len(pyramid)-2):
        last_inc = pyramid[len(pyramid)-3-i][0] - last_inc
        
    add_umbers.append(last_inc)
    
print(sum(add_umbers))
