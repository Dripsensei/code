import pygame
from sys import exit 
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])
pygame.display.set_caption('Dragons veil')
clock = pygame.time.Clock()

test_surface = pygame.Surface([ 500, 500 ])
test_surface.fill('Blue')

# Run until the user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit()
    screen.blit(test_surface,(400,500))
    pygame.display.update()
    clock.tick(60)
    