import pygame
import os

pygame.init()
clock = pygame.time.Clock()

pers = pygame.Rect(55, 55, 40, 30)
banana = pygame.Rect(105, 305, 40, 35)
screen1 = pygame.display.set_mode((500,500))

go_right = False
go_left = False
go_up = False 
go_down = False

#---------------------------------------------------
# vozduch = 1
# stenka = 0

papka = os.path.dirname(__file__)
put = os.path.abspath(papka + "/textures")
stenka = pygame.image.load(put + "/stenka.jpg")
pers_img = pygame.image.load(put + "/pers.png")
banana_img = pygame.image.load(put + "/banana.png")

textures = [
    [1,1,1,1,1,1,1,1,1,1], 
    [1,1,1,1,1,0,0,0,0,1], 
    [1,0,1,0,0,0,0,0,0,1], 
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1], 
    [1,0,0,0,0,0,0,0,0,1], 
    [1,0,1,0,0,0,0,0,0,1], 
    [1,1,1,1,1,1,1,1,1,1], 
    [1,0,1,0,0,0,0,0,0,1], 
    [1,1,1,1,1,1,1,1,1,1]  
]

rects = []
rects_textures = []

bad_rects = []

x = 0
y = 0

for texture in textures:
    for i in texture:
        kvadrat = pygame.Rect(x,y, 50, 50)
        rects.append(kvadrat)
        rects_textures.append(i)
        if i == 0:
            bad_rects.append(kvadrat)
        x += 50
    y += 50
    x = 0

game = True

while game:

    screen1.fill((255,0,0))

    for i in range(100):
        if rects_textures[i] == 0:
            screen1.blit(stenka, rects[i])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                go_right = True
            if event.key == pygame.K_a:
                go_left = True
            if event.key == pygame.K_w:
                go_up = True 
            if event.key == pygame.K_s:
                go_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                go_right = False
            if event.key == pygame.K_a:
                go_left = False
            if event.key == pygame.K_w:
                go_up = False
            if event.key == pygame.K_s:
                go_down = False

    screen1.blit(pers_img, pers)
    screen1.blit(banana_img, banana)

    for kvadrat in bad_rects:
        if pers.colliderect(kvadrat):
            pers.x = 55
            pers.y = 55

    if pers.colliderect(banana):
        print("Победа")
        break

    if go_right == True:
        pers.x += 5
    if go_left == True:
        pers.x -= 5
    if go_up == True:
        pers.y -= 5
    if go_down == True:
        pers.y += 5
        
    pygame.display.flip()
    clock.tick(60)