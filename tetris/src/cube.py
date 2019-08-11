# author: Stephan Becque (https://github.com/sjbecque)

class Cube:
    def __init__(self, x, y, origin = False):
        self.__x = x
        self.__y = y
        self.__origin = origin
        self.__value = ''

    @classmethod
    def current(cls, x, y, origin = False, **kwds):
        instance = cls(x, y, origin)
        instance.set_current()
        return instance

    @classmethod
    def stone(cls, x, y):
        instance = cls(x, y)
        instance.stonify()
        return instance

    # only used in spec
    def __add__(self, other):
        return self.__class__(
          self.x + other.x,
          self.y + other.y,
          self.origin
        )

    def __eq__(self, other):
        return (self.coordinates == other.coordinates and self.origin == other.origin)

    def rotate(self, origin, direction):
      directions = {
        'clockwise': 1,
        'counter_clockwise': -1
      }

      relative_x = self.x - origin.x
      relative_y = self.y - origin.y

      self.x = origin.x - relative_y * directions[direction]
      self.y = origin.y + relative_x * directions[direction]

      return self

    def to_s(self):
        if self.is_current:
            return "x"
        else:
            if self.value:
                return "o"
            else:
                return "-"

    def is_current(self):
        return self.value == "current"

    def is_stone(self):
        return self.value == "red"

    def set_current(self):
        self.__value = "current"
        return self

    def stonify(self):
        self.__value = "red"
        return self

    def __repr__(self):
        return f'Cube({self.__x},{self.__y},:{self.__value[0:3]}' + \
          (f',{self.__origin})' if self.__origin else ')')


    # properties & setters

    @property
    def coordinates(self):
        return [self.x, self.y]

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, value):
        self.__rotation = value

    @property
    def value(self):
        return self.__value

    @property
    def origin(self):
        return self.__origin