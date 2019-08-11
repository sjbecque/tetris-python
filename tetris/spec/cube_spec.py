# author: Stephan Becque (https://github.com/sjbecque)
from expects import expect, equal, be_a, be
from tetris.src.cube import Cube

with describe(Cube) as self:
    with before.each:
        self.subject = Cube(5,2)

    with describe('+'):
       with it('adds another Cube vector'):
           expect(self.subject + Cube(1,1)).to(equal(Cube(6,3)))

    with describe('rotate'):
       with it('rotates counter-clockwise relative to origin (note that y-axis points south)'):
           origin = Cube(1,1)
           before = self.subject.coordinates
           expect(before).to(equal([5,2]))

           self.subject.rotate(origin, 'counter_clockwise')
           after = self.subject.coordinates
           expect(after).to(equal(
               (origin + Cube(1,-4)).coordinates
           ))
