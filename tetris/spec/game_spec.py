# author: Stephan Becque (https://github.com/sjbecque)
from mamba import shared_context, included_context, it, before, describe
from expects import expect, equal, have_property, be_a
from tetris.src.game import Game
from tetris.src.tetromino_factory import TetrominoFactory
from tetris.src.cube_sets.stones import Stones
from tetris.src.cube_sets.tetromino import Tetromino
from doublex_expects import *
from doublex import Spy
import copy
from tetris.src.cube import Cube
# from tetris.src.cube_sets.cube_set import CubeSet


def setup(ctx):
    ctx.factory = TetrominoFactory()
    ctx.tetromino = ctx.factory._TetrominoFactory__tetrominos()[0]
    ctx.stones = Stones()
    ctx.width = 20
    ctx.height = 20
    setup_subject(ctx)

def setup_subject(ctx):
    ctx.tetromino_orig = copy.deepcopy(ctx.tetromino)
    ctx.stones_orig = copy.deepcopy(ctx.stones)

    ctx.subject = Game(
        ctx.width,
        ctx.height,
        ctx.tetromino,
        ctx.stones
    )

with describe(Game) as self:
    with before.each:
        setup(self)

    with shared_context('handling moving-down collision'):
        with it('turns the tetromino into stones'):
            self.subject.next_tick()
            expect( all([cube.is_stone() for cube in self.tetromino.cubes]) ).to(equal(True))

        with it('instantiates a new tetromino while retaining all stones'):
            self.subject.next_tick()

            original_plus_spawned_count = (self.tetromino_orig.count + self.stones_orig.count + self.factory.produce().count)
            current_count = (self.subject.tetromino.count + self.subject.stones.count)

            expect(original_plus_spawned_count).to(equal(current_count))

    with shared_context('handling horizontal collision'):
        with it('lets the tetromino stay put'):
            coordinates = lambda: [cube.coordinates for cube in self.subject.tetromino.cubes]
            before = coordinates()
            self.subject.move_horizontal(self.command)
            after = coordinates()
            expect(before).to(equal(after))

    with it('its collections contain arrays of cubes'):
        cubes = self.subject.tetromino.cubes + self.subject.stones.cubes
        for cube in cubes:
            expect(cube).to(be_a(Cube))

    with describe('next_tick') as self:
        with it('moves the tetromino down one spot'):
            cubes = lambda: [cube.y for cube in self.subject.tetromino.cubes]
            expect(cubes()).to(equal([0, 1, 1, 2]))
            self.subject.next_tick()
            expect(cubes()).to(equal([1, 2, 2, 3]))

        with describe('tetromino at the bottom'):
            with before.each:
                self.tetromino = Tetromino.c(
                    [10, self.height - 1],
                    [11, self.height - 1]
                )
                self.stones = Stones.c( [0, self.height - 1] )
                setup_subject(self)
            with included_context('handling moving-down collision'):
                pass

        with describe('tetrinomo just above a stone'):
            with before.each:
                setup(self)
                self.tetromino = Tetromino.c(
                    [0, self.height - 3],
                    [0, self.height - 2]
                )
                self.stones = Stones.c( [0, self.height - 1] )
                setup_subject(self)
            with included_context('handling moving-down collision'):
                pass

    with describe('process user input'):
        with it('moves tetromino to the left'):
            values = lambda: [cube.x for cube in self.subject.tetromino.cubes]
            expect(values()).to(equal([10, 10, 11, 11]))
            self.subject.move_horizontal('left')
            expect(values()).to(equal([9, 9, 10, 10]))

        with it('moves tetromino to the right'):
            values = lambda: [cube.x for cube in self.subject.tetromino.cubes]
            expect(values()).to(equal([10, 10, 11, 11]))
            self.subject.move_horizontal('right')
            expect(values()).to(equal([11, 11, 12, 12]))

        with describe('rotate'):
            with it('rotates tetromino clockwise (note that y-axis points south) and performs rotation correction'):
                self.subject.rotate('clockwise')
                rotated = [
                    Cube(12, 0, False),
                    Cube(11, 0, True),
                    Cube(11, 1, False),
                    Cube(10, 1, False)
                ]
                expect(self.subject.tetromino.cubes).to(equal(rotated))

        with describe('when at the leftedge'):
            with before.each:
                setup(self)
                self.tetromino = Tetromino.c( [0, 0] )
                setup_subject(self)
                self.command = 'left'
            with included_context('handling horizontal collision'):
                pass

        with describe('when at the leftedge'):
            with before.each:
                setup(self)
                self.tetromino = Tetromino.c( [19, 0] )
                setup_subject(self)
                self.command = 'right'
            with included_context('handling horizontal collision'):
                pass

        with describe('case of cube collision'):
            with before.each:
                setup(self)
                self.tetromino = Tetromino.c( [10, 0], [11, 1] )
                self.stones = Stones.c( [12, 1] )
                setup_subject(self)

            with it("doesn't react"):
                coordinates = lambda: [cube.coordinates for cube in self.subject.tetromino.cubes]
                before = coordinates()
                self.subject.move_horizontal('right')
                after = coordinates()
                expect(before).to(equal(after))

    with describe('grid'):
        with before.each:
            self.flat = [cube for row in self.subject.grid() for cube in row]

        with it('produces rows of cubes and nones'):
            compact = [cube for cube in self.flat if cube]
            for cube in compact:
                expect(cube).to(be_a(Cube))

        with it('has the right dimensions'):
            expect(len(self.subject.grid()[0])).to(equal(self.width))
            expect(len(self.flat)).to(equal(self.width*self.height))

        with it('returns a cube at the right spot'):
            expect(self.subject.grid()[0][10]).to(be_a(Cube))
