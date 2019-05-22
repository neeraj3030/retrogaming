import pygame

pygame.init()

black=(0,0,0)
red=(255,0,0)
white=(255,255,255)



gameDisplay=pygame.display.set_mode((600,600))

gameDisplay.fill(black)
pr=pygame.PixelArray(gameDisplay)
pr[300][300]= red


pygame.display.update()

pygame.quit()