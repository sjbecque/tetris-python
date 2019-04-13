from mamba import description, context, it
from expects import expect, equal
from engine import Engine
import time

with description('the engine loops') as self:
    with it('successfully produces list items and receives user input'):
        timeout = 3
        engine = Engine(True, timeout)
        time.sleep(3)
        with engine.mutex:
            engine.game.process_user_input("input")
            expect(engine.game.items).to(equal(["value","value","input"]))
