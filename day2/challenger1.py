def valid_game(line):
    games = line.split(':')
    number_game = games[0].split()[1]
    sets_game = games[1].split(';')
    sets_game[len(sets_game) - 1] = sets_game[
        len(sets_game) - 1].replace('\n', '')
    for set_game in sets_game:
        get_cubes = set_game.split(',')
        for cubes_color_and_number in get_cubes:
            number = cubes_color_and_number.split(' ')[1]
            color = cubes_color_and_number.split(' ')[2]
            if color == 'red' and int(number) > 12:
                return 0
            if color == 'green' and int(number) > 13:
                return 0
            if color == 'blue' and int(number) > 14:
                return 0
    return int(number_game)


def sum_id_game():
    sum = 0
    path = "./inputday2.txt"
    with open(path, 'r') as txt:
        for line in txt:
            sum += valid_game(line)
    print(sum)
