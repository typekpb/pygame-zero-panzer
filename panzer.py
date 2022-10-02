import pgzrun
import random

WIDTH = 800 #1700
HEIGHT = 600 #950
PANZER_STEP = 2
SHOT_STEP = 2 * PANZER_STEP

tankBlue = Actor('tank_blue')
tankBlue.topleft = 0, 10

grass = []
walls = []

shots = []
shotDesert = Actor('tank_bullet5_l')
shotDesert.topright = 0, 10
shots.append(shotDesert)

tankGreen = Actor('tank_green')
tankGreen.bottomright = WIDTH, HEIGHT

def generateGrass():
    for x in range(int(WIDTH/64) + 2):
        for y in range(int(HEIGHT/64) + 2):
            grass1 = Actor('tile_grass1')
            grass1.x = 64 * x
            grass1.y = 64 * y
            grass.append(grass1)


def generateWalls():
    for x in range(int(WIDTH/28) + 1):
        for y in range(int(HEIGHT/28) + 1):
            if random.randint(0, 100) < 10 and y > 2 and y < HEIGHT/28 - 3:
                wall = Actor('crate_metal')
                wall.topleft = (28 * x, 28 * y)
                walls.append(wall)

generateGrass()
generateWalls()

def draw():
    screen.clear()
    #screen.fill((0,0,0))
    #background.draw()


    for grass1 in grass:
        grass1.draw()
    for wall in walls:
        wall.draw()

    tankBlue.draw()
    shotDesert.draw()
    tankGreen.draw()

def handleShot():
    if keyboard.space:

        if tankBlue.image == 'tanks_tank_desert1_l':
            shotDesert.image = 'tank_bullet5_l'
            shotDesert.topright = tankBlue.topleft
        elif tankBlue.image == 'tanks_tank_desert1_r':
            shotDesert.image = 'tank_bullet5_r'
            shotDesert.topleft = tankBlue.topright
        elif tankBlue.image == 'tanks_tank_desert1_u':
            shotDesert.image = 'tank_bullet5_u'
            shotDesert.bottomleft = tankBlue.topleft
        elif tankBlue.image == 'tanks_tank_desert1_d':
            shotDesert.image = 'tank_bullet5_d'
            shotDesert.topright = tankBlue.bottomright

    if shotDesert.image == 'tank_bullet5_r':
        shotDesert.left = shotDesert.left + SHOT_STEP
    elif shotDesert.image == 'tank_bullet5_l':
        shotDesert.left = shotDesert.left - SHOT_STEP
    elif shotDesert.image == 'tank_bullet5_u':
        shotDesert.top = shotDesert.top - SHOT_STEP
    elif shotDesert.image == 'tank_bullet5_d':
        shotDesert.top = shotDesert.top + SHOT_STEP

def handlePazer(tank, key_left, key_right, key_up, key_down, image):

    # Save the original position of the tank
    original_x = tank.x
    original_y = tank.y

    if key_left:
        tank.x = tank.x - 2
        tank.angle = 270
    elif key_right:
        tank.x = tank.x + 2
        tank.angle = 90
    elif key_up:
        tank.y = tank.y - 2
        tank.angle = 180
    elif key_down:
        tank.y = tank.y + 2
        tank.angle = 0

    # Return tank to original position if colliding with wall
    if tank.collidelist(walls) != -1:
        tank.x = original_x
        tank.y = original_y

    if tank.x < 0 or tank.x > WIDTH or tank.y < 0 or tank.y > HEIGHT:
        tank.x = original_x
        tank.y = original_y



def update():

    handleShot()
    handlePazer(tankBlue, keyboard.left, keyboard.right, keyboard.up, keyboard.down, 'tank_blue')
    handlePazer(tankGreen, keyboard.a, keyboard.d, keyboard.w, keyboard.s, 'tank_green')

pgzrun.go()
