# pip install pygame

import pygame
from pygame.locals import *
import math
from random import randint

move_speed = 2

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

running = True
playerpos = [100, 100]

score = 0
arrows = []

enemy_timer = 100  # waktu kemunculan
enemies = [[width, 100]]  # list yang menampung koordinat musuh

health_point = 194  # default health point for castle
countdown_timer = 90000  # 90 detik

exitcode = 0
EXIT_CODE_GAME_OVER = 0
EXIT_CODE_WIN = 1

player = pygame.image.load('resources/images/dude.png')
player1 = pygame.image.load('resources/images/dude2.png')
grass = pygame.image.load('resources/images/grass.png')
castle = pygame.image.load('resources/images/castle.png')
arrow = pygame.image.load('resources/images/bullet.png')
enemy_img = pygame.image.load('resources/images/badguy.png')
enemy_img1 = pygame.image.load('resources/images/badguy2.png')
enemy_img2 = pygame.image.load('resources/images/badguy3.png')
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")

# 3.1 - Load audio
pygame.mixer.init()
hit_sound = pygame.mixer.Sound("resources/audio/explode.wav")
enemy_hit_sound = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot_sound = pygame.mixer.Sound("resources/audio/shoot.wav")
hit_sound.set_volume(0.05)
enemy_hit_sound.set_volume(0.05)
shoot_sound.set_volume(0.05)

# background music
pygame.mixer.music.load("resources/audio/moonlight.wav")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

keys = {
    "top": False,
    "bottom": False,
    "left": False,
    "right": False
}

while(running):
    screen.fill(0)

    for x in range(int(width/grass.get_width()+1)):
        for y in range(int(height/grass.get_height()+1)):
            screen.blit(grass, (x*100, y*100))

    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    # screen.blit(player, playerpos)
    mouse_position = pygame.mouse.get_pos()
    angle = math.atan2(
        mouse_position[1] - (playerpos[1]+32), mouse_position[0] - (playerpos[0]+26))
    player_rotation = pygame.transform.rotate(player, 360 - angle * 57.29)
    new_playerpos = (playerpos[0] - player_rotation.get_rect().width / 2,
                     playerpos[1] - player_rotation.get_rect().height / 2)
    screen.blit(player_rotation, new_playerpos)

    for bullet in arrows:
        arrow_index = 0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0])*10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > width or bullet[2] < -64 or bullet[2] > height:
            arrows.pop(arrow_index)
        arrow_index += 1
        # draw the arrow
        for projectile in arrows:
            new_arrow = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(new_arrow, (projectile[1], projectile[2]))

    enemy_timer -= 1
    if enemy_timer == 0:
        # buat musuh baru
        enemies.append([width, randint(50, height-32)])
        # reset enemy timer to random time
        enemy_timer = randint(1, 100)

    index = 0
    for enemy in enemies:
        # musuh bergerak dengan kecepatan 5 pixel ke kiri
        enemy[0] -= 2
        # hapus musuh saat mencapai batas layar sebelah kiri
        if enemy[0] < -64:
            enemies.pop(index)

        # 6.2.1 collision between enemies and castle
        enemy_rect = pygame.Rect(enemy_img.get_rect())
        enemy_rect.top = enemy[1]  # ambil titik y
        enemy_rect.left = enemy[0]  # ambil titik x
        # benturan musuh dengan markas kelinci
        if enemy_rect.left < 64:
            enemies.pop(index)
            health_point -= randint(5, 20)
            hit_sound.play()
            print("Oh tidak, kita diserang!!")

        # 6.2.2 Check for collisions between enemies and arrows
        index_arrow = 0
        for bullet in arrows:
            bullet_rect = pygame.Rect(arrow.get_rect())
            bullet_rect.left = bullet[1]
            bullet_rect.top = bullet[2]
            # benturan anak panah dengan musuh
            if enemy_rect.colliderect(bullet_rect):
                score += 1
                enemies.pop(index)
                arrows.pop(index_arrow)
                hit_sound.play()
                print("Boom! mati kau!")
                print("Score: {}".format(score))
            index_arrow += 1
        index += 1

    # gambar musuh ke layar
    for enemy in enemies:
        rr = randint(1, 3)
        if rr == 1:
            screen.blit(enemy_img, enemy)
        elif rr == 2:
            screen.blit(enemy_img1, enemy)
        else:
            screen.blit(enemy_img2, enemy)
        # print('TOTAL MUSUK ', len(enemies))
        # loop += 1
        # if loop % 2 == 0:
        #     screen.blit(enemy_img1, enemy)
        # else:
        #     screen.blit(enemy_img, enemy)

    screen.blit(healthbar, (5, 5))
    for hp in range(health_point):
        screen.blit(health, (hp+8, 8))

    # 6.4 - Draw clock
    font = pygame.font.Font(None, 24)
    minutes = int((countdown_timer-pygame.time.get_ticks()) /
                  60000)  # 60000 itu sama dengan 60 detik
    seconds = int((countdown_timer-pygame.time.get_ticks())/1000 % 60)
    time_text = "{:02}:{:02}".format(minutes, seconds)
    clock = font.render(time_text, True, (255, 255, 255))
    textRect = clock.get_rect()
    textRect.topright = [635, 5]
    screen.blit(clock, textRect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys["top"] = True
            elif event.key == K_a:
                keys["left"] = True
            elif event.key == K_s:
                keys["bottom"] = True
            elif event.key == K_d:
                keys["right"] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys["top"] = False
            elif event.key == K_a:
                keys["left"] = False
            elif event.key == K_s:
                keys["bottom"] = False
            elif event.key == K_d:
                keys["right"] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            arrows.append([angle, new_playerpos[0]+32, new_playerpos[1]+32])

    if keys["top"]:
        playerpos[1] -= move_speed  # kurangi nilai y
    elif keys["bottom"]:
        playerpos[1] += move_speed  # tambah nilai y
    if keys["left"]:
        playerpos[0] -= move_speed  # kurangi nilai x
    elif keys["right"]:
        playerpos[0] += move_speed  # tambah nilai x

    if pygame.time.get_ticks() > countdown_timer:
        running = False
        exitcode = EXIT_CODE_WIN
    if health_point <= 0:
        running = False
        exitcode = EXIT_CODE_GAME_OVER

if exitcode == EXIT_CODE_GAME_OVER:
    screen.blit(gameover, (0, 0))
else:
    screen.blit(youwin, (0, 0))

# Tampilkan score
text = font.render("Score: {}".format(score), True, (255, 255, 255))
textRect = text.get_rect()
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery + 24
screen.blit(text, textRect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()