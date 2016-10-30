import pygame;
from process import process;
from classes import *;
from levels import *;
#
def clear_walls():
	Wall.List=[];

#level array here

arr_level=[level1,level2,level3];


#
pygame.init();
screen_height=160;
screen_width=160##320;
screen=pygame.display.set_mode((screen_width,screen_height));

clock=pygame.time.Clock();
FPS=60;
totoal_frams=0;
player=Player(0,0);#inilaizy with
end_point=EndPoint(0,0);#inializy with 0,0
def load_level(levelArray):

	screen.fill((0,0,0));#with black
	x,y=0,0;
	clear_walls();#clean all walls
	for row in levelArray:
		for col in row:
			if col=="W":
				Wall(x, y)
			if col=="E":
				end_point.x=x;	
				end_point.y=y;
			if col=="P":
				player.x=x;
				player.y=y;	
			x+=BaseClass.width;
		y+=BaseClass.heigth;
		x=0;			

load_level(level1);
level_number=0;
while True:
	#fill back ground first
	screen.fill((0,0,0));#with black
	#process
	process(player);
	#process

	#logic

	if player.colliderect(end_point):

		level_number+=1;
		if level_number>=len(arr_level):
			level_number=0;
		load_level(arr_level[level_number]);


	#logic




	#draw
	player.draw(screen);
	end_point.draw(screen);
	Wall.draw_all(screen);	
	#draw

	clock.tick(FPS);
	totoal_frams+=1;
	pygame.display.update();
	
	
