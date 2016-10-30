
#----------------------------------import---------------------------------
import pygame;
#----------------------------------import---------------------------------

#----------------------------------BaseClass------------------------------
class BaseClass(pygame.Rect):
	width,heigth=16,16;
	def __init__(self,x,y,color=(255,255,0)):
		super(BaseClass,self).__init__(x,y,BaseClass.width,BaseClass.heigth);
		self.color=color;
	def draw(self,screen):
	 	 pygame.draw.rect(screen,self.color,self);		

#----------------------------------BaseClass------------------------------	



#----------------------------------walls----------------------------------
class Wall(BaseClass):
	List=[];
	def __init__(self,x,y):
		super(Wall,self).__init__(x,y,color=(255,255,255));
		Wall.List.append(self);	
	@staticmethod
	def draw_all(screen):
		for wl in Wall.List:
			wl.draw(screen);


#----------------------------------walls----------------------------------	

#----------------------------------Player---------------------------------
class Player(BaseClass):
	def __init__(self,x,y):
		super(Player,self).__init__(x, y,color=(255,200,0));
	def move(self,dx,dy):
		if dx!=0:
			self.move_single_axis(dx,0);
		if dy!=0:
			self.move_single_axis(0,dy);	

	def move_walls(self,dx,dy):
		if dx==0 and dy==0:
			return;
		for wall in Wall.List:
			wall.x+=-dx;
			wall.y+=-dy;	
		EndPoint.End_point.x+=-dx;
		EndPoint.End_point.y+=-dy;		

	def move_single_axis(self,dx,dy):
		crash=False;
		rect=pygame.Rect(self);
		rect.x+=dx;
		rect.y+=dy;
		for wall in Wall.List:
			if rect.colliderect(wall):
				crash=True;
				break;
				# if dx>0:
				# 	self.right=wall.left;
				# if dx<0:
				# 	self.left=wall.right;
				# if dy>0:
				# 	self.bottom=wall.top;
				# if dy<0:
				# 	self.top=wall.bottom;
				# dx=0;			
		if not crash:
			#self.x+=dx;
			self.y+=dy;
			self.move_walls(dx, dy);					
			
#----------------------------------Player---------------------------------

#----------------------------------end_point---------------------------------
class EndPoint(BaseClass):
	End_point=None;
	def __init__(self,x,y):
		super(EndPoint,self).__init__(x, y,color=(255,0,0));
		self.image=pygame.image.load('m.png');
		EndPoint.End_point=self;

	def draw(self,screen):
		screen.blit(self.image,(self.x,self.y));



#----------------------------------end_point---------------------------------