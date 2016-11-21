from TicTacToeBoard import TicTacToeBoard


class IConsoleOutput:
    def display(self, ttt_string):
        pass


class IConsoleInput:
    def get_next_input(self):
        pass


class ConsoleOutput(IConsoleOutput):
    def display(self, ttt_string):
        print(ttt_string)


class ConsoleInput(IConsoleInput):
    def get_next_input(self):
        return input()


class TicTacToeGame(object):
    def __init__(self, ui_input, ui_output, game_board):
        self.input = ui_input
        self.output = ui_output
        self.board = game_board

    def display_board(self):
        self.output.display(self.board.to_string())

    def start(self):
        while True:
            self.display_board()
            next_step = self.input.get_next_input()
            if next_step == "":
                return
            self.board.set_step(next_step)


class GameDriver(object):
    def __init__(self, input, output):
        self.game = TicTacToeGame(input, output, TicTacToeBoard())

    def run(self):
        self.game.start()


def main():
    GameDriver(ConsoleInput(), ConsoleOutput()).run()


if __name__ == '__main__':
    main()
