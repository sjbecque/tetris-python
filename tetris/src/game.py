# author: Stephan Becque (https://github.com/sjbecque)
from tetris.src.tetromino_factory import TetrominoFactory
from tetris.src.cube_sets.stones import Stones

class Game:
    def __init__(self, width = 20, height = 20, tetromino = None, stones = Stones()):
        self.__width = width
        self.__height = height
        self.__stones = stones
        self.__factory = TetrominoFactory()
        self.__tick_count = 0

        if tetromino:
            self.__tetromino = tetromino
        else:
            self.__init_tetromino()

    def next_tick(self):
        self.__tick_count = self.__tick_count + 1
        self.__move_down()

    def move_horizontal(self, direction):
        value = {
          'left': -1,
          'right': 1,
        }[direction]

        new_tetromino = self.__tetromino.clone().move( {'x': value, 'y': 0} )

        if not self.__is_collision(new_tetromino):
            self.__tetromino = new_tetromino

    def rotate(self, direction):
        if not self.tetromino.origin():
            return

        new_tetromino = self.__tetromino.clone().rotate(direction)

        if not self.__is_collision(new_tetromino):
            self.__tetromino = new_tetromino

    def grid(self):
        return [[self.__cube(x,y) for x in list(range(0,self.__width))] for y in list(range(0,self.__height))]

    def __init_tetromino(self):
        self.__tetromino = self.__factory.produce()

    def __move_down(self):
        new_tetromino = self.__tetromino.clone().move({'x': 0, 'y': 1})

        if self.__is_collision(new_tetromino):
            self.__stonify_tetromino()
            self.__stones.process_completed_rows(self.__width, self.__height)
            self.__init_tetromino()
        else:
            self.__tetromino = new_tetromino

    def __is_collision(self, tetromino):
        return (
            tetromino.is_bottom_collision(self.__height) or
            tetromino.is_boundary_collision(self.__width) or
            self.__is_cube_collision(tetromino, self.__stones)
        )

    def __is_cube_collision(self, tetromino, stones):
        # we can't simple use the intersect (&) operator on nested lists
        # or use tuples. We could take the intersect of the item their string values.
        # Or just go:
        return any(value for value in tetromino.coordinates if value in stones.coordinates)

    def __stonify_tetromino(self):
        self.__stones.add(self.__tetromino)

    def __cube(self, x, y):
        return (self.__tetromino.get(x,y) or self.__stones.get(x,y))

    @property
    def tetromino(self):
        return self.__tetromino

    @property
    def stones(self):
        return self.__stones