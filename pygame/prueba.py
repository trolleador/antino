import pygame
from pygame.locals import *
import sys
 

#iniciadores
pygame.init()

HEIGHT = 450
WIDTH = 400
FPS = 60

#ventana 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Game")
 
FramePerSec = pygame.time.Clock()

x = 0

rect = pygame.Rect(20,20,20,20)

#imagen

zorro = pygame.image.load('pygame\zorro nft.png')

#loop principal:

while True:

   displaysurface.fill((0,0,0))

   #cierra el progama si aplastas la "x" en la ventana
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

    

   pressed = pygame.key.get_pressed()
   if pressed[pygame.K_w]:
      rect.y -= 1
   if pressed[pygame.K_s]:
      rect.y += 1
   if pressed[pygame.K_a]:
      rect.x -= 1
   if pressed[pygame.K_d]:
      rect.x += 1

   pygame.draw.rect(displaysurface, (255,0,0), rect)

   displaysurface.blit(zorro, (rect.x,rect.y))

   x += .1
   #actualiza lo que se ve en ventana
   pygame.display.update()

   #limita los fps
   FramePerSec.tick(FPS)
    
    