# Importing modules
import pygame
from math import *
import sys
from random import *

# Initialization of Pygame
pygame.init()
width =1200
height = 700
ball_numbers = int(input("Enter the numbers of blocks: "))
boxw,boxh = float(input("Enter the box width: ")),float(input("Enter the box height: "))
e = float(input("Enter the collision coffiecient (coffiecient of restitution): "))
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("balls")
clock = pygame.time.Clock()
enter = True
FPS = 25
balls = []
vx = []
vy = []
flag = 0
time = 0
xrange = [10,16]
yrange = [10,16]
ccx,ccy = boxw,boxh
collisions = 0
for value in range(ball_numbers):
    balls.append([randint(10,width-10),height-10,(randint(50,255),randint(50,255),randint(50,255))])
    vx.append(randint(xrange[0],xrange[1]))
    vy.append(randint(yrange[0],yrange[1]))
def see(balls):
    for list in balls:
        pygame.draw.rect(screen,list[2], [list[0],list[1],boxw,boxh])
while enter:
    time+=(1/FPS)
    if ((int(time)+1)-time)<(1001/(1000*FPS)):
         time = int(time)+1
  #  print(time)
 #   if time==int(time):
   # balls.pop()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                for index,v in enumerate(vx):
                    vx[index]-=1
                    vy[index]-=1

    screen.fill((0,0,0))
    see(balls)
    for index,list in enumerate(balls):
        list[0]+=vx[index]
        list[1]-=vy[index]
    for index,list in enumerate(balls):
        if list[0]>(width-5) or list[0]<5:
            vx[index] = -vx[index]
        if list[1]>(height-10) or list[1]<5:
            vy[index] = -vy[index]
    for indexf,balf in enumerate(balls):
        for indexs,bals in enumerate(balls):
            if abs(balf[0]-bals[0])<ccx and abs(balf[1]-bals[1])<ccy:
                temp = vx[indexf]
                vx[indexf] = (vx[indexs]*(1+e)+vx[indexf]*(1-e))/2
                vx[indexs] = (temp*(1+e)+vx[indexs]*(1-e))/2
                

                temp = vy[indexf]
                vy[indexf] = (vy[indexs]*(1+e)+vy[indexf]*(1-e))/2
                vy[indexs] = (temp*(1+e)+vy[indexs]*(1-e))/2       
                break
    
    pygame.display.update()
    clock.tick(FPS)

