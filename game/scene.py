import pygame
import sys

from game.player import Player
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class BaseScene:
    def __init__(self, music_file=None):
        self.music_file = music_file
        self.score = None
        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def start_music(self):
        if self.music_file:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def run(self):
        pass

    def check_quit_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


class DrawSnake(BaseScene):
    def __init__(self) -> None:
        super().__init__()
        self.speed = 0.5
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(self.display))


    def my_events(self):
        for event in pygame.event.get():
            self.check_quit_event(event)


    def run(self):
        self.my_events()

        self.speed += 0.0005

        self.display.fill('white')
        
        self.player.draw(self.display)
        self.player.update()


class GameStateManager:
    def __init__(self, currentState) -> None:
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state

