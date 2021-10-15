# Import the pygame library and initialise the game engine
import pygame
from ball import Ball
from paddle import Paddle
from ball import Ball
import time
import random
 
pygame.init()
 
# Colours :)
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

 
#Player paddle
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
# AI Paddle
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

# Ball
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195
 

#draws every sprite in this group on the screen
all_sprites_list = pygame.sprite.Group()



all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
 


playing = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


#Initialise player scores
scoreA = 0
scoreB = 0




 

# -------- Main Program Loop -----------
while playing:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
              playing = False 
        


    # --- Game logic should go here

    def reset():

        paddleA.rect.x = 20
        paddleA.rect.y = 200

        paddleB.rect.x = 670
        paddleB.rect.y = 200

        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        all_sprites_list.draw(screen) 
        
        #Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (250,10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (420,10))


        pygame.display.flip()


    
    def create_timer(seconds):
        start = time.time()
        end = time.time()
        counter = 1
        while end - start < seconds:
            while counter < 4:
                # print("yep")
                # font = pygame.font.Font(None, 74)
                # text = font.render(str(counter), 1, WHITE)
                # screen.blit(text, (150,70))
                font = pygame.font.Font(None, 25)
                text = font.render(str(counter), True, BLACK)
                text_rect = text.get_rect(center=(700/2, 500/2))
                screen.blit(text, text_rect)
                time.sleep(0.5)
                counter += 1
            end = time.time()
        return

        



    # while not counter_var:
    
    all_sprites_list.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.move_up(5)
    if keys[pygame.K_s]:
        paddleA.move_down(5)


        
    if ball.rect.x>=690:
        scoreA+=1
        # point = True
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[0] = -ball.velocity[0]
        reset()
        time.sleep(0.5)
        create_timer(2)

        # pygame.time.delay(3000)
    if ball.rect.x<=0:
        scoreB+=1
        # point = True
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[0] = -ball.velocity[0]
        reset()
        time.sleep(0.5)
        create_timer(2)

        # pygame.time.delay(3000)
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]     

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    
    # opposition paddle AI
    # if paddleB.rect.y + 30 < ball.rect.y:
    #     paddleB.move_down(5)
    # elif paddleB.rect.y  + 30 > ball.rect.y:
    #     paddleB.move_up(5)

    # if paddleB.rect.y + random.randint(30, 35) < ball.rect.y:
    #     paddleB.move_down(7)
    # elif paddleB.rect.y  + random.randint(30, 35) > ball.rect.y:
    #     paddleB.move_up(7)
 
    if paddleB.rect.y + random.randint(20, 43) < ball.rect.y:
        paddleB.move_down(7)
    elif paddleB.rect.y  + random.randint(20, 43) > ball.rect.y:
        paddleB.move_up(7)

 
    # --- Drawing code should go here

    
    screen.fill(BLACK)
    
    #Draw the playing ground
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    
    all_sprites_list.draw(screen) 


    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))

    
 
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()