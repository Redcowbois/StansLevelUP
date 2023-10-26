import pygame
import os
import re
import pygame_textinput
import sys
from LevelManager import *
import Storage

#Initializing pygame variables
pygame.init()
pygame.display.set_caption("Level Up")

canvas = pygame.display.set_mode((500, 500))  
clock = pygame.time.Clock()
textInput = pygame_textinput.TextInputVisualizer(cursor_blink_interval=450)

#UI Elements 
redoButton = pygame.image.load("textures/redo.png")
enterButton = pygame.image.load("textures/enter.png")

#Program main loop
while True:
    canvas.fill((225, 225, 225))
    events = pygame.event.get()

    #Update the text input
    textInput.update(events)
    if len(textInput.value) > 10:
        textInput.value = textInput.value[:-1]

    #Check events
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: #If return, print value
            try: 
                input = float(textInput.value)
                print(input)
            except:
                textInput.value = ""


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Update UI
    textInputSurface = pygame.Surface((210, 50))
    textInputSurface.fill((255,255,255))
    canvas.blit(textInputSurface, textInputSurface.get_rect(topleft = (50,50)))

    canvas.blit(textInput.surface, (60, 62))
    canvas.blit(redoButton, redoButton.get_rect(topleft = (340, 50)))
    canvas.blit(enterButton, enterButton.get_rect(topleft = (420, 50)))
    pygame.display.update()
    clock.tick(30)