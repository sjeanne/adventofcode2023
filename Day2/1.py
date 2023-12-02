games_file = open('1.txt', 'r')

valid_games = []

NB_RED = 12
NB_BLUE = 14
NB_GREEN = 13

while True:
    game_line = games_file.readline().strip()
    if not game_line:
        break
    game_id_str, draw_str = game_line.split(':')
    # ID
    _, game_id = game_id_str.split(' ')

    # Draw
    draws = draw_str.replace(';', ',').split(', ')
    too_many_cubes_flag = False
    for draw in draws:
        nb_cubes, color = draw.strip().split(' ')
        if color == "blue":
            if int(nb_cubes) > NB_BLUE:
                too_many_cubes_flag = True
                break
        elif color == "red":
            if int(nb_cubes) > NB_RED:
                too_many_cubes_flag = True
                break
        elif color == "green":
            if int(nb_cubes) > NB_GREEN:
                too_many_cubes_flag = True
                break
    if not too_many_cubes_flag:
        valid_games.append(int(game_id))

print(f"{valid_games}, {sum(valid_games)}")
