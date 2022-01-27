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
    def __init__(self, x, y, thrust, message):
        self.x, self.y, self.thrust, self.message = x, y, thrust, message

    def __str__(self):
        return f'{self.x} {self.y} {self.thrust} {self.message}'


class State:
    def __init__(self, ckeckpoints, args):
        """
        args: checkpoint_index, x, y, vx, vy, angle
        """
        self.checkpoints = ckeckpoints
        self.checkpoint_index, self.x, self.y, self.vx, self.vy, self.angle = args
        self.next_move = Move(0, 0, 0, "init")

    def __str__(self):
        return f'{self.checkpoint_index} {self.x} {self.y} {self.vx} {self.vy} {self.angle}'

    def copy(self):
        return State(self.checkpoints, [self.checkpoint_index, self.x, self.y, self.vx, self.vy, self.angle])

    def next_checkpoint(self):
        return self.checkpoints[self.checkpoint_index]

    def simulate(self):
        desired_angle = 180 * math.atan2(self.next_move.y - self.y, self.next_move.x - self.x) / math.pi
        da = norm_angle(desired_angle - self.angle)
        da = max(-18, min(18, da))
        self.angle = self.angle + da
        self.vx += self.next_move.thrust * math.cos(self.angle * math.pi / 180)
        self.vy += self.next_move.thrust * math.sin(self.angle * math.pi / 180)
        self.x = int(self.x + self.vx)
        self.y = int(self.y + self.vy)
        self.vx = int(0.85 * self.vx)
        self.vy = int(0.85 * self.vy)
        self.angle = round(self.angle) % 360
        xc, yc = self.next_checkpoint()
        dx, dy = self.x - xc, self.y - yc
        if dx * dx + dy * dy <= 600 * 600:
            self.checkpoint_index += 1


def heuristic(state):
    """
    Включаем полный ход, если смотрим почти на следующий флаг.
    Поворачиваемся в сторону следующего флага.
    """
    cp = state.next_checkpoint()
    dx = cp[0] - state.x
    dy = cp[1] - state.y
    cp_angle = math.atan2(dy, dx) * 180 / math.pi
    da = norm_angle(cp_angle - state.angle)
    thrust = 200 if abs(da) < 15 else 0
    return Move(cp[0], cp[1], thrust, "heuristic")


def read_checkpoints():
    n = int(input())  # количество чекпоинтов
    checkpoints = []
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        checkpoints.append((x, y))
    return checkpoints


def estimate(state):
    """
    Возвращает оценку state.
    Чем больше число, тем более желаемый state.
    Чем больше checkpoint_index, тем лучше
    Чем ближе следующий чекпоинт, тем луче
    """
    pass


def random_search(state, depth):
    """
    Пока есть время — генерирует новую последовательность из depth случайных ходов.
    Симулирует эту последовательность.
    Оценивает финальное состояние после эти depth шагов и запоминает лучшую.

    Когда время закончилось, возвращает первый ход из лучшей последовательности.
    """
    pass


def main():
    checkpoints = read_checkpoints()
    old_state = None
    while True:
        state = State(checkpoints, list(map(int, input().split())))
        print(state, file=sys.stderr)
        if old_state:
            print(old_state, file=sys.stderr)
            # check simulation is correct
            # assert str(old_state) == str(state)

        # Поменяйте вызов heuristic на random_search
        state.next_move = heuristic(state)
        # state.next_move = random_search(state)
        print(state.next_move)
        state.simulate()
        old_state = state


if __name__ == '__main__':
    main()
