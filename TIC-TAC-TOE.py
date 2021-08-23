import pygame
from pygame import mixer
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("bensound-littleidea(1).wav")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)
values = [[38, 124, 38, 124, 45, 45, 0, 0], [133, 230, 38, 125, 138, 45, 0, 1], [227, 313, 38, 124, 232, 45, 0, 2],
          [38, 124, 133, 216, 45, 140, 1, 0], [133, 230, 133, 216, 140, 140, 1, 1],
          [227, 313, 133, 261, 233, 140, 1, 2], [38, 124, 227, 311, 45, 230, 2, 0],
          [133, 230, 227, 311, 140, 230, 2, 1], [227, 313, 227, 311, 233, 230, 2, 2]]

screen = pygame.display.set_mode((500, 350))
pygame.display.set_caption("TIC-TAC-TOE")
icon = pygame.image.load("tic-tac-toe.png")
pygame.display.set_icon(icon)
icon2 = pygame.image.load("Hi1.png")
icon1 = pygame.image.load('Hi.png')
icon3 = pygame.image.load("Hi2.png")
p1 = 45
p2 = 45
fond = pygame.font.Font('Chocolate Cookies.ttf', 32)


def show_name():
    if kkk % 2 == 0:
        score = fond.render("Player 1", True, (255, 255, 255))
    else:
        score = fond.render("Player 2", True, (255, 255, 255))
    score1 = fond.render("turn", True, (209, 237, 242))
    if conditions() != 0:
        screen.blit(score, (375, 125))
        screen.blit(score1, (375, 180))


def final(a):
    score2 = fond.render("Player 1 Won", True, (0, 0, 255))
    score3 = fond.render("Player 2 Won", True, (0, 0, 255))
    score4 = fond.render("Game tie", True, (0, 0, 255))
    if a == 1:
        screen.blit(score2, (150, 100))
    if a == 0:
        screen.blit(score3, (150, 100))
    if a == 2:
        screen.blit(score4, (150, 100))


def honey():
    screen.blit(icon1, (25, 25))


def ran(a, b):
    screen.blit(icon2, (a, b))


def run(c, d):
    screen.blit(icon3, (c, d))


def conditions():
    test = 0
    for i in range(len(a)):
        if a[i][0] == a[i][1] == a[i][2] != " ":
            if a[i][0] == 1:
                final(1)
                return 0
            else:
                final(0)
                return 0

        if a[0][i] == a[1][i] == a[2][i] != " ":
            if a[0][i] == 1:
                final(1)
                return 0
            else:
                final(0)
                return 0
    if a[0][0] == a[1][1] == a[2][2] != " ":
        if a[0][0] == 1:
            final(1)
            return 0
        else:
            final(0)
            return 0
    if a[0][2] == a[1][1] == a[2][0] != " ":
        if a[0][2] == 1:
            final(1)
            return 0
        else:
            final(0)
            return 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != " ":
                test = test + 1
    if test == 9:
        final(2)
        return 0
    return 1


brak = 1
a = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
kkk = 0
iii = []

while brak:
    screen.fill((196, 164, 132))
    if conditions() != 0:
        honey()
    if conditions()==0:
        m=0
        try:
            if m==0:
                sounds = pygame.mixer.Sound("JKL83NH-video-game-win.wav")
                sounds.play(0)
                break
        except:
            pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            brak = 0
        if event.type == pygame.MOUSEBUTTONUP:
            mousex, mousey = pygame.mouse.get_pos()
            n = 0
            for i in range(len(values)):
                if ((values[i][0] <= mousex <= values[i][1]) and (values[i][2] <= mousey <= values[i][3])):
                    n = n + 1
                    try:
                        sounds=pygame.mixer.Sound("chime.wav")
                        sounds.play()
                    except:
                        pass
                    iii.append(values[i][4])
                    iii.append(values[i][5])
                    kkk = kkk + 1
                    if kkk % 2 != 0:
                        a[values[i][6]][values[i][7]] = 1
                    else:
                        a[values[i][6]][values[i][7]] = 0
                    values.pop(i)
                    break
                if i+1==len(values) and n==0:
                    sounds = pygame.mixer.Sound("blip (1).wav")
                    sounds.play()

    if conditions() != 0:
        try:
            if 1 <= kkk:
                run(iii[0], iii[1])
            if 2 <= kkk:
                ran(iii[2], iii[3])
            if 3 <= kkk:
                run(iii[4], iii[5])
            if 4 <= kkk:
                ran(iii[6], iii[7])
            if 5 <= kkk:
                run(iii[8], iii[9])
            if 6 <= kkk:
                ran(iii[10], iii[11])
            if 7 <= kkk:
                run(iii[12], iii[13])
            if 8 <= kkk:
                ran(iii[14], iii[15])
            if 9 <= kkk:
                run(iii[16], iii[17])
        except:
            pass
    show_name()
    pygame.display.update()
