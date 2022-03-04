import random
import sys
import math
import time
from collections.abc import Callable


def norm_angle(a):
    a = a % 360  # 0..360
    if a > 180:
        a -= 360  # -180..180
    return a


class Move:
    def __init__(self, x, y, thrust, message = ""):
        self.x, self.y, self.thrust, self.message = x, y, thrust, message

    def __str__(self):
        return f'{self.x} {self.y} {self.thrust} {self.message}'


class State:
    def __init__(self, checkpoints, args):
        """
        args: checkpoint_index, x, y, vx, vy, angle
        """
        self.checkpoints = checkpoints
		self.checkpoint_index = checkpoint_index
		self.x = x
		self.y = y
        self.checkpoint_index, self.x, self.y, self.vx, self.vy, self.angle = args

    def __str__(self):
        return f'{self.checkpoint_index} {self.x} {self.y} {self.vx} {self.vy} {self.angle}'

    def copy(self):
        return State(self.checkpoints, [self.checkpoint_index, self.x, self.y, self.vx, self.vy, self.angle])

    def next_checkpoint(self):
        return self.checkpoints[self.checkpoint_index % len(self.checkpoints)]

    def simulate(self, move: Move):
        desired_angle = 180 * math.atan2(move.y - self.y, move.x - self.x) / math.pi
        da = norm_angle(desired_angle - self.angle)
        da = max(-18, min(18, da))
        self.angle = self.angle + da
        self.vx += move.thrust * math.cos(self.angle * math.pi / 180)
        self.vy += move.thrust * math.sin(self.angle * math.pi / 180)
        self.x = int(self.x + self.vx)
        self.y = int(self.y + self.vy)
        self.vx = int(0.85 * self.vx)
        self.vy = int(0.85 * self.vy)
        self.angle = round(self.angle) % 360
        xc, yc = self.next_checkpoint()
        dx, dy = self.x - xc, self.y - yc
        if dx * dx + dy * dy <= 600 * 600:
            self.checkpoint_index += 1


def estimate(state):
    """
    Возвращает оценку state.
    Чем больше число, тем более желаемый state.
    Чем больше checkpoint_index, тем лучше
    Чем ближе следующий чекпоинт, тем луче
    """
    pass


def create_random_moves(depth):
    """
    Создает и возвращает массив из depth случайных объектов Move.
    """
    pass



def random_search(state, depth):
    """
    Реализация алгоритма Monte-Carlo (другое название — случайный поиск)
    
    Пока есть время — создаёт новую последовательность из depth случайных ходов с помощью функции create_random_moves
    Симулирует эту последовательность ходов.
    Оценивает финальное состояние после эти depth шагов с помощью функции estimate и запоминает лучшую.

    Когда время закончилось, возвращает лучшую последовательность ходов.
    
    На каждый ход даётся 50 миллисекунд. 
    Чтобы засечь время, воспользуйтесь функцией time.time() — она возвращает текущее время в секундах (дробное число).
    """
    pass


def read_checkpoints():
    n = int(input())  # количество чекпоинтов
    checkpoints = []
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        checkpoints.append((x, y))
    return checkpoints


def main():
    checkpoints = read_checkpoints()
    old_state = None
    while True:
        state = State(checkpoints, list(map(int, input().split())))
        print(state, file=sys.stderr)
        if old_state:
            print(old_state, file=sys.stderr)
            # Проверка, что наша симуляция работает точно так же как и официальная.
            # Если раскомментировать строку ниже, то решение начнет падать с ошибкой каждый раз, 
            # когда наша симуляция ошиблась, предсказывая к чему приведет наш предыдущий ход
            # assert str(old_state) == str(state)

        best_moves = random_search(state)
        state.next_move = best_moves[0]
        print(state.next_move)
        
        state.simulate()
        old_state = state


if __name__ == '__main__':
    main()
