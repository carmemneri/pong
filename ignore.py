import sys, pygame, random

pygame.init()

size = width, height = 1000, 600
black = 0, 0, 0
white = 225, 225, 225

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
    'width': 20,
    'height': 20,
    'posx': 490,
    'posy': 290,
    'speedx': 1,
    'speedy': 1
}

ball['speedx'] = random.randint(-1,2)/2
ball['speedy'] = random.randint(-1,2)/2

screen = pygame.display.set_mode(size)

size = w, h = pygame.display.get_surface().get_size()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    events = pygame.event.get()

    #OBS: tem um bug com relacao a apertar uma tecla logo apos a outra
    #OBS2: ajeitar o random inicial da bola pra ela nao comecar muito rapido e nao comecar c um speedy mt pequeno ou speedx mt pequeno

    #movimentacao player1

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            player1['posy'] -= player1['speed']
        if event.key == pygame.K_s:
            player1['posy'] += player1['speed']

    if player1['posy'] <= 0 or player1['posy']+player1['height'] >= h:
        player1['speed'] = 0

    #movimentacao player2

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player2['posy'] -= player2['speed']
        if event.key == pygame.K_DOWN:
            player2['posy'] += player2['speed']

    #movimentacao ball

    ball['posx'] += ball['speedx']

    ball['posy'] += ball['speedy']

    if player1['posx'] <= ball['posx'] <= player1['posx'] + player1['width'] and player1['posy'] <= ball['posy'] <=player1['posy'] + player1['height']:
        ball['speedx'] = -ball['speedx']

    if ball['posx'] <= 0:
        ball['speedx'] = 0.5

    elif ball['posx'] >= 980:
        ball['speedx'] = -ball['speedx']

    if ball['posy'] <= 0:
        ball['speedy'] = -ball['speedy']

    elif ball['posy'] >= 580:
        ball['speedy'] = -ball['speedy']


    #background
    screen.fill(black)

    #player 1
    pygame.draw.rect(screen,white,(player1['posx'],player1['posy'],player1['width'],player1['height']))

    #player 2
    pygame.draw.rect(screen,white,(player2['posx'],player2['posy'],player2['width'],player2['height']))

    #ball
    pygame.draw.rect(screen,white,(ball['posx'],ball['posy'],ball['width'],ball['height']))

    pygame.display.flip()

pygame.quit()