import pygame

class Racket(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.rect = pygame.Rect(x, y, 10, 70)
        
        self.speed = 8
        
    def mouvement(self, keyUP, keyDOWN) -> None:
        keys = pygame.key.get_pressed()
        if keys[keyDOWN] and self.rect.bottom <= 360:
            self.rect.y += self.speed
        if keys[keyUP] and self.rect.top >= 0:
            self.rect.y -= self.speed
        
    def draw(self) -> None:
        pygame.draw.rect(self.surface, (255, 255, 255), self.rect)