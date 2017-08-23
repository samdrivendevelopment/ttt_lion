
def printboard(rowthing):
    row_format = '%s %s %s'
    print ''
    for row in rowthing:
        print row_format % tuple(row)

def check_quit(user_input):
    if user_input == 'q':
        return True
    if user_input == 'quit':
        return True

def check_overlap(y, x, row_list):
    if row_list[y][x] != '_':
        return True

win_condition_list = [
    [(0, 0), (0, 1), (0, 2)], # top row
    [(1, 0), (1, 1), (1, 2)], # middle row
    [(2, 0), (2, 1), (2, 2)], # bottom row
    [(0, 0), (1, 0), (2, 0)], # left column
    [(0, 1), (1, 1), (2, 1)], # center column
    [(0, 2), (1, 2), (2, 2)], # right column
    [(0, 0), (1, 1), (2, 2)], # negative diagonal
    [(0, 2), (1, 1), (2, 0)], # positive diagonal
]

def check_win(row_list, letter):
    for win_condition in win_condition_list:
# had to index everything out of nested lists
        first_y, first_x = win_condition[0]
        second_y, second_x = win_condition[1]
        third_y, third_x = win_condition[2]
# then check every spot to see if it is a win
        if row_list[first_y][first_x] == letter:
            if row_list[second_y][second_x] == letter:
                if row_list[third_y][third_x] == letter:
                    return True
cat_list = [
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 0),
    (2, 1),
    (2, 2),
]


def check_cat(row_list):
    for y, x in cat_list:
        if row_list[x][y] == '_':
            return False
    return True

def main():

    row_list = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_'],
    ]

    printboard(row_list)
# start with O so it turns into X
    letter = 'o'

    for item in range(99):
        print '\nWhat row?'
        y = raw_input('->')
        should_quit = check_quit(y)
        if should_quit:
            break
        print '\nWhat column?'
        x = raw_input('->')
        should_quit = check_quit(x)
        if should_quit:
            break

        is_overlapping = check_overlap(int(y), int(x), row_list)
        if is_overlapping:
            print '\nsomebody played there already'
            continue

        if letter == 'o':
            letter = 'x'
        elif letter == 'x':
            letter = 'o'

        row_list[int(y)][int(x)] = letter

        printboard(row_list)

        has_won = check_win(row_list, letter)
        if has_won:
            print '\n' + letter + ' has won!'
            break

        did_cat = check_cat(row_list)
        if did_cat:
            print '\nThe game is cat'
            break

main()


