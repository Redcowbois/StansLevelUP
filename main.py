import pygame
import pygame_textinput
import sys
from LevelManager import *
import Storage
from math import floor

#Initializing pygame variables
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.set_caption("Level Up")

canvas = pygame.display.set_mode((500, 270))  
clock = pygame.time.Clock()
textInput = pygame_textinput.TextInputVisualizer(cursor_blink_interval=450)


# Initializing LevelManager
initialLevel, initialHistory = Storage.readStorage()
levelManager = LevelManager(initialLevel, initialHistory)


#UI Elements 
redoButton = pygame.image.load("textures/redo.png")
enterButton = pygame.image.load("textures/enter.png")
xpText = font.render("Progress:", False, (0,0,0))
levelText = font.render("Level:  " + str(floor(levelManager.timeToLevel())), False, (0,0,0))
updateLevel = False


#Program main loop
while True:
    canvas.fill((225, 225, 225))
    events = pygame.event.get()
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
                updateLevel = True
            except:
                pass
            finally: 
                textInput.value = ""

        if (event.type == pygame.MOUSEBUTTONDOWN and mousePosX > 340 and mousePosX < 390 and mousePosY > 50 and mousePosY < 100):
            levelManager.undoEntry()
            levelText = font.render("Level:  " + str(floor(levelManager.timeToLevel())), False, (0,0,0))
            Storage.writeStorage(levelManager.timeSpent, levelManager.timeHistory)

        # Press Quit button
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            Storage.writeStorage(levelManager.timeSpent, levelManager.timeHistory)
            pygame.quit()
            sys.exit()



    ### Update UI
    # Text Input
    if updateLevel:
        levelText = font.render("Level:  " + str(floor(levelManager.timeToLevel())), False, (0,0,0))
        Storage.writeStorage(levelManager.timeSpent, levelManager.timeHistory) 
        updateLevel = False

    textInputBackgroundSurface = pygame.Surface((210, 50))
    textInputBackgroundSurface.fill((255,255,255))
    canvas.blit(textInputBackgroundSurface, textInputBackgroundSurface.get_rect(topleft = (50,50)))
    canvas.blit(textInput.surface, (60, 62))
    
    # Buttons
    canvas.blit(redoButton, redoButton.get_rect(topleft = (340, 50)))
    canvas.blit(enterButton, enterButton.get_rect(topleft = (420, 50)))

    # Xp Bar and Level
    canvas.blit(levelText, (50, 130))
    xpBackgroundSurface = pygame.Surface((400, 50))
    xpBackgroundSurface.fill((255, 255, 255))
    processValue = floor(400 * ((levelManager.timeToLevel()) - floor(levelManager.timeToLevel())))
    xpProgressSurface = pygame.Surface((processValue, 50))
    xpProgressSurface.fill((60, 225, 60))
    canvas.blit(xpBackgroundSurface, xpBackgroundSurface.get_rect(topleft = (50, 175)))
    canvas.blit(xpProgressSurface, xpProgressSurface.get_rect(topleft = (50, 175)))
    
    pygame.display.update()
    clock.tick(30)