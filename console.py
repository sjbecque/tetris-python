# simple console test environment

from tetris.src.engine import Engine
from tetris.src.game import Game
from tetris.src.tetromino_factory import TetrominoFactory
from tetris.src.cube import Cube
from tetris.src.cube_sets.cube_set import CubeSet
from tetris.src.cube_sets.stones import Stones
from tetris.src.cube_sets.tetromino import Tetromino

e = Engine(True, True)
g = Game()
f = TetrominoFactory()
t = f.produce()