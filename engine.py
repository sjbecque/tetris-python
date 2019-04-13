# author: Stephan Becque (https://github.com/sjbecque)
from threading import Lock, Thread, RLock
from multiprocessing import Process, Lock
import time

class Engine:
    def __init__(self, test, timeout):
        self.__game = Game()
        self.__mutex = Lock()
        self.__test = test
        self.__timeout = timeout

        self.__start_time_loop()
        if not test:
            self.__start_input_loop()

    def __start_time_loop(self):
        self.__time_loop = Thread(target = self.__time_loop_routine)
        self.__time_loop.start()

    def __time_loop_routine(self):
        count = 0

        if self.__test:
            loop_condition = lambda : count < self.__timeout
        else:
            loop_condition = lambda : True

        while loop_condition():
            count += 1
            time.sleep(1)
            with self.__mutex:
                self.__game.next_tick()

    def __start_input_loop(self):
        while True:
            input_var = input("geef input:")
            with self.__mutex:
                self.__game.process_user_input(input_var)


    @property
    def mutex(self):
        return self.__mutex

    @property
    def game(self):
        return self.__game

    @property
    def time_loop(self):
        return self.__time_loop

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
