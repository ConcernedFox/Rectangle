import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
class Circle():
    def __init__(self):
        self.color = input("What color do you want in the circle?")
        self.x = 250.5
        self.y = 250.5
        self.radius = int(input("What number do you want from 1 to 10"))
        self.width = int(input("What number do you want from 1 to 10"))
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.width)        
Vihaan_G = Circle()
Vihaan_G.draw()
pygame.display.update()
while True:
    for p in pygame.event.get():
        if p.type == pygame.QUIT:
            pygame.quit()   