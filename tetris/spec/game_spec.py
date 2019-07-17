from mamba import description, context, it
from expects import expect, equal
from tetris.src.game import Game

with description('next_tick') as self:
    with it('adds a value to items'):
        game = Game()
        expect(game.items).to(equal([]))
        game.next_tick()
        expect(game.items).to(equal(["value"]))

    with it('adds user input to items'):
        game = Game()
        expect(game.items).to(equal([]))
        game.process_user_input("input")
        expect(game.items).to(equal(["input"]))
