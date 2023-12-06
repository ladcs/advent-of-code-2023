def valid_game(line):
    red = []
    green = []
    blue = []
    games = line.split(':')
    sets_game = games[1].split(';')
    sets_game[len(sets_game) - 1] = sets_game[
        len(sets_game) - 1].replace('\n', '')
    for set_game in sets_game:
        get_cubes = set_game.split(',')
        for cubes_color_and_number in get_cubes:
            number = cubes_color_and_number.split(' ')[1]
            color = cubes_color_and_number.split(' ')[2]
            if color == 'red':
                red.append(int(number))
            if color == 'green':
                green.append(int(number))
            if color == 'blue':
                blue.append(int(number))
    red_sorted = sorted(red)
    green_sorted = sorted(green)
    blue_sorted = sorted(blue)
    return red_sorted[len(red) - 1] * green_sorted[
        len(green) - 1] * blue_sorted[len(blue) - 1]


def sum_multiply_power_of_set():
    sum = 0
    path = "./inputday2.txt"
    with open(path, 'r') as txt:
        for line in txt:
            sum += valid_game(line)
    print(sum)
