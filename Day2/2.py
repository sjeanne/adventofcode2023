games_file = open('1.txt', 'r')

games_powers = []

while True:
    game_line = games_file.readline().strip()
    if not game_line:
        break
    _, draw_str = game_line.split(':')

    # Draw
    draws = draw_str.replace(';', ',').split(', ')
    max_red = 0
    max_green = 0
    max_blue = 0
    for draw in draws:
        nb_cubes_str, color = draw.strip().split(' ')
        nb_cubes = int(nb_cubes_str)
        if color == "blue" and nb_cubes > max_blue:
            max_blue = nb_cubes
            continue
        elif color == "red" and nb_cubes > max_red:
            max_red = nb_cubes
            continue
        elif color == "green" and nb_cubes > max_green:
            max_green = nb_cubes
            continue
    games_powers.append(max_blue * max_green * max_red)

print(f"{games_powers}, {sum(games_powers)}")
