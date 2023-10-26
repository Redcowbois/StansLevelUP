import pygame
import pygame_textinput
import sys
from LevelManager import *
import Storage


#Initializing pygame variables
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.set_caption("Level Up")

canvas = pygame.display.set_mode((500, 500))  
clock = pygame.time.Clock()
textInput = pygame_textinput.TextInputVisualizer(cursor_blink_interval=450)


# Initializing LevelManager
initialLevel, initialHistory = Storage.readStorage()
levelManager = LevelManager(initialLevel, initialHistory)


#UI Elements 
redoButton = pygame.image.load("textures/redo.png")
enterButton = pygame.image.load("textures/enter.png")
xpText = font.render("Progress", False, (0,0,0))
levelText = font.render("Level:" + str(levelManager.timeToLevel()), False, (0,0,0))


#Program main loop
while True:
    canvas.fill((225, 225, 225))
    events = pygame.event.get([pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN, pygame.QUIT])
    mousePosX, mousePosY = pygame.mouse.get_pos()

    #Update the text input
    textInput.update(events)
    if len(textInput.value) > 10:
        textInput.value = textInput.value[:-1]

    #Check events
    for event in events:
        # Press enter (keyboard or button)
        if ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) 
        or (event.type == pygame.MOUSEBUTTONDOWN and mousePosX > 420 and mousePosX < 470 and mousePosY > 50 and mousePosY < 100)):
            try: 
                input = float(textInput.value)
                if input < 0: #if negative
                    raise ValueError
                
                levelManager.addTime(input)
                levelText = font.render("Level:" + str(levelManager.timeToLevel()), False, (0,0,0))
                Storage.writeStorage(levelManager.timeSpent, levelManager.timeHistory)
            except:
                print("error")
            finally:
                textInput.value = ""

        if (event.type == pygame.MOUSEBUTTONDOWN and mousePosX > 340 and mousePosX < 390 and mousePosY > 50 and mousePosY < 100):
            levelManager.undoEntry()
            levelText = font.render("Level:" + str(levelManager.timeToLevel()), False, (0,0,0))
            Storage.writeStorage(levelManager.timeSpent, levelManager.timeHistory)

        # Press Quit button
        if event.type == pygame.QUIT:
            Storage.writeStorage(levelManager.timeSpent, levelManager.timeHistory)
            pygame.quit()
            sys.exit()



    ### Update UI
    # Text Input
    textInputSurface = pygame.Surface((210, 50))
    textInputSurface.fill((255,255,255))
    canvas.blit(textInputSurface, textInputSurface.get_rect(topleft = (50,50)))
    canvas.blit(textInput.surface, (60, 62))
    
    # Buttons
    canvas.blit(redoButton, redoButton.get_rect(topleft = (340, 50)))
    canvas.blit(enterButton, enterButton.get_rect(topleft = (420, 50)))

    # Xp Bar and Level
    canvas.blit(xpText, (50, 300))
    canvas.blit(levelText, (50, 350))
    
    pygame.display.update()
    clock.tick(30)