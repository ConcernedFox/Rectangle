import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
class Circle():
    def __init__(self):
        self.color = input("What color do you want in the circle?")
        self.x = 250.5
        self.y = 250.5
        self.radius = 100
        self.width = 100
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.width) 
    def draw_again(self, radius):
        self.radius = self.radius + radius
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.width) 
Vihaan_G = Circle()
while True:
    for p in pygame.event.get():
        if p.type == pygame.QUIT:
            pygame.quit()  
        elif p.type == pygame.MOUSEBUTTONDOWN:
            Vihaan_G.draw()
            pygame.display.update()
        elif p.type == pygame.MOUSEBUTTONUP:
            Vihaan_G.draw_again(5)
            pygame.display.update()