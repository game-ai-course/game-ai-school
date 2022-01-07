import sys
import pytest
import cProfile
from solution import *


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
    assert moves[0] == [(0, 0), (1, 0)]


def test_moves_many_moves():
    s = read_state_from([
        '1 1 2 3',
        '2 2 1 3'])
    moves = list(s.moves())
    assert len(moves) == 3
    assert moves[0] == [(0, 0), (1, 0)]
    assert moves[1] == [(3, 0), (3, 1)]
    assert moves[2] == [(0, 1), (1, 1)]


def test_moves_large_area():
    s = read_state_from([
        '1 1',
        '1 1'])
    moves = list(s.moves())
    assert len(moves) == 1
    assert sorted(moves[0]) == [(0, 0), (0, 1), (1, 0), (1, 1)]


def test_apply_move():
    s = read_state_from([
        '3 3',
        '2 1',
        '1 2',
        '1 2'])
    moves = list(s.moves())
    
    s.apply_move(moves[0])
    expected = """
    0
    -1 3
    -1 1
    3 2
    2 2   
    """
    assert str(s) == expected


def test_apply_move_compaction():
    s = read_state_from([
        '1 1 1 -1',
        '2 3 1 3'])
    moves = list(s.moves())
    s.apply_move(moves[0])
    assert s.cells == [[2, 3, 3, -1], [-1, -1, -1, -1]]


def test_solve():
    state = read_state_from(
        '3 1 1 4 1 0 4 0 4 4 1 1 0 2 3|3 3 2 0 4 4 1 3 1 2 0 0 4 0 4|0 2 3 4 3 0 3 0 0 3 4 4 1 1 1|2 3 4 0 2 3 0 2 4 4 4 3 0 2 3|1 2 1 3 1 2 0 1 2 1 0 3 4 0 1|0 4 4 3 0 3 4 2 2 2 0 2 3 4 0|2 4 3 4 2 3 1 1 1 3 4 1 0 3 1|1 0 0 4 0 3 1 2 1 0 4 1 3 3 1|1 3 3 2 0 4 3 1 3 0 4 1 0 0 3|0 3 3 4 2 3 0 0 2 1 2 3 4 0 1|0 4 1 2 0 1 3 4 3 3 4 1 4 0 4|2 2 3 1 0 4 0 1 2 4 1 3 3 0 1|3 3 0 2 3 2 1 4 3 1 3 0 2 1 3|1 0 3 2 1 4 4 4 4 0 4 2 1 3 4|1 0 1 0 1 1 2 2 1 0 0 1 4 3 2'
        .split('|'))
    print(state)
    moves = solve(state, 19)
    for m in moves:
        # print(m)
        # print(state)
        state.apply_move(m)
    print(state.score)


def test_profile_solve():
    state = read_state_from(
        '3 1 1 4 1 0 4 0 4 4 1 1 0 2 3|3 3 2 0 4 4 1 3 1 2 0 0 4 0 4|0 2 3 4 3 0 3 0 0 3 4 4 1 1 1|2 3 4 0 2 3 0 2 4 4 4 3 0 2 3|1 2 1 3 1 2 0 1 2 1 0 3 4 0 1|0 4 4 3 0 3 4 2 2 2 0 2 3 4 0|2 4 3 4 2 3 1 1 1 3 4 1 0 3 1|1 0 0 4 0 3 1 2 1 0 4 1 3 3 1|1 3 3 2 0 4 3 1 3 0 4 1 0 0 3|0 3 3 4 2 3 0 0 2 1 2 3 4 0 1|0 4 1 2 0 1 3 4 3 3 4 1 4 0 4|2 2 3 1 0 4 0 1 2 4 1 3 3 0 1|3 3 0 2 3 2 1 4 3 1 3 0 2 1 3|1 0 3 2 1 4 4 4 4 0 4 2 1 3 4|1 0 1 0 1 1 2 2 1 0 0 1 4 3 2'
        .split('|'))
    with cProfile.Profile() as pr:
        solve(state, 100)
    pr.print_stats(1)
