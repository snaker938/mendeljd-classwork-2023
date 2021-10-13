# Import the pygame library and initialise the game engine
import pygame
from ball import Ball
from paddle import Paddle
from ball import Ball
 
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
 
# -------- Main Program Loop -----------
while playing:
    # --- Main event loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              playing = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     playing=False


    # --- Game logic should go here

    

    all_sprites_list.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.move_up(5)
    if keys[pygame.K_s]:
        paddleA.move_down(5)


        
    if ball.rect.x>=690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()
 
 
    # --- Drawing code should go here

    
    screen.fill(BLACK)
    
    #Draw the playing ground
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    
    all_sprites_list.draw(screen) 
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()