import pygame
import os
import pygame_textinput
import sys

#Initializing pygame variables
pygame.init()
pygame.display.set_caption("Level Up")

canvas = pygame.display.set_mode((500, 500))  
clock = pygame.time.Clock()
textinput = pygame_textinput.TextInputVisualizer()

#Program main loop
while True:
    canvas.fill((225, 225, 225))
    events = pygame.event.get()

    #Update the text input
    textinput.update(events)
    canvas.blit(textinput.surface, (10, 10))


    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(30)