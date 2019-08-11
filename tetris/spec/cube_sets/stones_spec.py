# author: Stephan Becque (https://github.com/sjbecque)
from expects import expect, equal, be_a, be
from tetris.src.cube import Cube
from tetris.src.cube_sets.cube_set import CubeSet
from tetris.src.cube_sets.stones import Stones

with describe(Stones) as self:
    with it('its factory method produces a Stones object'):
        expect(Stones.c([1,1])).to(be_a(Stones))

    with describe('process_completed_rows') as self:

        with it('removes all full rows and moves all stones above it down'):
            subject = Stones.c(\
                       [2,1],\
                [1,2], [2,2],\
                [1,3],\
                [1,4], [2,4],\
                [1,5]\
            )
            expect(subject.process_completed_rows(2,5)).to(equal(
                Stones.c([2,3],[1,4],[1,5])
            ))