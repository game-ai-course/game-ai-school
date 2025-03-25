import math


def heuristic(checkpoint: tuple[int, int]) -> str:
    """На полном ходу летим к следующему флагу"""
    return f"{checkpoint[0]} {checkpoint[1]} 200"


def norm_angle(a: float) -> float:
    a = a % 360  # 0..360
    if a > 180:
        a -= 360  # -180..180
    return a


def heuristic2(checkpoint: tuple[int, int], x: int, y: int, angle: int) -> str:
    """
    Включаем полный ход, если смотрим почти на следующий флаг.
    Поворачиваемся в сторону следующего флага.
    """
    cx, cy = checkpoint
    dx = cx - x
    dy = cy - y
    cp_angle = math.atan2(dy, dx) * 180 / math.pi
    da = norm_angle(cp_angle - angle)
    if abs(da) > 15:
        return f"{cx} {cy} 0 turn"
    return f"{cx} {cy} 200 thrust"


def heuristic3(checkpoint: tuple[int, int], x: int, y: int, vx: int, vy: int, angle: int) -> str:
    """
    Если текущая скорость такая, что до следующего чекпоинта мы докатимся по инерции,
    то выключаем двигатель.
    """
    pass


def read_checkpoints() -> list[tuple[int, int]]:
    n = int(input())  # количество чекпоинтов
    checkpoints = []
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        checkpoints.append((x, y))
    return checkpoints


def main():
    checkpoints = read_checkpoints()
    while True:
        checkpoint_index, x, y, vx, vy, angle = [int(i) for i in input().split()]
        checkpoint = checkpoints[checkpoint_index]
        # X Y THRUST MESSAGE
        print(heuristic(checkpoint))
        # print(heuristic2(checkpoint, x, y, angle))
        # next_checkpoint = checkpoints[(checkpoint_index + 1) % len(checkpoints)]


if __name__ == '__main__':
    main()
