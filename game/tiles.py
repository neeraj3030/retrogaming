import pygame
import time
import random


pygame.init()

display_width=800
display_height=600


gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Asphalt')
pygame.mixer.music.load("Broadway.mp3")
crash_sound=pygame.mixer.Sound("Crash.wav")
clock=pygame.time.Clock()

white=(255,255,255)
black=(0,0,0)
bright_red=(255,0,0)
bright_green=(0,255,0)
green=(0,150,0)
red=(150,0,0)
block_color=(53,115,255)

carImg= pygame.image.load('racecar.png')
pygame.display.set_icon(carImg)
car_width=73
pause=False

def fury(x,y):
	gameDisplay.blit(carImg,(x,y))


def things_dodged(count):
	font=pygame.font.SysFont(None,25)
	text=font.render('Score:'+str(count),True,black)
	gameDisplay.blit(text,(0,0))


def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def text_objects(text,font):
	TextSurface=font.render(text,True,black)
	return TextSurface,TextSurface.get_rect()


def crash():
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(crash_sound)



	largeText=pygame.font.SysFont('comicsansms',115)
	TextSurf,TextRect= text_objects('You Crashed',largeText)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				quitgame()
		
		#gameDisplay.fill(white)

		buttons('Restart',150,450,200,50,green,bright_green,game_loop)
		buttons('Quit',550,450,100,50,red,bright_red,quitgame) 
		

	pygame.display.update()		
	clock.tick(15)


def quitgame():
	pygame.quit()
	quit()

	
def buttons(msg,x,y,w,h,ic,ac,action=None):
	mouse=pygame.mouse.get_pos()
	click=pygame.mouse.get_pressed()

	if x+w>mouse[0]>x and y+h>mouse[1]>y:
		pygame.draw.rect(gameDisplay,ac,[x,y,w,h])
		if click[0]==1 and action!=None:
			action()


	else:
		pygame.draw.rect(gameDisplay,ic,[x,y,w,h])
	
	smallText=pygame.font.SysFont('freesansbold.ttf',40)
	TextSurf,TextRect= text_objects(msg,smallText)
	TextRect.center=((x+w/2),(y+h/2))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()		

def unpause():
	global pause
	pause=False



def paused():
	
	 
	while pause:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				quitgame()
		
		#gameDisplay.fill(white)
		largeText=pygame.font.SysFont('comicsansms',115)
		TextSurf,TextRect= text_objects('Asphalt',largeText)
		TextRect.center=((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf,TextRect)

		buttons('Continue',150,450,200,50,green,bright_green,unpause)
		buttons('Quit',550,450,100,50,red,bright_red,quitgame) 
		

	pygame.display.update()		
	clock.tick(15)




def game_intro():
	 
	while 1:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				quitgame()
		
		gameDisplay.fill(white)
		largeText=pygame.font.SysFont('freesansbold.ttf',135)
		TextSurf,TextRect= text_objects('Asphalt',largeText)
		TextRect.center=((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf,TextRect)

		buttons('GO!',150,450,100,50,green,bright_green,game_loop)
		buttons('Quit',550,450,100,50,red,bright_red,quitgame) 
		

	pygame.display.update()		
	clock.tick(15)

def game_loop():
	global pause
	pygame.mixer.music.play(-1)


	x=(display_width*0.45)
	y=(display_height*0.8)
	x_change=0
	gameExit=False
	
	thing_startx = random.randrange(0,display_width)
	thing_starty = -600
	thing_speed=0.5
	thing_width=100
	thing_height=100
	thing_count=1
	dodged=0
	while not gameExit:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			# print(event.type) [prints the int numbers, default value of pygame.QUIT=12 ]
			#print(event)
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					x_change = -5

				if event.key==pygame.K_RIGHT:
					x_change = 5

				if event.key==pygame.K_SPACE:
					pause=True
					paused()	

			if event.type==pygame.KEYUP:
				if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
					x_change = 0


		x+=x_change
		gameDisplay.fill(white)
		#things(thingx,thingy,thingw,thingh,color)	
			


		things(thing_startx,thing_starty,thing_width,thing_height,block_color)
		thing_starty+=thing_speed
		things_dodged(dodged)



		fury(x,y)
		if x < 0 or x > display_width-car_width:
			#pygame.time.wait(1000)
			crash()
            	
		if thing_starty > display_height:
			thing_starty = 0 - thing_height	
			thing_startx = random.randrange(0,display_width)
			#dodged+=1
			thing_speed+=1
			thing_width+=(1*0.2)
			thing_count=2
			
		if y < thing_starty + thing_height:
			print('y crossover')
			#if x > thing_startx and x < thing_startx+thing_width or x+car_width > thing_startx and x+car_width<thing_startx+thing_width:
				#print('x crossover')
				
			if x+car_width >thing_startx  and x < thing_startx+thing_width:
				#crash() 
				if y==thing_starty:	
					dodged+=1
					#break

				#gameDisplay.fill(white)
				#fury(x,y)

		pygame.display.update()
		clock.tick(60)
		
game_intro()
game_loop()



