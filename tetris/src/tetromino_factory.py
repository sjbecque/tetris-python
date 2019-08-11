# author: Stephan Becque (https://github.com/sjbecque)
from tetris.src.cube import Cube
from tetris.src.cube_sets.tetromino import Tetromino
import random

class TetrominoFactory:
    def produce(self):
        # index = 0 if self.test else random.randint(0, __tetrominos.size)
        index = random.randint(0, len(self.__tetrominos()) - 1)
        return self.__tetrominos()[index]

    def __tetrominos(self):
        return [
            Tetromino.c([10, 0], [10, 1, True], [11, 1], [11, 2]).set_rotation_corrections({
               0 : { 'clockwise': { 'x':-1, 'y':0 } , 'counter_clockwise': { 'x':-1, 'y':1 } },
               1 : { 'clockwise': { 'x':1 , 'y':-1} , 'counter_clockwise': { 'x':0 , 'y':-1} },
               2 : { 'clockwise': { 'x':0 , 'y':1 } , 'counter_clockwise': { 'x':0 , 'y':0 } },
               3 : { 'clockwise': { 'x':0 , 'y':0 } , 'counter_clockwise': { 'x':1 , 'y':0 } }
            }),
            Tetromino.c([10, 0], [11, 0],       [10, 1], [11, 1]),
            Tetromino.c([10, 0], [10, 1, True], [10, 2], [11, 1]),
            Tetromino.c([10, 0], [10, 1, True], [10, 2], [10, 3])
        ]

    def __repr__(self):
        return "TetrominoFactory instance"
