import math


def heuristic(checkpoints):
    """На полном ходу летим к следующему флагу"""
    return f"{checkpoints[0]} {checkpoints[1]} 200"


def norm_angle(a: float) -> float:
    a = a % 360  # 0..360
    if a > 180:
        a -= 360  # -180..180
    return a


def heuristic2(checkpoint, x, y, angle):
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


def heuristic3(cp, x, y, vx, vy, angle):
    """
    Если текущая скорость такая, что до следующего чекпоинта мы докатимся по инерции,
    то выключаем двигатель.
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
    while True:
        checkpoint_index, x, y, vx, vy, angle = [int(i) for i in input().split()]
        checkpoint = checkpoints[checkpoint_index]
        # X Y THRUST MESSAGE
        # print(heuristic(checkpoint))
        print(heuristic2(checkpoint, x, y, angle))


if __name__ == '__main__':
    main()
