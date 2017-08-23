#!/usr/bin/python

import json
import sys

def printboard(rowthing, ui):
    row_format = '%s %s %s'
    ui.write('')
    for row in rowthing:
        ui.write(row_format % tuple(row))

def vertical_win(board, letter):
    for i in range(2):
        if board[0][i] == letter:
            if board[1][i] == letter:
                if board[2][i] == letter:
                    return True
    return False

def horizontal_win(board, letter):
    for i in range(2):
        if board[i] == [letter] * 3:
            return True
    return False

def diagonal_win(board, letter):
    # negative diagonal
    if board[0][0] == letter:
        if board[1][1] == letter:
            if board[2][2] == letter:
                return True
    # positive diagonal
    if board[0][2] == letter:
        if board[1][1] == letter:
            if board[2][0] == letter:
                return True
    return False
 
def has_won(board, letter):
    if vertical_win(board, letter):
        return True
    if horizontal_win(board, letter):
        return True
    if diagonal_win(board, letter):
        return True
    return False


def end_game(board, letter, ui):
    if has_won(board, letter):
        ui.write('\n' + letter + ' has won!')
        return True

    if did_cat(board):
        ui.write('\nThe game is cat')
        return True
    return False

def turn_change(letter):
    return {'o': 'x', 'x': 'o'}.get(letter)

def did_cat(board):
    for i in range(2):
        if '_' in board[i]:
            return False
    return True

def should_quit(user_input):
    if user_input in ('q', 'quit'):
        return True
    return False

def is_overlapping(y, x, board):
    if board[int(y)][int(x)] != '_':
        return True
    return False

def is_input_invalid(char):
    if char not in ('0', '1', '2'):
        return True
    return False

class ShellUI(object):
    def read(self):
        return raw_input('->')

    def write(self, text):
        print text

class TicTacToeGame(object):
    def turn(self):
        printboard(self.state['board'], self.ui)

        self.ui.write('What row?')
        first_raw = self.ui.read()
        if should_quit(first_raw):
            return True

        if is_input_invalid(first_raw):
            self.ui.write('That does not seem valid.')
            return False

        self.ui.write('What column?')
        second_raw = self.ui.read()
        if should_quit(second_raw):
            return True

        if is_input_invalid(second_raw):
            self.ui.write('That does not seem vaild')
            return False

        if is_overlapping(first_raw, second_raw, self.state['board']):
            self.ui.write('Someone is already there.')
            return False

        self.state['board'][int(first_raw)][int(second_raw)] = self.state['letter']

        if end_game(self.state['board'], self.state['letter'], self.ui):
            self.ui.write('Game has ended.')
            return True

        self.state['letter'] = turn_change(self.state['letter'])

        return False


def main():
    # initialize state by calling function
    filename = sys.argv[1]
    f = open(filename)
    state = json.load(f)
    f.close()
    game = TicTacToeGame()
    game.state = state
    game.ui = ShellUI()

    for i in range(999):
        should_break = game.turn()
        if should_break:
            break


if __name__ == '__main__':
    main()

