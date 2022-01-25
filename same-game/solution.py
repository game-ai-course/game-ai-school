import sys


class State:
    def __init__(self, columns: list[list[int]], score: int = 0):
        self.columns = columns
        self.score = score


    def __str__(self):
        w = len(self.columns)
        if w == 0:
            return '.'
        h = max(len(col) for col in self.columns)
        rows = []
        for y in range(h - 1, -1, -1):
            row = []
            for x in range(w):
                row.append('.' if y >= len(self.columns[x]) else str(self.columns[x][y]))
            rows.append(' '.join(row))
        return '\n'.join(rows)


    def moves(self):
        """
        Возвращает список ходов, которые можно отправить в apply_move

        * Как представлять один ход?
        * Как искать все ходы?
        """
        pass


    def apply_move(self, move) -> 'State':
        """
        Применяет ход и возвращает новое состояние (не меняя текущее!)

        * Как это реализовать в коде?
        """
        pass


def greedy_ai(state: State, estimate):
    """
    Среди всех доступных ходов выбирает тот, на котором значение функции estimate максимальное.
    Возвращает один ход
    """
    pass


def estimate_move(state: State, move) -> float:
    """
    Чем больше возвращаемое число, тем более хороший это ход.
    """
    pass


def solve(state: State, seconds: float):
    """
    Возвращает сколько-то первых ходов для решения уровня.
    Может вернуть только 1 первый ход. В первой практике так и нужно делать.
    
    Но на codingame.com на первый ход дают 20 секунд, а на последующие всего по 50ms.
    Поэтому выгодно решить полностью весь уровень на первом ходу и вернуть список всех ходов.
    Во время второй практики, после реализации apply_move переделайте этот метод так, чтобы он возвращал всю последовательность ходов до завершения уровня.
    """
    move = greedy_ai(state, estimate_move)
    return [move]


def read_state_from(lines: list[str]) -> State:
    rows = []
    for line in lines:
        row = []
        for color in line.split():
            row.append(-1 if color == '.' else int(color))
        rows.append(row)

    # Переводим в наш формат: список столбцов, клетки в которых перечислены снизу вверх, без пустых клеток
    cols = [[row[x] for row in reversed(rows) if row[x] != -1] for x in range(len(rows[0]))]
    return State(cols)


def read_state() -> State:
    lines = [input() for _ in range(15)]
    return read_state_from(lines)


def main():
    moves = []
    move_index = 0
    first_move = True
    while True:
        state = read_state()
        if first_move:
            print(state, file=sys.stderr)
        if move_index >= len(moves):
            timeout = 19 if first_move else 0.05
            moves = solve(state, timeout)
            move_index = 0
        x, y = moves[move_index][0]
        move_index += 1
        print(x, y)
        first_move = False


if __name__ == '__main__':
    main()
