class Game:
    def __init__(self):
        self.board = [[' '] * 3 for _ in range(3)]
        self.move = True  # ход крестика

    def setChar(self, char, row_coord, col_coord):
        row_coord -= 1
        col_coord -= 1
        if 0 <= row_coord < 3 and 0 <= col_coord < 3 and self.board[row_coord][col_coord] == ' ':
            self.board[row_coord][col_coord] = char
            self.move = not self.move
            self.showBoard()
            return True
        return False

    def showBoard(self):
        for i in range(len(self.board)):
            print('|'.join(self.board[i]))
            if i != 2:
                print('-' * 5)
        print()

    def check(self):
        chars = ('O', 'X')
        for i in chars:
            for j in self.board:
                if j.count(i) == 3:
                    self.showWinner(i)
                    return True

            for j in range(3):
                temp = 0
                for k in range(3):
                    if self.board[k][j] == i:
                        temp += 1
                if temp == 3:
                    self.showWinner(i)
                    return True

            if self.board[0][0] == i and self.board[1][1] == i and self.board[2][2] == i:
                self.showWinner(i)
                return True
            elif self.board[0][2] == i and self.board[1][1] == i and self.board[2][0] == i:
                self.showWinner(i)
                return True
        return False

    def showWinner(self, char):
        print("Выиграл", char)
        print()


while True:
    game = Game()
    print('Игра началась! Первый ходит "X". Чтобы сходить, укажите номер строки и столбца, куда вы хотите поставить '
          'фигуру, нумерация начинается с 1. Удачи!')
    game.showBoard()
    while not game.check():
        curr_move = 'X' if game.move else 'O'
        print(f'Сейчас ходит {curr_move}. Куда его поставить?')
        row, col = map(int, input().split())
        while not game.setChar(curr_move, row, col):
            print('Похоже, что вы ввели неверные координаты. Введите еще раз.')
            row, col = map(int, input().split())
    print('Хоите сыграть еще раз? Введите "Да", если хотите, иначе - любой другой текст.')
    again = input()
    if again.strip() != 'Да':
        break
