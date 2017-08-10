
from tictactoe import TicTacToeGame

class BetterTestUI(object):
    def read(self):
        fake_user_input = self.input_list[self.index]
        self.index += 1
        return fake_user_input

    def write(self, text):
        pass

def make_better_test_game(input_list):
    state = {
        'letter': 'x',
        'board': [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ],
    }
    game = TicTacToeGame()
    game.state = state
    game.ui = BetterTestUI()
    game.ui.index = 0
    game.ui.input_list = input_list
    return game

def test_is_invalid_st_input():
    game = make_better_test_game(['t'])
    result = game.turn()
    return result == False

def test_is_invalid_nd_input():
    game = make_better_test_game(['1', 't'])
    result = game.turn()
    return result == False

def test_is_st_quit():
    game = make_better_test_game(['q'])
    result = game.turn()
    return result == True

def test_is_nd_quit():
    game = make_better_test_game(['1', 'q'])
    result = game.turn()
    return result == True

def test_is_overlapping():
    game = make_better_test_game(['1', '1'])
    game.state['board'][1][1] = 'o'
    result = game.turn()
    boards_are_same = game.state['board'] == [
        ['_', '_', '_'],
        ['_', 'o', '_'],
        ['_', '_', '_'],
    ]

    return (result == False) and (game.state['letter'] == 'x') and boards_are_same

def test_is_not_overlapping():
    game = make_better_test_game(['1', '1'])
    result = game.turn()
    boards_are_same = game.state['board'] == [
        ['_', '_', '_'],
        ['_', 'x', '_'],
        ['_', '_', '_'],
    ]

    return (result == False) and (game.state['letter'] == 'o') and boards_are_same


def test_has_won():
    game = make_better_test_game(['1', '1'])
    game.state['board'][0][2] = 'x'
    game.state['board'][2][0] = 'x'
    result = game.turn()
    return result == True

def test_has_not_won():
    game = make_better_test_game(['1', '1'])
    result = game.turn()
    return result == False

def test_has_cat():
    game = make_better_test_game(['1', '1'])
    game.state['board'] = [
        ['o', 'o', 'x'],
        ['x', '_', 'o'],
        ['o', 'o', 'x'],
    ]
    result = game.turn()
    return result == True

def test_has_not_cat():
    game = make_better_test_game(['1', '1'])
    result = game.turn()
    return result == False

def main():

    if not test_is_invalid_st_input():
        print 'Turn did not catch the first invaild charater.'

    if not test_is_invalid_nd_input():
        print 'Turn did not catch the second invaild charater.'

    if not test_is_st_quit():
        print 'turn did not catch the first quit.'

    if not test_is_nd_quit():
        print 'turn did not catch the second quit.'

    if not test_is_overlapping():
        print 'turn did not catch the overlap.'

    if not test_is_not_overlapping():
        print 'turn detected a overlap when there was none.'

    if not test_has_won():
        print 'turn did not catch the win.'

    if not test_has_not_won():
        print 'turn detected a win when there was none.'

    if not test_has_cat():
        print 'turn did not catche the cats.'

    if not test_has_not_cat():
        print 'turn detected a cats when there was none.'

if __name__ == '__main__':
    main()

