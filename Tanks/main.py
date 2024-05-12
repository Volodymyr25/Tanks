import pygame
import os
import random
from modules.classes import *
from modules.mapsetting import map

FPS = pygame.time.Clock()

pygame.init()

sound = pygame.mixer.music.load('sounds/back_music.wav')
sound = pygame.mixer.music.play()
sound = pygame.mixer.music.set_volume(0.1)


background = pygame.image.load(os.path.join(path, 'images/background.png'))
background = pygame.transform.scale(background, (width, width))

font = pygame.font.Font(None, 120)
winner1_text = font.render('blue win', True, (0,0,255))
winner2_text = font.render('red win', True, (255,0,0))


x = 0
y = 0
blocks_list = []

wall_image1 = os.path.join(path, 'images/wall.png')
wall_image2 = os.path.join(path, 'images/wall1.png')


for row in map:
    for i in row:
        if i == 1:
            blocks_list.append(Block(x, y, 1, wall_image1))
        elif i == 2:
            blocks_list.append(Block(x, y, 2, wall_image2))
        x += step
    y += step
    x = 0


player1  =  Player(1,1)
player2 = Player2(1,3)
clock = pygame.time.Clock()

is_game_running = True

winner = None
while is_game_running:
    window.blit(background, (0,0))
    for block in blocks_list:
        block.blit()
        if block.colliderect(player1.bullet):
            player1.bullet.stop()
            if block.type_block == 1:
                map[block.y // step][block.x // step] = 0

                block.x = 1000000
        if block.colliderect(player2.bullet):
            player2.bullet.stop()
            if block.type_block == 1:
                map[block.y // step][block.x // step] = 0

                block.x = 1000000
    player1.bullet.move()
    player2.bullet.move()
    player1.blit()
    player2.blit()
    if player1.colliderect(player2.bullet):
        winner = 2
        is_game_running = False
        is_winner = True
    elif player2.colliderect(player1.bullet):
        winner = 1
        is_game_running = False
        is_winner = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
    clock.tick(10)
    pygame.display.flip()

cors = (width // 2 - winner1_text.get_width() // 2, 
        width // 2 - winner1_text.get_height()// 2)
while is_winner:
    window.blit(background, (0,0))
    if winner == 1:
        window.blit(winner1_text, cors)
    elif winner == 2:
        window.blit(winner2_text, cors)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_winner = False
    pygame.display.flip()