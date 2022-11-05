#importamos la biblioteca XD
import pygame
from pygame.locals import *
import sys
 

#iniciadores
pygame.init()

HEIGHT = 800
WIDTH = 800
FPS = 60

#ventana 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Never gonna give you up Never gonna let you down Never gonna run around and desert you")
 
FramePerSec = pygame.time.Clock()

x = 0
y = 0

rect = pygame.Rect(20,20,20,20)

#imagen

zorro = pygame.image.load("C:/Users/Cecilia/Desktop/yo/pygame/zorro nft.png")

#loop principal:

while True:

   #Se necesita rellenar toda la pantalla con un color para que el frame anterior no salga como fondo
   displaysurface.fill((0,0,0))

   #cierra el progama si aplastas la "x" en la ventana
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

    

   #checa que teclas están oprimidas
   pressed = pygame.key.get_pressed()

   #movimiento
   if pressed[pygame.K_w]:
      rect.y -= 2
   if pressed[pygame.K_s]:
      rect.y += 2
   if pressed[pygame.K_a]:
      rect.x -= 2
   if pressed[pygame.K_d]:
      rect.x += 2


   #renderizado
   pygame.draw.rect(displaysurface, (255,0,0), rect)

   displaysurface.blit(zorro, (rect.x,rect.y))
   
   #actualiza lo que se ve en ventana
   pygame.display.update()

   #limita los fps
   FramePerSec.tick(FPS)
    
    