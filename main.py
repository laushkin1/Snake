import pygame
import sys

from game.settings import FPS, SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_NAME

from game.scene import DrawSnake, GameStateManager

class Game:

    pygame.init()
    pygame.display.set_caption(WINDOW_NAME)
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.display = Game.display

        self.gameStateManager = GameStateManager("drawSnake")

        self.drawSnake = DrawSnake()

        self.states = {
            "drawSnake": self.drawSnake
        }

    def run(self):
        while True:
            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()

