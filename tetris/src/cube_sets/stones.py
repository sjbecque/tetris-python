# author: Stephan Becque (https://github.com/sjbecque)
from tetris.src.cube import Cube
from tetris.src.cube_sets.cube_set import CubeSet

class Stones(CubeSet):
    def __init__(self):
        super(type(self), self).__init__()

    def init_cube(*args):
        return Cube.stone(*args)

    def add(self, cubeset):
        new_cubes = cubeset.cubes
        [cube.stonify() for cube in new_cubes]
        self.cubes += new_cubes

    def process_completed_rows(self, width, height):
        # use assignment expression in while loop from python3.8
        # onwards instead of duplicating method calls
        while self.__lowest_completed_row_y_value(width, height):
            y_value = self.__lowest_completed_row_y_value(width, height)
            self.__delete_row(y_value)

        return self

    def __lowest_completed_row_y_value(self, width, height):
        y_values = [y_value for y_value in list(range(0, height)) if len(self.__row(y_value)) == width]

        if y_values:
          return y_values[-1]
        else:
            None

    def __delete_row(self, y_value):
        self._cubes = [cube for cube in self._cubes if cube.y != y_value]

        cubes_above = [cube for cube in self._cubes if cube.y < y_value]

        for cube in cubes_above:
            cube.y += 1

    def __row(self, y_value):
        return [cube for cube in self.cubes if cube.y == y_value]