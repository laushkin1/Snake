import pygame

from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, screen) -> None:
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('game/sprites/snake_body.png')
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        
    def move_player(self, direction = 4):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            direction = 0
        if keys[pygame.K_d]:
            direction = 1
        if keys[pygame.K_s]:
            direction = 2
        if keys[pygame.K_a]:
            direction = 3

        if direction == 0:
            self.rect.y -= 5
        elif direction == 1:
            self.rect.x += 5
        elif direction == 2:
            self.rect.y += 5
        elif direction == 3:
            self.rect.x -= 5

    def update(self):
        self.move_player()

