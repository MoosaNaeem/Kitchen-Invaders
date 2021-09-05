import sys,pygame
import random
pygame.init()

size = width, height = 1300, 1000

screen = pygame.display.set_mode(size)
black = 0,0,0


def createProjectile(imagePath, initialX, initialY):
    print("Created Projectile")
    projectile = pygame.image.load(imagePath)
    projectileControl = projectile.get_rect()
    projectileControl.move_ip(initialX, initialY)




burgerSpeed = [0,0]
burger = pygame.image.load("./assets/burger.png").convert()
burgerControl = burger.get_rect()
burgerControl.move_ip(400,800)


powderSpeed = [0,0]
powder = pygame.image.load("./assets/powder.png").convert()
powderControl = powder.get_rect()
powderControl.move_ip(400,0)

randomCounter = random.randint(0,200)
counter = 0

sesameSeeds = []
seedboxes = []
sesamePicture = pygame.image.load("./assets/sesameseed.png").convert()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            burgerSpeed[0] = 2
            
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            burgerSpeed[0] = -2

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            #createProjectile("./assets/sesameseed.png", burgerPositionX, burgerControl.y)

            # sesameSeeds.append([burgerControl.x,burgerControl.y])
            seedbox = sesamePicture.get_rect()
            seedbox.move_ip(burgerControl.x, burgerControl.y)
            seedboxes.append(seedbox)
        pygame.time.Clock().tick(60)

    burgerControl = burgerControl.move(burgerSpeed)
    powderControl = powderControl.move(powderSpeed)
    
    
    for seed in seedboxes:
       seed.y += -5

    # Iterate over a slice copy if you want to mutate a list.
    # for sesame in seedboxes[:]:
    #     if sesame[0] < 0:
    #         seedboxes.remove(sesame)
            
    #if burger collision then stop
    if burgerControl.left < 0 or burgerControl.right > width:
        burgerSpeed[0] = 0
    #if powder collision then stop
    if powderControl.left < 0 or powderControl.right > width:
        powderSpeed[0] = 0



    #POWDER AI v1
    # if counter >= randomCounter:
    #     powderSpeed[0] *= -1
    #     counter = 0
    #     randomCounter = random.randint(0,200)
    # else:
    #     counter += 1

    #POWDER AI v2


    burgerPositionX = burgerControl.x
    powderPositionX = powderControl.x

    if powderPositionX > burgerPositionX and counter >= randomCounter:
        powderSpeed[0] = -1
        counter = 0
        randomCounter = random.randint(0,200)
    elif powderPositionX <= burgerPositionX and counter >= randomCounter:
        powderSpeed[0] = 1
        counter = 0
        randomCounter = random.randint(0,200)
    else:
        counter += 1

    screen.fill(black)
    screen.blit(burger, burgerControl)
    screen.blit(powder, powderControl)
    for sesame in seedboxes:
        screen.blit(sesamePicture, sesame)
    pygame.display.flip()