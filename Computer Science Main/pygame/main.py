"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
PINK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

    x = 485
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here

    BOTTOM=(51, 252, 40)
    BASE=(244,164,96)
    PINK = (255,105,180)
    SKY_BLUE = (135,206,235)

    #Draw background
    screen.fill(SKY_BLUE)

    #Draw bottom
    pygame.draw.rect(screen, BOTTOM, [0, 380, 500, 120], 0)
    
    
    #Draw Home base
    pygame.draw.rect(screen, BASE, [105,120,290,260], 0)
    
    #Draw draw top
    
    pygame.draw.polygon(screen, RED, [[241,315], [270,315], [255, 270]], 0)
    

    #Draw windows
    pygame.draw.rect(screen, PINK, [155, 155, 30, 30], 0)
    pygame.draw.rect(screen, PINK, [235, 155, 30, 30], 0)
    pygame.draw.rect(screen, PINK, [315, 155, 30, 30], 0)
    
    pygame.draw.rect(screen, PINK, [155, 215, 30, 30], 0)
    pygame.draw.rect(screen, PINK, [235, 215, 30, 30], 0)
    pygame.draw.rect(screen, PINK, [315, 215, 30, 30], 0)
    
    pygame.draw.rect(screen, PINK, [155, 275, 30, 30], 0)
    

    pygame.draw.rect(screen, PINK, [315, 275, 30, 30], 0)
    
    #Draw door
    pygame.draw.rect(screen, WHITE, [241, 315, 30, 65], 0)
    pygame.draw.rect(screen, (0,0,0), [240, 340, 20, 10], 0)

    #Draw Sun
    pygame.draw.circle(screen, (255,255,0), (x, 65), 65)

   
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()