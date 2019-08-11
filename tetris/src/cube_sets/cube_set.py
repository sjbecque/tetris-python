# author: Stephan Becque (https://github.com/sjbecque)
from tetris.src.cube import Cube
import copy

class CubeSet:
    def __init__(self):
        self._cubes = []

    @property
    def cubes(self):
        return self._cubes

    @property
    def count(self):
        return len(self._cubes)

    @cubes.setter
    def cubes(self, value):
        self._cubes = value

    # shorthand method for cube_set creation
    @classmethod
    def c(cls, *cubes_args):
        instance = cls()
        instance._cubes = [
          cls.init_cube(*cube_args) for cube_args in cubes_args
        ]
        return instance

    def get(self, x, y):
        found = [cube for cube in self._cubes if cube.x == x and cube.y == y]
        return found[0] if found else None

    def init_cube(*args):
        return Cube(*args)

    def __eq__(self, other):
        coordinates_self = [cube.coordinates for cube in self._cubes]
        sorted_self = sorted(coordinates_self) #, key=lambda x: x.count, reverse=True)

        coordinates_other = [cube.coordinates for cube in other.cubes]
        sorted_other = sorted(coordinates_other)

        return sorted_self == sorted_other

    def clone(self):
        cube_set = type(self)()
        cube_set.cubes = [copy.copy(cube) for cube in self._cubes]
        return cube_set

    def __repr__(self):
        cubes_str = ",".join([cube.__str__() for cube in self._cubes])
        return f'{type(self).__name__}: [{cubes_str}]'

    @property
    def coordinates(self):
        return [cube.coordinates for cube in self._cubes]