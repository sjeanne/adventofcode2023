input_file = open('1.txt', 'r')


times = list(map(int, input_file.readline().strip().split()[1:]))
distances = list(map(int, input_file.readline().strip().split()[1:]))

winning_output = 1
for race, time in enumerate(times):
    print(f'Race: {race} {time} {distances[race]}')
    winning_times = []
    for t in range(time+1):
        if t*(time-t) > distances[race]:
            winning_times.append(t)
    winning_output *= len(winning_times)
print(winning_output)