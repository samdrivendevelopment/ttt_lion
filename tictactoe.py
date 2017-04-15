
def printboard(rowthing):
    row_format = '%s %s %s'
    print ''
    for row in rowthing:
        print row_format % tuple(row)

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

def has_won(row_list, letter):
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
    return False

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


def did_cat(row_list):
    for y, x in cat_list:
        if row_list[x][y] == '_':
            return False
    return True

def should_quit(user_input):
    return user_input in ('q', 'quit')

def is_overlapping(y, x, row_list):
    return row_list[y][x] != '_'

def is_input_invalid(char):
    return not (char in ('0', '1', '2'))

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

        # assigns the new y via input from the player
        print '\nWhat row?'
        y = raw_input('->')

        # checks if the player quits
        if should_quit(y):
            break

        # makes sure all the inputs are vaild
        if is_input_invalid(y):
            print 'That does not seem right'
            continue

        # asigns the new x via input from the player
        print '\nWhat column?'
        x = raw_input('->')

        # checks if the player quits
        if should_quit(x):
            break

        # makes sure all the inputs are vaild
        if is_input_invalid(x):
            print 'That does not seem right'
            continue

        # checks for overlaping
        if is_overlapping(int(y), int(x), row_list):
            print '\nsomebody played there already'
            continue

        # makes sure it goes back to the last turn it should go to
        if letter == 'o':
            letter = 'x'
        elif letter == 'x':
            letter = 'o'

        # assigns the new list
        row_list[int(y)][int(x)] = letter

        # shows the changes in the board
        printboard(row_list)

        # checks if there is a win yet
        if has_won(row_list, letter):
            print '\n' + letter + ' has won!'
            break

        # checks for cats
        if did_cat(row_list):
            print '\nThe game is cat'
            break

if __name__ == '__main__':
    main()


