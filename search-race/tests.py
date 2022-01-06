import sys
import pytest
from heuristics import *
from simulation import *


def test_norm_angle():
    assert norm_angle(360) == 0
    assert norm_angle(370) == 10
    assert norm_angle(350) == -10
    assert norm_angle(-10) == -10
    assert norm_angle(-360) == 0
    assert norm_angle(-370) == -10
    assert norm_angle(10) == 10


def test_heuristic():
    assert heuristic((10, 20)) == "10 20 200  naive"
