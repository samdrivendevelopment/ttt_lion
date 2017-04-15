
from tictactoe import did_cat, has_won, should_quit, is_overlapping,\
    is_input_invalid


def test_game_is_not_cat():
    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_'],
    ]
    result = did_cat(board)
    return result == False

def test_game_is_cat():
    board = [
        ['x', 'o', 'x'],
        ['x', 'o', 'o'],
        ['o', 'x', 'x'],
    ]
    result = did_cat(board)
    return result == True

def test_if_not_win():
    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_'],
    ]
    result = has_won(board, 'o')
    return result == False

def test_if_x_vertical_win():
    board = [
        ['x', '_', '_'],
        ['x', '_', '_'],
        ['x', '_', '_'],
    ]
    result = has_won(board, 'x')
    return result == True

def test_if_x_horizontal_win():
    board = [
        ['x', 'x', 'x'],
        ['_', '_', '_'],
        ['_', '_', '_'],
    ]
    result = has_won(board, 'x')
    return result == True

def test_if_x_diagonal_win():
    board = [
        ['x', '_', '_'],
        ['_', 'x', '_'],
        ['_', '_', 'x'],
    ]
    result = has_won(board, 'x')
    return result == True

def test_should_quit():
    result = should_quit('q')
    return result == True

def test_should_not_quit():
    result = should_quit('1')
    return result == False


def test_does_overlap():
    board = [
       ['_', '_', '_'],
       ['_', 'x', '_'],
       ['_', '_', '_'],
    ]
    result = is_overlapping(1, 1, board)
    return result == True

def test_does_not_overlap():
    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_'],
    ]
    result = is_overlapping(1, 1, board)
    return result == False

def test_vaild_input():
    result = is_input_invalid('1')
    return result == False

def main():
    print 'start test suite'

    if not test_game_is_cat():
        print 'did_cat failed to detect cat'

    if not test_game_is_not_cat():
        print 'did_cat detected cat incorrectly'

    if not test_if_not_win():
        print 'has_won failed to detect win'

    if not test_if_x_vertical_win():
        print 'has_won detected vertical x win incorrectly'

    if not test_if_x_horizontal_win():
        print 'has_won detected horizontal x win incorrectly'

    if not test_if_x_diagonal_win():
        print 'has_won detected diagonal x win incorrectly'

    if not test_should_quit():
        print 'should_quit failed to detect quit'

    if not test_should_not_quit():
        print 'should_quit detected quit incorrectly'

    if not test_does_overlap():
        print 'is_overlapping failed to detect overlap'

    if not test_does_not_overlap():
        print 'is_overlapping detected overlap incorrectly'

    if not test_vaild_input():
        print 'check_input detected input incorectly'

    print 'stop test suite'

if __name__ == '__main__':
    main()

