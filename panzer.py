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
bullets = []
bullet_holdoff = []
bullet_holdoff.append(100)
bullet_holdoff.append(100)

tankGreen = Actor('tank_green')
tankGreen.bottomright = WIDTH, HEIGHT

enemy = Actor('tank_huge')
enemy.y = 25
enemy.x = 400
enemy.move_count = 0


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

#    if :
#        screen.draw.text(' Won!', (260,250), color=(255,255,255), fontsize=100)
#    else:
    for wall in walls:
        wall.draw()

    tankBlue.draw()
    tankGreen.draw()
    enemy.draw()

    for bullet in bullets:
        bullet.draw()

def handleShot(tank, key_shot, bullet_image, index):
    if bullet_holdoff[index] == 0:
        if key_shot:
            bullet = Actor(bullet_image)
            if tank.angle + 180 >= 360:
                bullet.angle = (tank.angle + 180) - 360
            else:
                bullet.angle = (tank.angle + 180)

            bullet.x = tank.x
            bullet.y = tank.y
            bullets.append(bullet)
            bullet_holdoff[index]=100
    else:
        bullet_holdoff[index] -= 1

    for bullet in bullets:
        if bullet.angle == 270:
            bullet.x = bullet.x + 5
        elif bullet.angle == 90:
            bullet.x = bullet.x - 5
        elif bullet.angle == 0:
            bullet.y = bullet.y - 5
        elif bullet.angle == 180:
            bullet.y = bullet.y + 5

    for bullet in bullets:
        wall_index = bullet.collidelist(walls)
        if wall_index != -1:
            del walls[wall_index]
            bullets.remove(bullet)
        if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
            bullets.remove(bullet)

    index = tank.collidelist(bullets)
    if index != -1 and bullets[index].image != bullet_image:
        tank.topleft = 0, 10
        bullets.remove(bullets[index])


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

def handleEnemy():
    choice = random.randint(0, 10)
    if enemy.move_count > 0:
        enemy.move_count = enemy.move_count - 1

        original_x = enemy.x
        original_y = enemy.y
        if enemy.angle == 0:
            enemy.y = enemy.y + 2
        elif enemy.angle == 90:
            enemy.x = enemy.x + 2
        elif enemy.angle == 180:
            enemy.y = enemy.y - 2
        elif enemy.angle == 270:
            enemy.x = enemy.x - 2

        if enemy.collidelist(walls) != -1:
            enemy.x = original_x
            enemy.y = original_y
            enemy.move_count = 0

        if enemy.x < 0 or enemy.x > 800 or enemy.y < 0 or enemy.y > 600:
            enemy.x = original_x
            enemy.y = original_y
            enemy.move_count = 0

    elif choice == 0:
        print('shoot')
    elif choice == 1:
        enemy.angle = random.randint(0, 3) * 90
    else:
        enemy.move_count = 20

def update():

    handleShot(tankBlue, keyboard.space, 'bullet-blue3_outline', 0)
    handlePazer(tankBlue, keyboard.left, keyboard.right, keyboard.up, keyboard.down, 'tank_blue')

    handleShot(tankGreen, keyboard.q,  'bullet-green3_outline', 1)
    handlePazer(tankGreen, keyboard.a, keyboard.d, keyboard.w, keyboard.s, 'tank_green')

    handleEnemy()

pgzrun.go()
