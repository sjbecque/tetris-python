# author: Stephan Becque (https://github.com/sjbecque)
from expects import expect, equal, be_a, be
from tetris.src.tetromino_factory import TetrominoFactory
from tetris.src.cube_sets.tetromino import Tetromino

with describe(Cube) as self:
    with describe('produce'):
        with it('produces tetrominos'):
            expect(TetrominoFactory().produce()).to(be_a(Tetromino))