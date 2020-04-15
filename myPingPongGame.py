import pygame, random
pygame.init()

pygame.display.set_caption('My Ping Pong Game')
windowLenght = 900
windowHeight = 600

#ball velocity
ball_velocity_x = 15 * random.choice((1,-1))
ball_velocity_y = 15 * random.choice((1,-1))

# create paddles and ball
paddle_1 = pygame.Rect(10, windowHeight/2, 30, 90)
paddle_2 = pygame.Rect(870, windowHeight/2, 30, 90)
ball = pygame.Rect(windowLenght/2, windowHeight/2, 30, 30)
net = pygame.Rect(windowLenght /2, 0, 10, windowLenght)
board = pygame.Rect(windowLenght/2 - 50, windowHeight/2, 100, 100)
#players score
player_1_score = 0
player_2_score = 0

running = True
isFirstRun = True
clock = pygame.time.Clock()
counter = 5

pygame.time.set_timer(pygame.USEREVENT, 1000)

while running:

    screen = pygame.display.set_mode([windowLenght, windowHeight])
    screen.fill((0,0,0))

    # display scoreboard
    font = pygame.font.Font(None, 74)
    text1 = font.render(str(player_1_score), 1, (255,255,255))
    screen.blit(text1, (300, 10))

    font = pygame.font.Font(None, 74)
    text2 = font.render(str(player_2_score), 1, (255,255,255))
    screen.blit(text2, (600, 10))

    for event in pygame.event.get():
        if isFirstRun:
            if event.type == pygame.USEREVENT:
                counter -= 1
                if counter == 0:
                    isFirstRun = False
                    counter = 'Play on!'
                font = pygame.font.Font(None, 320)
                text3 = font.render(str(counter), 1, (255,16,8))
                screen.blit(text3, (windowLenght/2 - 90, windowHeight/2 - 90))


        if event.type == pygame.QUIT:
            running = False

        # handles paddle motion functionality
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if paddle_1.y > 0:
                    paddle_1.y -= 20
            if event.key == pygame.K_z:
                if paddle_1.y < windowHeight - 90:
                    paddle_1.y += 20
            if event.key == pygame.K_k:
                if paddle_2.y > 0:
                    paddle_2.y -= 20
            if event.key == pygame.K_m:
                if paddle_2.y < windowHeight - 90:
                    paddle_2.y += 20

    if isFirstRun ==  False:
        # player scores
        if ball.left < 1:
            player_2_score += 1
        if ball.right >= windowLenght:
            player_1_score += 1

        # checks for ball hitting boundaries
        if ball.top <= 0 or ball.bottom >= windowHeight:
            ball_velocity_y *= -1
        if ball.left <= 0 or ball.right >= windowLenght:
            #ball will reset when hitting left or right boundry
            resetBall()

        # check if ball collides with paddles
        if ball.colliderect(paddle_1):
            ball_velocity_x *= -1
        if ball.colliderect(paddle_2):
            ball_velocity_x *= -1

        ball.y += ball_velocity_y
        ball.x += ball_velocity_x

    # Drawing pygame objects on canvas
    pygame.draw.rect(screen, (255,255,255), paddle_1)
    pygame.draw.rect(screen, (255,255,255), paddle_2)
    pygame.draw.rect(screen, (255,255,255), net)
    pygame.draw.ellipse(screen, (255,255,255), ball)
    pygame.display.flip()

    # function will reset ball and randomize ball direction
    def resetBall():
        global ball_velocity_x, ball_velocity_y
        ball_velocity_x *= random.choice((-1,1))
        ball_velocity_y *= random.choice((1,-1))
        ball.center = (windowLenght/2, windowHeight/2)


pygame.quit()
