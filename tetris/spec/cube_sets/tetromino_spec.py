# author: Stephan Becque (https://github.com/sjbecque)
from expects import expect, equal, be_a, be
from tetris.src.cube import Cube
from tetris.src.cube_sets.cube_set import CubeSet
from tetris.src.cube_sets.tetromino import Tetromino

with describe(Tetromino) as self:
    with it('its factory method produces a Tetromino object'):
        expect(Tetromino.c([1,1])).to(be_a(Tetromino))

    with describe('clone') as self:
        with it('copies Tetromino specific properties'):
            subject = Tetromino.c([1,1])
            rotation = 1
            corrections = {}
            subject.rotation = rotation
            subject.rotation_corrections = corrections
            clone = subject.clone()
            expect(clone.rotation).to(equal(rotation))
            expect(clone.rotation_corrections).to(equal(corrections))

# most other methods are covered by game_spec.py,
# which tested Tetromino behavior before it was
# extracted into its own class.