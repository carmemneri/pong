import sys, random, pygame
from pygame.locals import *

screenSize = screenWidth, screenHeight = 1000, 600

black = 0,0,0
white = 255,255,255

def telaInicial():
    text = titulo.render('pong.io', 1, white)
    play = fonteDefault.render('play', 1, white)
    options = fonteDefault.render('options', 1, white)
    credits = fonteDefault.render('credits', 1, white)
    screen.blit(text,(400,100))
    screen.blit(play,(300,200))
    screen.blit(options,(300,250))
    screen.blit(credits,(300,300))
    
def credits():
    msg = 'Obrigado Galerinha por Jogar este meu joguinho muito bom, porque eu tenho que ter a autoestima alta'
    screen.blit(msg,(300,300))
    
def game():
	player1 = {
    'width': 25,
    'height': 100,
    'posx': 100,
    'posy': 250,
    'speed': 1
    }
    
	player2 = {
    'width': 25,
    'height': 100,
    'posx': 875,
    'posy': 250,
    'speed': 1
	}
	
	ball = {
    'width': 25,
    'height': 25,
    'posx': 500,
    'posy': 250,
    'speed': 1
	}
    
    #movimentacao player1
	while True:
		screen.fill(black)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		key = pygame.key.get_pressed()

		# Movimentacao Player 1
		if key[K_w]:
			player1['posy'] -= player1['speed']

		if key[K_s]:
			player1['posy'] += player1['speed']

		if player1['posy'] <= 0:
			player1['posy'] = 0

		elif player1['posy'] + player1['height'] >= screenHeight:
			player1['posy'] = screenHeight - player1['height']
			
		# Movimentacao Player 2	
		if key[K_UP]:
			player2['posy'] -= player2['speed']

		if key[K_DOWN]:
			player2['posy'] += player2['speed']

		if player2['posy'] <= 0:
			player2['posy'] = 0

		elif player2['posy'] + player2['height'] >= screenHeight:
			player2['posy'] = screenHeight - player2['height']
		
		#background
		screen.fill(black)

		#player 1
		pygame.draw.rect(screen,white,(player1['posx'],player1['posy'],player1['width'],player1['height']))

		#player 2
		pygame.draw.rect(screen,white,(player2['posx'],player2['posy'],player2['width'],player2['height']))
		#ball
		pygame.draw.rect(screen,white,(ball['posx'],ball['posy'],ball['width'],ball['height']))

		pygame.display.update()
		
		
    
    
pygame.init()

fonteMain = pygame.font.get_default_font()
titulo = pygame.font.SysFont(fonteMain,60)
fonteDefault = pygame.font.SysFont(fonteMain, 45)

screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption("")

while True:

    #condicoes de saida

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    key = pygame.key.get_pressed()
    if(key[K_g]):
		game()
    if key[K_w] and key[K_LCTRL]:
        sys.exit()

    #background
    # testar se eu n colocar um background ele vai ficar dando o bug de repeticao
    screen.fill(black)

    telaInicial()

    # aprender pra q serve: pygame.display.update()
    pygame.display.flip()
    
pygame.quit()













'''(pygame.font.init()

    fonteMain = pygame.font.get_default_font()
    titulo = pygame.font.SysFont(fonteMain,60)
    fonteDefault = pygame.font.SysFont(fonteMain, 45)
    text = titulo.render('pong.io', 1, white)
    play = fonteDefault.render('play', 1, white)
    options = fonteDefault.render('options', 1, white)
    credits = fonteDefault.render('credits', 1, white)
    screen.blit(text,(400,100))
    screen.blit(play,(300,200))
    screen.blit(options,(300,250))
    screen.blit(credits,(300,300)))'''

'''
 #player 1 "print"
    pygame.draw.rect(screen,white,(player1['posx'],player1['posy'],player1['width'],player1['height']))


#background
    # testar se eu n colocar um background ele vai ficar dando o bug de repeticao
    screen.fill(black)

    events = pygame.event.get()

    #movimentacao player1

    key = pygame.key.get_pressed()

    if key[K_w]:
        player1['posy'] -= player1['speed']

    if key[K_s]:
        player1['posy'] += player1['speed']

    if player1['posy'] <= 0:
        player1['posy'] = 0

    elif player1['posy'] + player1['height'] >= screenHeight:
        player1['posy'] = screenHeight - player1['height']'''
