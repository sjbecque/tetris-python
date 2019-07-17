class Game:
    def __init__(self):
       self.__items = []

    def next_tick(self):
       self.__items.append("value")

    def process_user_input(self, input):
        self.__items.append(input)

    @property
    def items(self):
        return self.__items