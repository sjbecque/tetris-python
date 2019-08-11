# author: Stephan Becque (https://github.com/sjbecque)
from threading import Lock, Thread, RLock
from multiprocessing import Process, Lock
from tetris.src.game import Game
import time, os, sys
import easy_getch #for non-blocking character input

class Engine:
    def __init__(self, test, console):
        self.__test = test
        self.__console = console
        self.__game = Game()
        self.__mutex = Lock()
        self.__stop_time_loop = False

    def start(self):
        # if (not(self.__test) and not(self.__console)):
        #     self.start_browser()
        #     self.start_ui_websocket()

        self.__start_time_loop()
        if not(self.__test):
            self.__start_input_loop()

    def stop(self):
        self.__stop_time_loop = True

    def __start_browser(self):
        os.system("x-www-browser ui.html")

    def __start_time_loop(self):
        self.__time_loop = Thread(target = self.__time_loop_routine)
        self.__time_loop.start()

    def __time_loop_routine(self):
        while True:
            if self.__stop_time_loop:
                break
            time.sleep(0.3)
            with self.__mutex:
                self.__game.next_tick()
                if not(self.__test):
                    self.render()

    def process_user_input(self, input):
        if input == '4':
            self.__game.move_horizontal('left')
        elif input == '6':
            self.__game.move_horizontal('right')
        elif input == '1':
            self.__game.rotate('counter_clockwise')
        elif input == '3':
            self.__game.rotate('clockwise')
        elif input == 'q':
            print("quitting...")
            self.stop()
            exit()
        else:
            pass

    def render(self):
        if self.__console:
            def cell_str(cell):
                return cell.to_s() if cell else "-"
            def print_line(str):
                print(str + "\r")

            print_line("======================")
            for row in self.__game.grid():
                print_line("".join([cell_str(cell) for cell in row]))
            print_line("press q to quit")

    def __start_input_loop(self):
        while True:
            input_var = easy_getch.getch()
            with self.__mutex:
                self.process_user_input(input_var)
                self.render()

    @property
    def mutex(self):
        return self.__mutex

    @property
    def game(self):
        return self.__game

    @property
    def time_loop(self):
        return self.__time_loop

