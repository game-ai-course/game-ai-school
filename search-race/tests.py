import sys
# import pytest
from searchrace_simulation import *


def test_norm_angle():
    assert norm_angle(360) == 0
    assert norm_angle(370) == 10
    assert norm_angle(350) == -10
    assert norm_angle(-10) == -10
    assert norm_angle(-360) == 0
    assert norm_angle(-370) == -10
    assert norm_angle(10) == 10


def test_play_game():
    checkpoints = [(10892, 5399), (4058, 1092), (6112, 2872), (1961, 6027), (7148, 4594), (7994, 1062), (1711, 3942),
                   (10892, 5399), (4058, 1092), (6112, 2872), (1961, 6027), (7148, 4594), (7994, 1062), (1711, 3942),
                   (10892, 5399), (4058, 1092), (6112, 2872), (1961, 6027), (7148, 4594), (7994, 1062), (1711, 3942)]
    state = State(checkpoints, 0, 1711, 3942, 0, 0, 9)
    t = 0
    while state.checkpoint_index < len(checkpoints):
        print(state, file=sys.stderr)
        move = random_search(state)[0]
        state.simulate(move)
        t += 1
        if t > 600:
            break
    print(t)
    assert t < 300
