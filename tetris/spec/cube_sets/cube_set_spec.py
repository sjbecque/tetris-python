# author: Stephan Becque (https://github.com/sjbecque)
from expects import expect, equal, be_a, be
from tetris.src.cube import Cube
from tetris.src.cube_sets.cube_set import CubeSet

with describe(CubeSet) as self:
    with describe('clone') as self:
        with it('produces a clone'):
            cube_set = CubeSet.c([0,0])
            clone = cube_set.clone()
            expect(clone).to(be_a(CubeSet))
            expect(cube_set.cubes[0]).not_to(be(clone.cubes[0]))

    with describe('==') as self:
        with it('equates equivalent cube_sets correctly'):
            expect(CubeSet.c([2,1],[1,2]) == CubeSet.c([1,2],[2,1])).to(equal(True))
            expect(CubeSet.c([2,1],[1,2]) == CubeSet.c([1,2],[1,2])).to(equal(False))

    with describe('get') as self:
        with it(''):
            cube_coordinates = [1,1]
            cube_set = CubeSet.c([0,0],cube_coordinates)
            expect(cube_set.get(1,1)).to(equal(Cube(*cube_coordinates)))
