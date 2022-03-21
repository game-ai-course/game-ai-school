import pytest
import cProfile
from samegame import *


def test_moves_are_empty():
    s = read_state_from([
        '1 2 1 2',
        '2 1 2 1'])
    moves = list(s.moves())
    assert moves == []


def test_moves_single_move():
    s = read_state_from([
        '1 1 2',
        '2 3 4'])
    moves = list(s.moves())
    assert len(moves) == 1
    assert moves[0] == [(0, 1), (1, 1)]


def test_moves_many_moves():
    s = read_state_from([
        '1 1 1 3',
        '2 2 4 3'])
    moves = [sorted(m) for m in s.moves()]
    assert len(moves) == 3
    assert [(0, 0), (1, 0)] in moves
    assert [(0, 1), (1, 1), (2, 1)] in moves
    assert [(3, 0), (3, 1)] in moves


def test_moves_large_area():
    s = read_state_from([
        '1 1',
        '1 1'])
    moves = [sorted(m) for m in s.moves()]
    assert len(moves) == 1
    assert [(0, 0), (0, 1), (1, 0), (1, 1)] in moves


def test_apply_move():
    s = read_state_from([
        '2 2 1',
        '1 1 3',
        '1 2 3'])
    move = [m for m in s.moves() if (0, 1) in m][0]
    s = s.apply_move(move)
    expected = [
        '. . 1',
        '. 2 3',
        '2 2 3']
    assert str(s).split('\n') == expected


def test_apply_move_compaction():
    s = read_state_from([
        '1 . 3 .',
        '2 1 1 1',
        '3 1 2 1'])
    move = [m for m in s.moves() if (1, 0) in m][0]
    s = s.apply_move(move)
    expected = [
        '1 .',
        '2 3',
        '3 2']
    assert str(s).split('\n') == expected


def test_solve():
    """
    Запускаем функцию solve на отдельном тесте.
    Печатаем на консоль количество очков, которое набирает наш алгоритм на этом тесте
    """
    state = read_state_from(
        '3 1 1 4 1 0 4 0 4 4 1 1 0 2 3\n3 3 2 0 4 4 1 3 1 2 0 0 4 0 4\n0 2 3 4 3 0 3 0 0 3 4 4 1 1 1\n2 3 4 0 2 3 0 2 4 4 4 3 0 2 3\n1 2 1 3 1 2 0 1 2 1 0 3 4 0 1\n0 4 4 3 0 3 4 2 2 2 0 2 3 4 0\n2 4 3 4 2 3 1 1 1 3 4 1 0 3 1\n1 0 0 4 0 3 1 2 1 0 4 1 3 3 1\n1 3 3 2 0 4 3 1 3 0 4 1 0 0 3\n0 3 3 4 2 3 0 0 2 1 2 3 4 0 1\n0 4 1 2 0 1 3 4 3 3 4 1 4 0 4\n2 2 3 1 0 4 0 1 2 4 1 3 3 0 1\n3 3 0 2 3 2 1 4 3 1 3 0 2 1 3\n1 0 3 2 1 4 4 4 4 0 4 2 1 3 4\n1 0 1 0 1 1 2 2 1 0 0 1 4 3 2'
        .splitlines())
    moves = chokudai_solve(state)
    print(moves)
    for m in moves:
        state = state.apply_move(m)
    print(state.score)



def test_profile_solve():
    """
    Этот тест измеряет количество времени, проведенное в каждой из функций вашего решения.
    Изучение отчета позволяет найти самые "горячие" места в коде, которые стоило бы оптимизировать.
    """
    state = read_state_from(
        '3 1 1 4 1 0 4 0 4 4 1 1 0 2 3|3 3 2 0 4 4 1 3 1 2 0 0 4 0 4|0 2 3 4 3 0 3 0 0 3 4 4 1 1 1|2 3 4 0 2 3 0 2 4 4 4 3 0 2 3|1 2 1 3 1 2 0 1 2 1 0 3 4 0 1|0 4 4 3 0 3 4 2 2 2 0 2 3 4 0|2 4 3 4 2 3 1 1 1 3 4 1 0 3 1|1 0 0 4 0 3 1 2 1 0 4 1 3 3 1|1 3 3 2 0 4 3 1 3 0 4 1 0 0 3|0 3 3 4 2 3 0 0 2 1 2 3 4 0 1|0 4 1 2 0 1 3 4 3 3 4 1 4 0 4|2 2 3 1 0 4 0 1 2 4 1 3 3 0 1|3 3 0 2 3 2 1 4 3 1 3 0 2 1 3|1 0 3 2 1 4 4 4 4 0 4 2 1 3 4|1 0 1 0 1 1 2 2 1 0 0 1 4 3 2'
        .split('|'))
    with cProfile.Profile() as pr:
        chokudai_solve(state)
    pr.print_stats(1)
