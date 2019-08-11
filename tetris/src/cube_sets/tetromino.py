# author: Stephan Becque (https://github.com/sjbecque)
from tetris.src.cube import Cube
from tetris.src.cube_sets.cube_set import CubeSet

class Tetromino(CubeSet):
    def __init__(self):
        self.rotation = 0
        self.rotation_corrections = None
        super(type(self), self).__init__()

    def init_cube(*args):
        return Cube.current(*args)

    def set_rotation_corrections(self, corrections):
        self.rotation_corrections = corrections
        return self

    def rotate(self, direction):
        for cube in self.cubes:
            cube.rotate(self.origin(), direction)

        self.rotation += {
          'clockwise': 1,
          'counter_clockwise': 1,
        }.get(direction)

        if self.rotation_corrections:
            self.move(
                self.rotation_corrections[self.__rotation_index()][direction]
            )

        return self

    def move(self, vector):
        for cube in self.cubes:
            cube.x = cube.x + vector['x']
            cube.y = cube.y + vector['y']
        return self

    def is_bottom_collision(self, height):
        return any(cube for cube in self.cubes if cube.y >= height)

    def is_boundary_collision(self, width):
        return any(cube for cube in self.cubes if not(0 <= cube.x < width))

    def origin(self):
        return next((cube for cube in self.cubes if cube.origin), None)

    def clone(self):
        tetromino = super().clone()
        tetromino.rotation = self.rotation
        tetromino.rotation_corrections = self.rotation_corrections
        return tetromino


    def __rotation_index(self):
        return self.rotation % 4