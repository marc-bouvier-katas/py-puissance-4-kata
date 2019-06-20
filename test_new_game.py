from grid import *

def test_new_game():
    assert game().ascii() =="""OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO"""

def test_play_red_in_first_column():
    assert game().play('R',1).ascii() == """OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
ROOOOOO"""
