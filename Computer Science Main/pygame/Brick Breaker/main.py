# Import the pygame library and initialise the game engine
import pygame
from ball import Ball
from paddle import Paddle
from ball import Ball
from block import Block
import time
import random
 
pygame.init()
 
# Colours :)
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Open a new window
size = (550, 700)
# size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("block Breaker")

all_sprites_list = pygame.sprite.Group()


#Player paddle
paddle = Paddle(WHITE, 100, 10)
paddle.rect.x = 225
paddle.rect.y = 630


# Ball
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195


# Add sprites to group

all_sprites_list.add(paddle)
all_sprites_list.add(ball)



################### BLOCKS   ########################

all_blocks = pygame.sprite.Group()
for i in range(6):
    block = Block(WHITE,80,30)
    block.rect.x = 50 + i* 100
    block.rect.y = 60
    all_sprites_list.add(block)
    all_blocks.add(block)
for i in range(6):
    block = Block(WHITE,80,30)
    block.rect.x = 50 + i* 100
    block.rect.y = 100
    all_sprites_list.add(block)
    all_blocks.add(block)
for i in range(6):
    block = Block(WHITE,80,30)
    block.rect.x = 50 + i* 100
    block.rect.y = 140
    all_sprites_list.add(block)
    all_blocks.add(block)




playing = True

score = 0
lives = 3
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()




# -------- Main Program Loop -----------
while playing:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
              playing = False 
        


    # --- Game logic should go here
    
    all_sprites_list.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        paddle.move_right(5)
    if keys[pygame.K_a]:
        paddle.move_left(5)



    if ball.rect.x>=540: # 550, from 800 :: 700, from 600
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>690:
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (125,195))
            pygame.display.flip()
            pygame.time.wait(3000)

            playing = False

    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]


    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()


    block_collision_list = pygame.sprite.spritecollide(ball,all_blocks,False)
    for brick in block_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
      if len(all_blocks)==0:
           #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (125,195))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Stop the Game
            playing=False




    # --- Drawing code should go here

    
    screen.fill(BLACK)
    
    #Draw the playing ground
    # pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    
    all_sprites_list.draw(screen) 


    #Display scores:
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (450,10))

    
 
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
print("oogles")
# input("Please enter to continue...")
pygame.quit()