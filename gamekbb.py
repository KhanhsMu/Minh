# Write your# Write your code here :-)
import pygame
import pgzrun
import random
WIDTH = 800
HEIGHT = 615
bg = Actor('nen', size=(WIDTH, HEIGHT))
keo = Actor('keo')
keo.x = 200
keo.y = 550
bua = Actor('bua')
bua.x = 400
bua.y = 550
bao = Actor('bao')
bao.x = 600
bao.y = 550
may = random.randint(1, 3)
nguoi = 0
outcome = ""
sounds_play = False
play_nhac= 2
def update():
    global may, nguoi, outcome, sounds_play,play_nhac
    if keyboard.left or keyboard.a:
        nguoi = 1
    elif keyboard.down or keyboard.s:
        nguoi = 2
    elif keyboard.right or keyboard.d:
        nguoi = 3
    elif keyboard.RETURN:  # check if enter key is pressed
        reset_game()
    if keyboard.o:
        play_nhac = 1
    if keyboard.i:
        play_nhac = 0
    if play_nhac==1:
        sounds..play()
        play_nhac =2
    if play_nhac==0:
        sounds.nhac.stop()
        play_nhac =2
    if nguoi != 0:
        if nguoi == may:
            outcome = "HOA"
        elif nguoi == 1 and may == 3 or nguoi == 2 and may == 1 or nguoi == 3 and may == 2:
            if sounds_play == False:
                sounds.gamethang.play()
                outcome = "THANG"
            sounds_play = True
        else:
            if sounds_play == False:
                sounds.gamethua.play()
                outcome = "THUA"
            sounds_play = True
    if outcome != "":
        clock.schedule_unique(reset_game, 2)

def draw():
    bg.draw()
    keo.draw()
    bua.draw()
    bao.draw()
    screen.draw.text(outcome, (300, 100), color=(0, 0, 0), fontname='publicpixel', fontsize=30)
    screen.draw.text('BOT', (125, 250), color=(0, 0, 0), fontname='publicpixel', fontsize=30)
    screen.draw.text('HUMAN', (600, 250), color=(0, 0, 0), fontname='publicpixel', fontsize=30)
    screen.draw.text('A', (190, 450), color=(0, 0, 0), fontname='publicpixel', fontsize=30)
    screen.draw.text('S', (390, 450), color=(0, 0, 0), fontname='publicpixel', fontsize=30)
    screen.draw.text('D', (590, 450), color=(0, 0, 0), fontname='publicpixel', fontsize=30)
    if nguoi != 0:
        if may == 1:
            screen.blit('keo', (100, 300))
        elif may == 2:
            screen.blit('bua', (100, 300))
        elif may == 3:
            screen.blit('bao', (100, 300))
    screen.draw.text('NHAN ENTER DE CHOI LAI', (15, 10), color=(255,255 , 0), fontname='publicpixel', fontsize=15)
    # draw the image of player's choice on the right
    if nguoi == 1:
        screen.blit('keo', (600, 300))
    elif nguoi == 2:
        screen.blit('bua', (600, 300))
    elif nguoi == 3:
        screen.blit('bao', (600, 300))
def reset_game():
    global may, nguoi, outcome, sounds_play
    may = random.randint(1, 3)
    nguoi = 0
    outcome = ""
    sounds_play = False
#############################################

