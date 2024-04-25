import pygame

from sys import exit
from racket import Racket
from ball import Ball

pygame.init()

class Game:
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.displaySurface = pygame.display.set_mode((640, 360))
        
        self.font = pygame.font.Font('dogica.ttf', 50)
        
        self.player1 = Racket(10, 130)
        self.player2 = Racket(620, 130)
        self.ball = Ball()
        
        self.scorePlayer1 = 0
        self.scorePlayer2 = 0
        
    def run(self) -> None:
        while True:
            
            self.displaySurface.fill((0, 0, 0))
            pygame.draw.rect(self.displaySurface, (255, 255, 255), (310, 0, 1, 360))
            
            self.player1.draw()
            self.player2.draw()
            
            self.ball.draw()
            
            score1 = self.font.render(str(self.scorePlayer1), False, (255, 255, 255))
            self.displaySurface.blit(score1, (260, 10))
            score2 = self.font.render(str(self.scorePlayer2), False, (255, 255, 255))
            self.displaySurface.blit(score2, (320, 10))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            if self.ball.rect.right >= 640:
                self.scorePlayer1 += 1
                self.ball.__init__()
            elif self.ball.rect.left <= 0:
                self.scorePlayer2 += 1
                self.ball.__init__()
                    
            self.player1.mouvement(pygame.K_w, pygame.K_s)
            self.player2.mouvement(pygame.K_i, pygame.K_k)
            
            self.ball.collision([self.player1.rect, self.player2.rect])
            self.ball.mouvement()
                    
            pygame.display.flip()
            self.clock.tick(60)
                    
if __name__ == "__main__":
    pong = Game()
    pong.run()