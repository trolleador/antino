#importamos la biblioteca XD
import pygame
from pygame.locals import *
import sys
import os #esto es para dirname




dirname = os.path.dirname(__file__)+"/"
 

class Jugador:
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

class Bala:
   def __init__(self, position_x, position_y, velocity_x, velocity_y, imagen):
      self.x = position_x
      self.y = position_y
      self.imagen = pygame.image.load(dirname+imagen)
      self.vx = velocity_x 
      self.vy = velocity_y

   def movimiento(self):
      self.x = self.x + .01*self.vx
      self.y = self.y + .01*self.vy

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

player = Jugador(100,100,"personayarma.png")

fondo = pygame.image.load(dirname+"fondo.png")

zorro = pygame.image.load(dirname+"zorro2.png")

bala = Bala(100,100,0,0,"bala.png")

#loop principal:

while True:

   #Se necesita rellenar toda la pantalla con un color para que el frame anterior no salga como fondo
   displaysurface.fill((255,255,255))

   #cierra el progama si aplastas la "x" en la ventana
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()
         
      if event.type == pygame.MOUSEBUTTONUP:
         pos = pygame.mouse.get_pos()
         bala.x = player.x
         bala.y = player.y
         bala.vx = pos[0]-player.x
         bala.vy = pos[1]-player.y


    

   #checa que teclas están oprimidas
   pressed = pygame.key.get_pressed()


   #movimiento con clases 
   player.movimiento(pressed)
   bala.movimiento()


   #renderizado

   displaysurface.blit(fondo, (0,0))
   displaysurface.blit(zorro, (150,150))


   displaysurface.blit(player.imagen, (player.x,player.y))


   displaysurface.blit(bala.imagen, (bala.x,bala.y))

   #actualiza lo que se ve en ventana
   pygame.display.update()

   #limita los fps
   FramePerSec.tick(FPS)
    
    