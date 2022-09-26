import pgzrun
import random

WIDTH =  1700
HEIGHT =  950
PANZER_STEP = 2
SHOT_STEP = 2 * PANZER_STEP

panzerDesert = Actor('tanks_tank_desert1_r')
panzerDesert.topleft = 0, 10

shotDesert = Actor('tank_bullet5_l')
shotDesert.topright = 0, 10

panzerGreen = Actor('tanks_tank_green1_l')
panzerGreen.bottomright = WIDTH, HEIGHT

boxWooden = Actor('tanks_crate_wood')
boxWooden.topleft = random.randint(0, WIDTH), random.randint(0, HEIGHT)

def draw():
    screen.clear()
    panzerDesert.draw()
    shotDesert.draw()
    boxWooden.draw()
#    panzerGreen.draw()


def handleShot():
    if keyboard.SPACE:

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
    if shotDesert.image == 'tank_bullet5_l':
        shotDesert.left = shotDesert.left - SHOT_STEP
    if shotDesert.image == 'tank_bullet5_u':
        shotDesert.top = shotDesert.top - SHOT_STEP
    if shotDesert.image == 'tank_bullet5_d':
        shotDesert.top = shotDesert.top + SHOT_STEP

def handlePazer():
    if keyboard.left:
        panzerDesert.image = 'tanks_tank_desert1_l'
    elif keyboard.right:
        panzerDesert.image = 'tanks_tank_desert1_r'
    elif keyboard.up:
        panzerDesert.image = 'tanks_tank_desert1_u'
    elif keyboard.down:
        panzerDesert.image = 'tanks_tank_desert1_d'


    if panzerDesert.image == 'tanks_tank_desert1_r':
        panzerDesert.left = panzerDesert.left + PANZER_STEP
        if panzerDesert.right > WIDTH:
            panzerDesert.image = 'tanks_tank_desert1_l'

    elif panzerDesert.image == 'tanks_tank_desert1_l':
        panzerDesert.left = panzerDesert.left - PANZER_STEP
        if panzerDesert.left < 0:
            panzerDesert.image = 'tanks_tank_desert1_r'

    elif panzerDesert.image == 'tanks_tank_desert1_u':
        panzerDesert.top = panzerDesert.top - PANZER_STEP
        if panzerDesert.top < 0:
            panzerDesert.image = 'tanks_tank_desert1_d'

    elif panzerDesert.image == 'tanks_tank_desert1_d':
        panzerDesert.bottom = panzerDesert.bottom + PANZER_STEP
        if panzerDesert.bottom > HEIGHT:
            panzerDesert.image = 'tanks_tank_desert1_u'

    if panzerDesert.colliderect(boxWooden):
        if panzerDesert.image == 'tanks_tank_desert1_r':
            panzerDesert.image = 'tanks_tank_desert1_l'
        elif panzerDesert.image == 'tanks_tank_desert1_l':
            panzerDesert.image = 'tanks_tank_desert1_r'
        elif panzerDesert.image == 'tanks_tank_desert1_u':
            panzerDesert.image = 'tanks_tank_desert1_d'
        elif panzerDesert.image == 'tanks_tank_desert1_d':
            panzerDesert.image = 'tanks_tank_desert1_u'



def update():

    handleShot()
    handlePazer()


#    panzerGreen.left -= 2
#    if panzerGreen.left < 0:
#        panzerGreen.right = 0

pgzrun.go()
