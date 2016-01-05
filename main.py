import cv2
import numpy as np
import pygame
import sys
import AirBrush
import os
#Arugments
printpts = False
show = False
changeDim = False
b, g, r = 0, 255, 255
for i in range(1, len(sys.argv)):
	arg = sys.argv[i]
	if arg == '-a':
		printpts = True
		show = True
	elif arg == '-p':
		printpts = True
	elif arg == '-v':
		show = True
	elif arg == '-c':
		b = int(raw_input("B: "))
		g = int(raw_input("G: ")) 
		r = int(raw_input("R: "))
	elif arg == '-s':
		changeDim = True
		w = int(raw_input("Width: "))
		h = int(raw_input("Height: "))

#pygame vars
pygame.init()
pygame.mouse.set_visible(False)
SIZE = [800, 640]
if changeDim:
	SIZE[0] = w
	SIZE[1] = h
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Air Paint")
#Canvas for painting, cursor for drawing cursor
canvas = pygame.Surface(screen.get_size())
canvas = canvas.convert()
cursor = pygame.Surface(screen.get_size())
cursor.set_colorkey((1,1,1))
canvas.fill((255, 255, 255))
#color and paint related vars
colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
colorString = ["Black", "Red", "Green", "Blue", "Yellow", "Purple", "Turquoise", "Eraser"]
color=0
brushSize = 5
eraser = [False, 0, 5]
rainbow = False
draw = False
#brush
cap = cv2.VideoCapture(0)
brush = AirBrush.brush(cap=cap, B=b, G=g, R=r)
x, y=0, 0
#main loop
done=False
while not done:
	cursor.fill((1, 1, 1))
	#Keyboard input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				done = True
	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		exit()
	if pygame.key.get_pressed()[pygame.K_UP]:
		eraser[2]+=1
		brushSize = eraser[2]
		

	if pygame.key.get_pressed()[pygame.K_DOWN]:
		eraser[2]-=1
		if eraser[2]<0:
			eraser[2] = 0
		brushSize = eraser[2]
		
		
	if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT]:
		eraser[2]=5	
		brushSize = eraser[2]
		rainbow=False

	if pygame.key.get_pressed()[pygame.K_SPACE]:
		color+=1
		color%=(len(colors)-1)
		brushSize = eraser[2]
		rainbow=False

	if pygame.key.get_pressed()[pygame.K_RETURN]:
		draw = not draw
		
	if pygame.key.get_pressed()[pygame.K_d]:
		color = 0
		rainbow=False
	if pygame.key.get_pressed()[pygame.K_r]:
		color = 1
		rainbow=False
	if pygame.key.get_pressed()[pygame.K_g]:
		color = 2
		rainbow=False
	if pygame.key.get_pressed()[pygame.K_b]:
		color = 3
		rainbow=False
	if pygame.key.get_pressed()[pygame.K_y]:
		color = 4
		rainbow=False
	if pygame.key.get_pressed()[pygame.K_p]:
		color = 5
		rainbow=False
	if pygame.key.get_pressed()[pygame.K_t]:
		color = 6
		rainbow=False
	if pygame.key.get_pressed()[pygame.K_TAB]:
		rainbow=True	

	if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
		canvas.fill((255, 255, 255))
		eraser[2] = 5
		brushSize = eraser[2]
		rainbow=False

	if pygame.key.get_pressed()[pygame.K_e]:
		rainbow=False
		if eraser[0]:
			eraser[0] = False
			color = eraser[1]
			brushSize = eraser[2]

		else:
			eraser[0] = True
			eraser[1] = color
			eraser[2] = brushSize
			color = len(colors)-1
			brushSize = brushSize + 5

	if pygame.key.get_pressed()[pygame.K_s]:
		pygame.image.save(canvas, "Picture.bmp")
		
	if rainbow:
		color+=1
		color%=6		


	pygame.display.set_caption("[Air Paint] Color: "+colorString[color]+", Brush Size: "+str(brushSize)+", Lifted: "+str(not draw))
	#Get position of brush
	x, y, found = brush.getPos(show, printpts)

	x = SIZE[0] - int(SIZE[0]/brush.width)*x
	y = int(SIZE[1]/brush.height)*y

	if found:
		try:
			pygame.mouse.set_pos([x, y])
			#Draw cursor
			pygame.draw.rect(cursor, colors[color], (x-brushSize, y-brushSize, brushSize, brushSize), 2)
			pygame.draw.rect(cursor, (255, 255, 255), (x-brushSize+2, y-brushSize+2, brushSize-4, brushSize-4), 2)
		except TypeError:
			pass
	
		if draw:
			try:
				pygame.draw.circle(canvas, colors[color], [x, y], brushSize)
				#Draw cursor
				if color == len(colors)-1:
					pygame.draw.rect(cursor, (0, 0, 0), (x-brushSize, y-brushSize, brushSize, brushSize), 1)
					pygame.draw.rect(cursor, (255, 255, 255), (x-brushSize+2, y-brushSize+2, brushSize-4, brushSize-4))
				else:
					pygame.draw.rect(cursor, colors[color], (x-brushSize, y-brushSize, brushSize, brushSize))
			except:
				pass
	#Draw cursor on top of canvas
	screen.blit(canvas, (0, 0))
	screen.blit(cursor, (0, 0))
	pygame.display.flip()