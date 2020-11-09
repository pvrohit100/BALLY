#import libraries
import pygame,sys
from pygame.locals import *

from random import seed
from random import randint

# seed random number generator
seed(15)

###########

pygame.init()

#screen
disp=pygame.display.set_mode((650,650))
pygame.display.set_caption("Bally Game")
#disp.fill((0,100,0))
bg = pygame.image.load('clouds.jpeg')
explosion=pygame.image.load('ex.png')
life=pygame.image.load('lifewbg.png')
nail=pygame.image.load('nailaa.png')
disp.blit(bg,(0,0))

FPS=100
iflife=0
lives=3

ifout=0

fpsclk=pygame.time.Clock()

#game variables
block1x,block1y=randint(0, 600),randint(0, 12)*50
block2x,block2y=randint(0, 600),randint(0, 12)*50
block3x,block3y=randint(0, 600),randint(0, 12)*50
block4x,block4y=randint(0, 600),randint(0, 12)*50
block5x,block5y=randint(0, 600),randint(0, 12)*50
block6x,block6y=randint(0, 600),randint(0, 12)*50

#rock1x,rock1y=randint(0, 600),randint(0, 12)*50
rock1x,rock1y=randint(0, 600),randint(0, 600)
rock2x,rock2y=randint(0, 600),randint(0, 600)

ballx,bally=300,40
lifex,lifey=0,0
score=0
fontObj = pygame.font.SysFont('calibri', 32)


while True:
    #display curr block & rock pos
    #disp.fill((100,200,0))
    
    disp.blit(bg,(0,0))

    



    
    
    if block1y<650:
        pygame.draw.line(disp,(60,60,200),(block1x,block1y),(block1x+75,block1y),10)
    if block2y<650:
        pygame.draw.line(disp,(60,60,200),(block2x,block2y),(block2x+75,block2y),10)
    if block3y<650:
        pygame.draw.line(disp,(60,60,200),(block3x,block3y),(block3x+75,block3y),10)
    if block4y<650:
        pygame.draw.line(disp,(60,60,200),(block4x,block4y),(block4x+75,block4y),10)
    if block5y<650:
        pygame.draw.line(disp,(60,60,200),(block5x,block5y),(block5x+75,block5y),10)
    if block6y<650:
        pygame.draw.line(disp,(60,60,200),(block6x,block6y),(block6x+75,block6y),10)

    #pygame.draw.line(disp,(100,0,0),(rock1x,rock1y),(rock1x+75,rock1y),10)
    disp.blit(nail,(rock1x,rock1y-5))
    #pygame.draw.line(disp,(100,0,0),(rock2x,rock2y),(rock2x+75,rock2y),10)
    disp.blit(nail,(rock2x,rock2y-5))

    pygame.draw.circle(disp,(0, 0, 120),(ballx,bally),20,0)
    pygame.draw.circle(disp,(0, 0, 200),(ballx,bally),20,5)
    

    seconds=pygame.time.get_ticks()
    text1=fontObj.render('SCORE: '+str(int((seconds/500))),3,(0,0,0))
    
    disp.blit(text1,(430,30))

    
    pygame.display.update()

    while ifout:
        #ifout=1
        #disp.blit(explosion,(ballx-50,bally-45))
        text1=fontObj.render('OUT',50,(0,0,0))
        disp.blit(text1,(300,300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

    for i in range(lives):
        disp.blit(life,(i*30,15))

    #update/move blocks rocks
    block1y=block1y-2
    block2y=block2y-2
    block3y=block3y-2
    block4y=block4y-2
    block5y=block5y-2
    block6y=block6y-2

    rock1y=rock1y-2
    rock2y=rock2y-2
    if iflife==1:
        lifey=lifey-2
        disp.blit(life,(lifex,lifey-25))
    pygame.display.update()

    #if out of screen generate new random blocks
    seed(seconds)
    if block1y<0:
        block1x,block1y=randint(0, 600),randint(14, 22)*50
        iflife=1#randint(0, 4)        #gen new life
        if iflife==1:
            lifex,lifey=block1x+20,block1y
    if block2y<0:
        block2x,block2y=randint(0, 600),randint(14, 22)*50
    if block3y<0:
        block3x,block3y=randint(0, 600),randint(14, 22)*50
    if block4y<0:
        block4x,block4y=randint(0, 600),randint(14, 22)*50                
    if block5y<0:
        block5x,block5y=randint(0, 600),randint(14, 22)*50
    if block6y<0:
        block6x,block6y=randint(0, 600),randint(14, 22)*50

    if rock1y<0:
        rock1x,rock1y=randint(0, 600),randint(700, 1100)
    if rock2y<0:
        rock2x,rock2y=randint(0, 600),randint(700, 1100)
    if bally<20 or bally>600:
        print("OUT")
        #fpsclk.tick(1)
        disp.blit(explosion,(ballx-50,bally-45))
        text1=fontObj.render('BOOM',50,(0,0,0))
        disp.blit(text1,(300,300))
        pygame.display.update()
        pygame.time.wait(1000)
        #ifout=1
        lives=lives-1
        if bally<20:
            bally=40#bally+20+max(-bally+block1y,-bally+block2y,-bally+block3y,-bally+block4y,-bally+block5y)
        else:       #actually min
            bally=40#bally+20+max(-bally+block1y,-bally+block2y,-bally+block3y,-bally+block4y,-bally+block5y)
        if lives==0:
            ifout=1
        
    #print(bally)
    #ball move down or on blocks
    
    

    if (bally+25>block1y and bally+10<block1y) and ((ballx+20)>block1x and (ballx-20)<(block1x+75)):
        bally=block1y-20
        if iflife==1:
            iflife=0
            lives=min(lives+1,5)

        
    elif (bally+25>block2y and bally+10<block2y) and ((ballx+20)>block2x and (ballx-20)<(block2x+75)):
        bally=block2y-20
        
    elif (bally+25>block3y and bally+10<block3y) and ((ballx+20)>block3x and (ballx-20)<(block3x+75)):
        bally=block3y-20
        
    elif (bally+25>block4y and bally+10<block4y) and ((ballx+20)>block4x and (ballx-20)<(block4x+75)):
        bally=block4y-20
        
    elif (bally+25>block5y and bally+10<block5y) and ((ballx+20)>block5x and (ballx-20)<(block5x+75)):
        bally=block5y-20
        
    elif (bally+25>block6y and bally+10<block6y) and ((ballx+20)>block6x and (ballx-20)<(block6x+75)):
        bally=block6y-20
        

    elif (bally+25>rock1y and bally+10<rock1y) and ((ballx+20)>rock1x and (ballx-20)<(rock1x+75)):
        text1=fontObj.render('BOOM',50,(0,0,0))
        disp.blit(text1,(300,300))
        print("OUT")
        disp.blit(explosion,(ballx-50,bally-45))
        pygame.display.update()
        #ifout=1
        lives=lives-1
        bally=40#bally+20+max(-bally+block1y,-bally+block2y,-bally+block3y,-bally+block4y,-bally+block5y)
        if lives==0:
            ifout=1
        
    elif (bally+25>rock2y and bally+10<rock2y) and ((ballx+20)>rock2x and (ballx-20)<(rock2x+75)):
        text1=fontObj.render('BOOM',50,(0,0,0))
        disp.blit(text1,(300,300))
        print("OUT")
        disp.blit(explosion,(ballx-50,bally-45))
        pygame.display.update()
        pygame.time.wait(1000)
        #ifout=1
        lives=lives-1
        bally=40#bally+20+max(-bally+block1y,-bally+block2y,-bally+block3y,-bally+block4y,-bally+block5y)
        if lives==0:
            ifout=1
       
    else:
        bally=bally+1
        

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                ballx=ballx-5
                
            elif event.key==K_RIGHT:
                ballx=ballx+5
        
        
        
        

        


        
    pygame.display.update()
    fpsclk.tick(FPS)

