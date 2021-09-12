import sys,pygame
import random
pygame.init()

size = width, height = 1300, 1000
screen = pygame.display.set_mode(size)
black = 0,0,0


#burger variables
burgerSpeed = [0,0]
burger = pygame.image.load("./assets/burger.png").convert()
burgerControl = burger.get_rect()
burgerControl.move_ip(400,800)
sesameSeeds = []
seedboxes = []
sesamePicture = pygame.image.load("./assets/sesameseed.png").convert()

fireSpeed = 8
fireRate = 10

#powder variables
powderSpeed = [0,0]
powder = pygame.image.load("./assets/powder.png").convert()
powderControl = powder.get_rect()
powderControl.move_ip(400,0)
powderDrops = []
powderBoxes = []
powderdropPicture = pygame.image.load("./assets/powderDrops.png").convert()
powderHealth = 100
powderHealthBarPicture = pygame.image.load("./assets/PowderHealthBar.png").convert()
powderHealthRect = powderHealthBarPicture.get_rect()
# powderHealthRect.move_ip(50,50)
powderDropSpeed = 2
powderDropRate = 50


#game variables
randomCounter = random.randint(0,200)
counter = 0
fixedCounter = 0
fixedCounter2 = 0


#main game loop
while 1:
    #event listening
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            burgerSpeed[0] = 2
            
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            burgerSpeed[0] = -2

        if pygame.key.get_pressed()[pygame.K_SPACE] and fixedCounter >= fireRate:
            fixedCounter = 0
            #creating a new sesameseed instance
            seedbox = sesamePicture.get_rect()
            seedbox.move_ip(burgerControl.x, burgerControl.y)
            seedboxes.append(seedbox)
    
    pygame.time.Clock().tick(60)

    burgerControl = burgerControl.move(burgerSpeed)
    powderControl = powderControl.move(powderSpeed)
    
    for seed in seedboxes:
       seed.y += -fireSpeed
       if(seed.x >= powderControl.left and seed.x <= powderControl.right and seed.y <= powderControl.bottom and seed.y >= powderControl.top):
           print("powder got hit")
           seedboxes.remove(seed)
           powderHealth -= 5
           powderHealthRect.inflate_ip(100, 100)

    #if burger collision then stop
    if burgerControl.left < 0 or burgerControl.right > width:
        burgerSpeed[0] = 0
    #if powder collision then stop
    if powderControl.left < 0 or powderControl.right > width:
        powderSpeed[0] = 0

    #POWDER AI v2
    powderHealthRect = powderHealthBarPicture.get_rect()
    powderHealthRect.move_ip(powderControl.x, powderControl.y)
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
    elif abs(powderPositionX - burgerPositionX) <= 50 and fixedCounter2 > powderDropRate:
        powderBox = powderdropPicture.get_rect()
        fixedCounter2 = 0
        powderBox.move_ip(powderControl.x, powderControl.y)
        
        powderBoxes.append(powderBox)
    else:
        counter += 1

    for pow in powderBoxes:
           pow.y += powderDropSpeed
           if(pow.x >= burgerControl.left and pow.x <= burgerControl.right and pow.y <= burgerControl.bottom and pow.y >= burgerControl.top):
               print("burger got hit")
               powderBoxes.remove(pow)


    fixedCounter2 += 1

    fixedCounter += 1
    screen.fill(black)
    screen.blit(burger, burgerControl)
    screen.blit(powder, powderControl)
    screen.blit(powderHealthBarPicture, powderHealthRect)
    for pow in powderBoxes:
        screen.blit(powderdropPicture, pow)
    for sesame in seedboxes:
        screen.blit(sesamePicture, sesame)
    pygame.display.flip()