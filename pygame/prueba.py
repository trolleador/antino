#importamos la biblioteca XD
import pygame
from pygame.locals import *
import sys
import os #esto es para dirname




dirname = os.path.dirname(__file__)+"/"
 

class jugador:
   

   def __init__(self, position_x, position_y, imagen):
      self.x = position_x
      self.y = position_y
      self.imagen = pygame.image.load(dirname+imagen)

   def movimiento(self, pressed):
      if pressed[pygame.K_w]:
         self.y -= 2
      if pressed[pygame.K_s]:
         self.y += 2
      if pressed[pygame.K_a]:
         self.x -= 2
      if pressed[pygame.K_d]:
         self.x += 2



#iniciadores
pygame.init()

HEIGHT = 700
WIDTH = 700
FPS = 60

#ventana 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Matar zorros")
 
FramePerSec = pygame.time.Clock()




rect = pygame.Rect(20,20,20,20)

#imagenimage.png

#Player pero con clases, (oUwUo) : 

player = jugador(100,100,"personayarma.png")

fondo = pygame.image.load(dirname+"fondo.png")

zorro = pygame.image.load(dirname+"zorro2.png")

bala = pygame.image.load(dirname+"bala.png")

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


   #movimiento con clases 
   player.movimiento(pressed)


   #renderizado

   displaysurface.blit(fondo, (0,0))
   displaysurface.blit(zorro, (150,150))


   displaysurface.blit(player.imagen, (player.x,player.y))


   displaysurface.blit(bala, (15,15))

   #actualiza lo que se ve en ventana
   pygame.display.update()

   #limita los fps
   FramePerSec.tick(FPS)
    
    