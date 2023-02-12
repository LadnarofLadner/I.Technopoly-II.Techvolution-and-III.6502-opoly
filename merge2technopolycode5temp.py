import random
import pygame

# Initialize the pygame

# create the pygame
pygame.init()

# create the screen
def text_format(message, textFont, textSize, textColor):
	screen = pygame.display.set_mode((1300,700))
	blue=(0, 0, 255)
	yellow=(255,255,0)
	white=(255, 255, 255)
	black=(0, 0, 0)



#Main Menu
def main_menu():

	menu=True
	selected="start"

	while menu:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_UP:
					selected="start"
				elif event.key==pygame.K_DOWN:
					selected="quit"
				if event.key==pygame.K_RETURN:
					if selected=="start":
						print("Start")
					if selected=="quit":
						pygame.quit()
						quit()
	
		#Main Menu UI		
		screen.fill(blue)
		title=text_format("Sourcecodester", font, 90, yellow)
		if selected=="start":
			text_start=text_format("START", font, 75, white)
		else:
			text_start = text_format("START", font, 75, black)
		if selected=="quit":
			text_quit=text_format("QUZIT", font, 75, black)
		else:
			text_quit=text_format("QUIT", font, 75, black)

		title_rect=title.get_rect()
		start_rect=text_start.get_rect()
		quit_rect=text_quit.get_rect()

		# Main Menu Text
		screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
		screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
		screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
		clock.tick(FPS)
		pygame.display.set_caption("Python -Pygame Simple Main Menu Selection")

#Initialize the Game
main_menu()
pygame.quit()
quit()

# create the screen
screen = pygame.display.set_mode((1300,700))
	
#Title and Icon
pygame.display.set_caption("Technopoly")
icon = pygame.image.load('ram.png')
pygame.display.set_icon(icon)

#Background

Background = pygame.image.load('technopolyboard725sq.bmp')
BackgroundX = 250
BackgroundY = 0

#Player
playerImg = pygame.image.load('ram (1).bmp')
playerX = 280
playerY = 225
playerImg3 = pygame.image.load('ram (2).bmp')
player3X = 280
player3Y = 285
playerImg4 = pygame.image.load('ram (3).bmp')
player4X = 280
player4Y = 350
playerImg5 = pygame.image.load('ram (4).bmp')
player5X = 280
player5Y = 405
playerImg6 = pygame.image.load('ram (5).bmp')
player6X = 280
player6Y = 465
playerImg7 = pygame.image.load('ram (6).bmp')
player7X = 280
player7Y = 520
playerImg8 = pygame.image.load('ram (7).bmp')
player8X = 280
player8Y = 580

def player1():
	screen.blit(playerImg, (playerX, playerY))

def player3():
	screen.blit(playerImg3, (player3X, player3Y))

def player4():
	screen.blit(playerImg4, (player4X, player4Y))

def player5():
	screen.blit(playerImg5, (player5X, player5Y))

def player6():
	screen.blit(playerImg6, (player6X, player6Y))

def player7():
	screen.blit(playerImg7, (player7X, player7Y))

def player8():
	screen.blit(playerImg8, (player8X, player8Y))

def BackGround():
	screen.blit(Background, (BackgroundX, BackgroundY))

# Game Loop
running = True
while running:

	# RGB - Red, Green, Blue		
	screen.fill((0, 255, 255))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


	BackGround()
	player1()
	player3()
	player4()
	player5()
	player6()
	player7()
	player8()
	pygame.display.update()
#Game Loop2

#Meyer's_Original_Technpoly.py - TECHNOPOLY
	print("Developed by Randall Meyer (with code partially derived from Stephen Hustedde's MONOPOLY ROLLS program.)\n")
	print("""This game is a tool to teach three different lessons to students of the sciences and humanities.
	The first game (I) can be played like that other more boring and inaccurate game developed in 1915 by Lizzie Maggie and sometimes 		referred to as 'The Landlord's Game'.
	The second game, (II), provides a more accurate lesson of the TECHVOLUTION of the human animal, wherein each physical address is replaced
	The Third Game, (III), has players collect Op Code Cards and Digital Data Cards, and actually hand program a schematic moidel of the 		vintage 6502 microproceesor from 1975.\n""")

	spaces = ["Go (COLLECT 200$)", "Numbers", "Patent Fees", "Writing", "Serendipity ; Community Quest",
          "Metallic Circuits", "Time", "Innovation Station", "Math and Measure", "Logic",
          "Visiting College ; Research", "Optics", "Data Farm", "Chemistry", "Physics",
          "Electromagnetic Spectrum", "Electricity", "Magnetism", "Automata", "Parents Garage",
          "Vacuum Tubes", "Innovation Station", "Crystals", "Interconnection", "Satellites and Rockets",
          "Mechanical Computers", "Electro-Mechanical Computers", "Semiconductor Fabrication Facility", "Electronic Computers", "Go To College",
          "Memory", "Operating Systems", "Serendipity ; Community Quest", "Data Structures","Lasers and Fiber Optics",
          "Innovation Station", "Integrated Circuits", "Incorporation fees", "Microprocessors"]

	current = 0
	die1 = die2 = total = 0
	doubles = 0
	rolls = 0
	print("Technopoly! You are currently on GO (COLLECT $200).")
	roll_em = input("Press Enter to roll dice; x to end")

	while (roll_em.upper() != "X")  :
		die1 = random.randint (1,6)
		die2 = random.randint (1,6)
		total = die1 + die2
		rolls += 1
		current = (current + total) % 39 # add total roll to current location and use modulus too
		mySpace = spaces[current]
		print('\nYou rolled a {0} and a {1} for a total of {2}. You\'re at "{3}".'.format(die1, die2, total, mySpace.upper()))
		roll_em = input("Press Enter to roll dice; x to end")
	
		print("\nThanks for playing ... you rolled",rolls,"times.\n")	