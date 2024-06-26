import pygame
from random import choice

class Ball(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.rect = pygame.Rect(305, 165, 10, 10)
        
        self.speed = 4
        self.maxSpeed = 5
        self.direction = pygame.Vector2()
        self.direction.x = choice([-1, 1])
        self.direction.y = 1
    
    def mouvement(self) -> None:
        self.rect.x += self.speed * self.direction.x
        self.rect.y += self.speed * self.direction.y
        
    def collision(self, colliderList: list[pygame.Rect]) -> None:
        if self.rect.bottom >= 360 or self.rect.top <= 0:
            self.direction.y *= -1
        for collider in colliderList:
            if self.rect.colliderect(collider):
                offsetTop = collider.bottom - self.rect.top
                offsetBottom = self.rect.bottom - collider.top
                offsetRight = collider.left - self.rect.right
                offsetLeft = self.rect.left - collider.right
                if offsetRight < 6 and offsetRight > -6 or offsetLeft < 6 and offsetLeft > -6:
                    if self.rect.right >= collider.left or self.rect.left <= collider.right and offsetTop < 5 and offsetTop > -5:
                        self.direction.x *= -1
                        if self.speed < self.maxSpeed : self.speed += 0.25
                if offsetTop < 6 and offsetTop > -6 or offsetBottom < 6 and offsetBottom > -6:
                    if self.rect.top <= collider.bottom or self.rect.bottom >= collider.top:
                        self.direction.y *= -1
                        if self.speed < self.maxSpeed : self.speed += 0.25
    
    def draw(self) -> None:
        pygame.draw.rect(self.surface, (255, 255, 255), self.rect)