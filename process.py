import pygame;
import sys;

def process(player):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit();
			sys.exit();
	keys=pygame.key.get_pressed();
	if keys[pygame.K_LEFT]:
		player.move(-1,0);
	if keys[pygame.K_RIGHT]:
		player.move(1,0);
	if keys[pygame.K_UP]:
		player.move(0,-1);
	if keys[pygame.K_DOWN]:
		player.move(0,1);	