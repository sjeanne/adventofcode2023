input_file = open('1.txt', 'r')


time = int( "".join(input_file.readline().strip().split()[1:]))
distance = int( "".join(input_file.readline().strip().split()[1:]))

winning_output = 1
winning_times = []
for t in range(time+1):
    if t*(time-t) > distance:
        winning_times.append(t)
print(len(winning_times))