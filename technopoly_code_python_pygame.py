import pygame

# Initialize the pygame

# create the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1000,1400))
	
#Title and Logo
pygame.display.set_caption("Technopoly")
icon = pygame.image.load("Technopoly_pygame_Logo.png")
pygame.display.set_icon (icon)

# Player
playerImg = pygame.image.load (CeramicDIP.jpg)
playerX = 10
playerY = 10


def player():
	screen.blit(playerImg, (playerX, playerY))


# Game Loop
running = True
while running:

	# RGB = Red, Green, Blue		
	screen.fill((0, 255, 255))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
			
	
	
	player()
	pygame.display.update()
