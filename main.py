# snake game in python

import pygame, sys, time, random

# check for initialising error
check_error = pygame.init()
if check_error[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_error[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized")
clock = pygame.time.Clock()
# Play Surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snako')
#time.sleep(5)

# Colors
red = pygame.Color(255,0,0)#gameOver
green = pygame.Color(0,255,0)#Snake
black = pygame.Color(0,0,0)#Score
white = pygame.Color(255,255,255)#background
brown = pygame.Color(162,42,42)#food
gray = pygame.Color(190,190,190)#button
# FPS Controller
fpsController = pygame.time.Clock()

# Important Variables


score = 0
def text_objects(text ,font,color):
    textSurf = font.render(text,True,color)
    return textSurf,textSurf.get_rect()

def button(x,y,w,h,ac,ic,msg,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(playSurface,ac,(x,y,w,h))
        if click[0] ==1 and action != None:
            action()
    else:
        pygame.draw.rect(playSurface,ic,(x,y,w,h))

    smallText = pygame.font.SysFont('comicsansms',30)
    TextSurf,TextRect = text_objects(msg,smallText,black)
    TextRect.center =((x+(w/2)),(y+(h/2)))
    playSurface.blit(TextSurf,TextRect)
def quitgame():
    pygame.quit()
    quit()
#Game Over Function
def gameOver():
    #gameover = True
    myFont = pygame.font.SysFont('comicsansms', 92)
    GOsurf = myFont.render('Game Over!', True, black)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360,15)
    playSurface.blit(GOsurf, GOrect)
    #showScore(0)
    button(230,400,140,40,white,gray,"RESTART",game_loop)
    button(400,400,100,40,white,gray,"QUIT",quitgame)    
    pygame.display.flip()
    clock.tick(15)
# score function
def showScore(choice=1):
    sFont = pygame.font.SysFont('comicsansms', 30)
    Ssurf = sFont.render('Score : {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (100, 10)
    else:
        Srect.midtop = (360, 150)

    playSurface.blit(Ssurf, Srect)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        bg = pygame.image.load("backk.jpg")        
        playSurface.blit(bg,(0,0))
        largeText = pygame.font.SysFont('comicsansms',100)
        TextSurf, TextRect = text_objects("Snako", largeText,black)
        TextRect.center = ((360),(220))
        playSurface.blit(TextSurf, TextRect)
        button(230,300,140,60,white,gray,"PLAY",game_loop)
        button(400,300,140,60,white,gray,"QUIT",quitgame)
       
        pygame.display.update()
        clock.tick(15)
#Main Logic Of Game
def game_loop():
      #  global changeTo
        # global direction
        #global foodPos
        #global foodSpawn
        #global snakePos
    global score
    snakePos = [100,50]
    snakeBody = [[100,50],[90,50],[80,50]] #,[70,50],[60,50],[50,50],[40,50],[30,50],[20,50]

    foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
    foodSpawn = True

    direction = 'RIGHT'
    changeTo = direction
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    changeTo = 'RIGHT'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    changeTo = 'LEFT'
                if event.key == pygame.K_UP or event.key == ord('w'):
                    changeTo = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    changeTo = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Validation of direction
        if changeTo == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if changeTo == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if changeTo == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if changeTo == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'

        if direction == 'RIGHT':
            snakePos[0] += 10
        if direction == 'LEFT':
            snakePos[0] -= 10
        if direction == 'UP':
            snakePos[1] -= 10
        if direction == 'DOWN':
            snakePos[1] += 10

        # snake bodyh mechanism
        bg = pygame.image.load("game.jpg")       
        playSurface.blit(bg,(0,0))
        snakeBody.insert(0, list(snakePos))
        if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
            score+=10
            foodSpawn = False
        else:
            snakeBody.pop()

        if foodSpawn == False:
            foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
        foodSpawn = True

        for pos in snakeBody:
            pygame.draw.rect(playSurface,brown,pygame.Rect(pos[0], pos[1],10,10))

        pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

        if snakePos[0] > 710 or snakePos[0] < 0:
            gameOver()
        if snakePos[1] > 450 or snakePos[1] < 0:
            gameOver()

        for block in snakeBody[1:]:
            if snakePos[0] == block[0] and snakePos[1] == block[1]:
                gameOver()

        showScore()

        pygame.display.flip()
        fpsController.tick(10)
game_intro()        
game_loop()        