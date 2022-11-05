#importamos la biblioteca XD
import pygame
from pygame.locals import *
import sys
import os




dirname = os.path.dirname(__file__)
 

#iniciadores
pygame.init()

HEIGHT = 700
WIDTH = 700
FPS = 60

#ventana 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Never gonna give you up Never gonna let you down Never gonna run around and desert you")
 
FramePerSec = pygame.time.Clock()

x = 0
y = 0

rect = pygame.Rect(20,20,20,20)

#imagen

zorro = pygame.image.load("C:/Users/Cecilia/Desktop/yo/pygame/zorro2.png")
fondo = pygame.image.load("C:/Users/Cecilia/Desktop/yo/pygame/fondo.png")
persona = pygame.image.load("C:/Users/Cecilia/Desktop/yo/pygame/personayarma.png")
bala = pygame.image.load("C:/Users/Cecilia/Desktop/yo/pygame/bala.png")

#loop principal:

while True:

   #Se necesita rellenar toda la pantalla con un color para que el frame anterior no salga como fondo
   displaysurface.fill((255,255,255))

   #cierra el progama si aplastas la "x" en la ventana
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

    

   #checa que teclas están oprimidas
   pressed = pygame.key.get_pressed()

   #movimiento
   if pressed[pygame.K_w]:
      y -= 2
   if pressed[pygame.K_s]:
      y += 2
   if pressed[pygame.K_a]:
      x -= 2
   if pressed[pygame.K_d]:
      x += 2


   #renderizado

   displaysurface.blit(fondo, (0,0))
   displaysurface.blit(zorro, (150,150))
   displaysurface.blit(persona, (x,y))
   
   displaysurface.blit(bala, (700,700))

   #actualiza lo que se ve en ventana
   pygame.display.update()

   #limita los fps
   FramePerSec.tick(FPS)
    
    