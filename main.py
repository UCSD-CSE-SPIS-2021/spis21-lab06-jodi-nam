
import pygame
import os 

# the dimensions of the background image
screen_length = 600
screen_height = 427 
dim_field = (screen_length, screen_height)

# screen is created
screen = pygame.display.set_mode(dim_field)

# background is imported 
background = pygame.image.load(os.path.join("assets","background.jpg"))
background = pygame.transform.scale(background, dim_field)

# sprite is imported 
player = pygame.image.load(os.path.join("assets", "player.png")).convert()
player.set_colorkey((101, 141, 209))

# import flag and dimensions 
flag_length = 50
flag_height = 60
flag_dimension = (flag_length, flag_height)
flag = pygame.image.load(os.path.join("assets", "flag.png"))
flag = pygame.transform.scale(flag, flag_dimension)

# extra surprise :)
sun_length = 200
sun_height = 150
sun_dimension = (sun_length, sun_height)
sun = pygame.image.load(os.path.join ("assets", "done.jpeg"))
sun = pygame.transform.scale(sun, sun_dimension)
rect_sun = pygame.Rect(0, 0, 25, 10)

# creating player
x = 200
y = 200
width = 24
height = 26
rect_player = pygame.Rect(x, y, width, height)

# platforms
platform_1 = pygame.Rect(50, 350, 150, 10)
platform_2 = pygame.Rect(200, 150, 100, 10)
platform_3 = pygame.Rect(300, 250, 300, 10)
ground = pygame.Rect(0, screen_height-10, screen_length, 10)
platform_list = [ground, platform_1, platform_2, platform_3]   

# creating flag
rect_flag = pygame.Rect(500, 190, 25, 10)
flag_list = [rect_flag]

# Game loop
clock = pygame.time.Clock()
FPS = 60
running = True
jumping = True
while running:
    clock.tick(FPS)
    step_size = 12
    step_size_fall = 12
    jump_size = -20
 
 # gravity
    rect_player.move_ip(0, step_size_fall)
    
 # Location 2
 # Processing events
    for event in pygame.event.get():

      # Quit game
      if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_q:
            running = False

     # Horizontal movement 1
        #if event.key == pygame.K_RIGHT:
            #rect_player.move_ip(step_size , 0  )
        #if event.key == pygame.K_LEFT:
            #rect_player.move_ip(-step_size, 0  )

 # Location 3
 # horizontal movement ver 2
    keys = pygame.key.get_pressed()
    if keys [pygame.K_RIGHT]:
        rect_player.move_ip(step_size, 0)
    if keys [pygame.K_LEFT]:
        rect_player.move_ip(-step_size, 0)    

 # boundaries 
    if (rect_player.left <=  0):
        rect_player.left = 0
        
    if (rect_player.right >= screen_length):
        rect_player.right = screen_length
    
 # problem child :( top boundary doesnt work
    if rect_player.top > screen_height: 
        rect_player.top = screen_height 

    if (rect_player.bottom <= 0):
        rect_player.bottom = 0

 # collisions
    index = rect_player.collidelist(platform_list)

    if index != -1:
        rect_player.move_ip(0, -step_size)
              
 #collisions with flag
    win = rect_player.collidelist(flag_list)
    if win != -1:
        running = False
        print("You won!")
        # rect_player has to touch the checkered flag itself to win, not the pole.
 # jumping
    if jumping:  
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                rect_player.move_ip(0,jump_size) 




    screen.blit(background, (0,0))
    #pygame.draw.rect(screen, (255,0,0), rect_player)
    screen.blit(player, rect_player)

    pygame.draw.rect(screen, (25, 200, 50), ground)
    pygame.draw.rect(screen, (0, 50, 255), platform_1)
    pygame.draw.rect(screen, (0, 50, 255), platform_2 )
    pygame.draw.rect(screen, (0, 50, 255), platform_3 )
   
    screen.blit(flag, rect_flag)
    screen.blit(sun, rect_sun)

    pygame.display.update()


    #bruh we are SLOW #👹👹👹👹👹👹👹👹👹😭😭😭😭😭😭
    # we unfortunately did not fix our top boundary bc of time <3 # we are so sorry