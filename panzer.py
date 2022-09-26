import pgzrun
import random

WIDTH = 1700
HEIGHT = 950
PANZER_STEP = 2
SHOT_STEP = 2 * PANZER_STEP

panzerDesert = Actor('tanks_tank_desert1_r')
panzerDesert.topleft = 0, 10

shotDesert = Actor('tank_bullet5_l')
shotDesert.topright = 0, 10

panzerGreen = Actor('tanks_tank_green1_l')
panzerGreen.bottomright = WIDTH, HEIGHT

boxWooden = Actor('tanks_crate_wood')
boxWooden.images = ['tanks_crate_wood', 'tank_explosion2','tank_explosion3','tank_explosion4']
boxWooden.fps = 1
boxWooden.topleft = random.randint(0, WIDTH), random.randint(0, HEIGHT)

def draw():
    screen.clear()
    panzerDesert.draw()
    shotDesert.draw()
    boxWooden.draw()
    panzerGreen.draw()


def handleShot():
    if keyboard.space:

        if panzerDesert.image == 'tanks_tank_desert1_l':
            shotDesert.image = 'tank_bullet5_l'
            shotDesert.topright = panzerDesert.topleft
        elif panzerDesert.image == 'tanks_tank_desert1_r':
            shotDesert.image = 'tank_bullet5_r'
            shotDesert.topleft = panzerDesert.topright
        elif panzerDesert.image == 'tanks_tank_desert1_u':
            shotDesert.image = 'tank_bullet5_u'
            shotDesert.bottomleft = panzerDesert.topleft
        elif panzerDesert.image == 'tanks_tank_desert1_d':
            shotDesert.image = 'tank_bullet5_d'
            shotDesert.topright = panzerDesert.bottomright

    if shotDesert.image == 'tank_bullet5_r':
        shotDesert.left = shotDesert.left + SHOT_STEP
    elif shotDesert.image == 'tank_bullet5_l':
        shotDesert.left = shotDesert.left - SHOT_STEP
    elif shotDesert.image == 'tank_bullet5_u':
        shotDesert.top = shotDesert.top - SHOT_STEP
    elif shotDesert.image == 'tank_bullet5_d':
        shotDesert.top = shotDesert.top + SHOT_STEP

    if shotDesert.colliderect(boxWooden):
#        boxWooden.animate()
        boxWooden.image = 'tank_explosion4'
        #shotDesert.left = WIDTH
        shotDesert.bottomleft = WIDTH + 100, HEIGHT + 100

    elif boxWooden.image == 'tank_explosion4':
        boxWooden.left = WIDTH

def handlePazer(panzer, key_left, key_right, key_up, key_down, image_left, image_right, image_up, image_down):
    if key_left:
        panzer.image = image_left
    elif key_right:
        panzer.image = image_right
    elif key_up:
        panzer.image = image_up
    elif key_down:
        panzer.image = image_down


    if panzerDesert.image == image_right:
        panzer.left = panzer.left + PANZER_STEP
        if panzer.right > WIDTH:
            panzer.image = image_left

    elif panzer.image == image_left:
        panzer.left = panzer.left - PANZER_STEP
        if panzer.left < 0:
            panzer.image = image_right

    elif panzer.image == image_up:
        panzer.top = panzer.top - PANZER_STEP
        if panzer.top < 0:
            panzer.image = image_down

    elif panzer.image == image_down:
        panzer.bottom = panzer.bottom + PANZER_STEP
        if panzer.bottom > HEIGHT:
            panzer.image = image_up

    if panzer.colliderect(boxWooden):
        if panzer.image == image_right:
            panzer.image = image_left
        elif panzer.image == image_left:
            panzer.image = image_right
        elif panzer.image == image_up:
            panzer.image = image_down
        elif panzer.image == image_down:
            panzer.image = image_up



def update():

    handleShot()
    handlePazer(panzerDesert, keyboard.left, keyboard.right, keyboard.up, keyboard.down, 'tanks_tank_desert1_l', 'tanks_tank_desert1_r', 'tanks_tank_desert1_u', 'tanks_tank_desert1_d')
    handlePazer(panzerGreen, keyboard.a, keyboard.d, keyboard.w, keyboard.s, 'tanks_tank_green1_l', 'tanks_tank_green1_r', 'tanks_tank_green1_u', 'tanks_tank_green1_d')

pgzrun.go()
