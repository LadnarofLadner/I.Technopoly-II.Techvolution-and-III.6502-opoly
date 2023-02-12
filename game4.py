import pygame, sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1300,700])
base_font = pygame.font.Font(None,32)
user_text = 'I. Introduction'
user_text2 = 'II. Instructions'
user_text3 = 'III. Technopoly: Easy'
user_text4 = 'IV. Techvolution: Medium'
user_text5 = 'V. 6502-opoly: Hard'
user_text6 = 'VI. Exit'

input_rect = pygame.Rect(50,50,1200,32)
input_rect2 = pygame.Rect(50,100,1200,32)
input_rect3 = pygame.Rect(50,150,1200,32)
input_rect4 = pygame.Rect(50,200,1200,32)
input_rect5 = pygame.Rect(50,250,1200,32)
input_rect6 = pygame.Rect(50,300,1200,32)
color_active = pygame.Color('black')
color_passive = pygame.Color('gray15')
color = color_passive

active = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if input_rect.collidepoint(event.pos):
				active = True
			else:
				active = False
				

		if event.type == pygame.KEYDOWN:
			if active == True:
				if event.key == pygame.K_BACKSPACE:			
					user_text = user_text[0:-1]
				else:
					user_text +=event.unicode

	screen.fill((0,255,200))

	if active:
		color = color_active
	else:
		color = color_passive
	
	pygame.draw.rect(screen,color,input_rect,2)

	text_surface = base_font.render(user_text,True,(0,0,0))
	screen.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))

	pygame.draw.rect(screen,color,input_rect2,2)

	text_surface = base_font.render(user_text2,True,(0,0,0))
	screen.blit(text_surface,(input_rect2.x + 5, input_rect2.y + 5))

	pygame.draw.rect(screen,color,input_rect3,2)

	text_surface = base_font.render(user_text3,True,(0,0,0))
	screen.blit(text_surface,(input_rect3.x + 5, input_rect3.y + 5))

	pygame.draw.rect(screen,color,input_rect4,2)
	
	text_surface = base_font.render(user_text4,True,(0,0,0))
	screen.blit(text_surface,(input_rect4.x + 5, input_rect4.y + 5))

	pygame.draw.rect(screen,color,input_rect5,2)

	text_surface = base_font.render(user_text5,True,(0,0,0))
	screen.blit(text_surface,(input_rect5.x + 5, input_rect5.y + 5))
	
	pygame.draw.rect(screen,color,input_rect6,2)

	text_surface = base_font.render(user_text6,True,(0,0,0))
	screen.blit(text_surface,(input_rect6.x + 5, input_rect6.y + 5))
	
	pygame.display.flip()
	clock.tick(60)
