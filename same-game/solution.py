import sys
import math

class State:
    def __init__(self, columns: list[list[int]]):
        self.h = len(columns)
        self.w = len(columns[0])
        self.columns = columns

    def __str__(self):
        h = len(self.columns[0])
        w = len(self.columns)
        res = f'{self.score}\n'
        for y in range(h - 1, -1, -1):
            for x in range(w):
                res += '.' if self.columns[x][y] == -1 else str(self.columns[x][y])
            res += '\n'
        return res


    def moves(self):
        """
        Возвращает список ходов, которые можно отправить в apply_move
        
        * Как представлять один ход?
        * Как искать все ходы?
        """
        pass


    def apply_move(self, move):
        """
        Применяет ход: 
        1. Удаляет область клеточек.
        2. Сдвигает нужные клетки над удалённой областью вниз.
        3. Если освободился один или несколько столбцов, сдвигает правую часть влево.

        * Как это реализовать в коде?
        """
        pass


    def copy(self) -> State:
        """
        Создает полную копию состояния игры
        """
        pass


def greedy_ai(state: State, estimate):
    """
    Среди всех доступных ходов выбирает тот, на котором значение функции estimate максимальное.
    Возвращает один ход
    """
    pass


def estimate_move(state, move) -> float:
    pass


def solve(state: State) -> list:
    moves = []
    while True:
        move = greedy_ai(state, estimate_move)
        if move is None:
            return moves
        moves.append(move)
        state.apply_move(move)


def read_state_from(lines: list[str]) -> State:
    rows = []
    for line in lines:
        row = []
        for color in line.split():
            row.append(color)
        rows.append(row)

    # меняем местами строки со столбцами, ориентированными снизу вверх
    cols = [[row[x] for row in reversed(rows)] for x in range(len(rows[0]))]
    return State(cols)


def read_state() -> State:
    lines = [input() for _ in range(15)]
    return read_state_from(lines)


def main():
    moves = None
    move_index = 0
    while True:
        state = read_state()
        if moves is None or move_index >= len(moves):
            moves = list(solve(state, 19 if moves is None else 0.05))
            move_index = 0
        move = moves[move_index]
        move_index += 1
        print(move[0], move[1])


if __name__ == '__main__':
    main()
