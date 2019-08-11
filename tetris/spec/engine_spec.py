# author: Stephan Becque (https://github.com/sjbecque)
from mamba import description, context, it
from expects import expect, equal
from tetris.src.engine import Engine
import time

with description('the engine loops') as self:
    with it('tells the game periodically to advance to next tick'):
        subject = Engine(True, True)
        subject.start()
        time.sleep(1)
        expect(subject._Engine__game._Game__tick_count).to(equal(3))
        subject.stop()
