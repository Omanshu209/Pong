import pygame
from random import randint

pygame.init()

win = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Pong!")

rect1y=350
rect2y=350
FPS=42
ball1x=550
ball1y=100
ballPos=1
hit=0
ballSpeed=9
rect1w=10
rect1l=85
rect2w=10
rect2l=85
wall=False
i=0
m=0
rect1up=False
rect1c=False
rect1down=False
rect2up=False
rect2c=False
rect2down=False
up=False
down=False
up2=False
down2=False
compY=randint(-100,0)
AIY=randint(-70,-20)
score1=0
score2=0
AI="off"
col=(0,255,0)

class text:
    def __init__(self,nameA,size,nameB,word,colour,posX,posY):
        self.nameA=pygame.font.SysFont("comicsans",size,True)
        self.nameB=self.nameA.render(word,1,colour)
        win.blit(self.nameB,(posX,posY))
    
def DrawGameWindow():
    global wall,i,ball1x,ballPos,ball1y,luck,m,score1,score2,compY
    win.fill((0,0,0))
    pygame.draw.rect(win,col,(0,0,1100,700),7)
    pygame.draw.rect(win,(0,0,255),(1107,0,150,700),7)
    pygame.draw.rect(win,(255,0,127),(1110,530,142,165))
    pygame.draw.rect(win,(0,255,0),(1110,530,142,165),4)
    pygame.draw.rect(win,(255,255,0),(0,703,1259,20),4)
    pygame.draw.rect(win,(255,255,255),(20,rect1y,rect1w,rect1l))
    pygame.draw.rect(win,(255,255,255),(1075,rect2y,rect2w,rect2l))
    pygame.draw.rect(win,(255,255,255),(545,20,7,665))
    text("scoreA",100,"scoreA2",f"{score1}",(255,0,0),225,50)
    text("scoreB",100,"scoreB2",f"{score2}",(255,0,0),775,50)
    text("AI",150,"AI2","AI",(102,0,204),1120,550)
    text("AI2",45,"AI22",f"{AI}",(0,255,0),1162,650)
    text("om",20,"om2","M      A      D      E           B      Y           O      M      A      N      S      H      U",(225,128,0),300,707)
    text("upm",40,"upm2","UP : R",(255,255,0),1112,30)
    text("downm",38,"downm2","DOWN : F",(255,255,0),1112,60)
    if ball1x<40:
        if ball1y<rect1y-5 or ball1y>rect1y+90:
            wall=True
            while i < 100 :
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()
            wall=False
            ball1x=550
            ball1y=350
            i=0
            if ballPos==1:
                ballPos=-1
                score1+=1
            elif ballPos==-1:
                ballPos=1
                score2+=1
    if ball1x>1060:
        if ball1y<rect2y-5 or ball1y>rect2y+90:
            wall=True
            while m < 100 :
                pygame.time.delay(10)
                m+= 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        m = 301
                        pygame.quit()
            wall=False
            ball1x=550
            ball1y=350
            m=0
            if ballPos==1:
                score1+=1
            elif ballPos==-1:
                ballPos=1
                score2+=1
    if ball1x==550 and ballPos==1:
        if AI=="off":
            if score1<score2:
                compY=randint(-120,7)
            elif score1>=score2:
                compY=randint(-112,3)
        elif AI=="on":
            AIY=randint(-70,-20)
    if wall==False:
        pygame.draw.circle(win,(211,211,211), (ball1x,ball1y), 9)
    pygame.display.update()
    
clock=pygame.time.Clock()
run=True
while run:
    if rect2y<601:
        if AI=="off":
            rect2y=ball1y+compY
        elif AI=="on":
            rect2y=ball1y+AIY
    else:
        rect2y=600
    rect1upS=rect1y-4
    rect1upE=rect1y+35
    rect1cS=rect1y+36
    rect1cE=rect1y+50
    rect1downS=rect1y+51
    rect1downE=rect1y+90
    rect2upS=rect2y-4
    rect2upE=rect2y+35
    rect2cS=rect2y+36
    rect2cE=rect2y+50
    rect2downS=rect2y+51
    rect2downE=rect2y+90
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            if mx>=1110 and my>=530 and mx<=1252 and my<=695:
                if AI=="off":
                    AI="on"
                    col=(255,0,0)
                elif AI=="on":
                    AI="off"
                    col=(0,255,0)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_r] and rect1y>20:
        rect1y-=10
    elif keys[pygame.K_f] and rect1y<590:
        rect1y+=10
    if ball1x>1060 and wall==False:
        ballPos=-1
        if ball1y>rect2upS and ball1y<rect2upE and ball1x>1055:
            rect2up=True
            up=False
            down=False
        elif ball1y>rect2cS and ball1y<rect2cE and ball1x>1055:
            rect2c=True
        elif ball1y>rect2downS and ball1y<rect2downE and ball1x>1055:
            rect2down=True
            up=False
            down=False
    elif ball1x<40 and wall==False:
        ballPos=1
        if ball1y>rect1upS and ball1y<rect1upE and ball1x<45:
            rect1up=True
            up=False
            down=False
        elif ball1y>rect1cS and ball1y<rect1cE and ball1x<45:
            rect1c=True
        elif ball1y>rect1downS and ball1y<rect1downE and ball1x<45:
            rect1down=True
            up=False
            down=False
    if hit==0 and wall==False:
        ball1x+=ballSpeed*ballPos
    if rect1up==True and wall==False:
        if ball1y>41:
            ball1y-=5
        else:
            rect1up=False
    elif rect1down==True and wall==False:
        if ball1y<679:
            ball1y+=5
        else:
            rect1down=False
    if rect2up==True and wall==False:
        if ball1y>41:
            ball1y-=5
        else:
            rect2up=False
    elif rect2down==True and wall==False:
        if ball1y<679:
            ball1y+=5
        else:
            rect2down=False
    elif ball1y<=680 and ball1y>660 and wall==False:
        up=True
        rect1up=False
        rect1down=False
    elif ball1y>=10 and ball1y<50 and wall==False:
        down=True
        rect1up=False
        rect1down=False
    if down==True:
        if ball1y<680:
            ball1y+=5
        else:
            compY=randint(-100,0)
            down=False
    elif up==True:
        if ball1y>20:
            ball1y-=5
        else:
            compY=randint(-100,0)
            up=False

    DrawGameWindow()

pygame.quit()
