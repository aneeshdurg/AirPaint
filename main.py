import cv2
import numpy as np
import pygame
import sys
import AirBrush
#Arugments
printpts = False
show = False
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

#pygame vars
pygame.init()
SIZE = [1920, 1080]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Air Paint")
pygame.mouse.set_cursor(*pygame.cursors.diamond)
screen.fill((255, 255, 255))
done=False
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
brush = AirBrush.brush(cap, b, g, r)
x, y=0, 0
#main loop
while not done:
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
		pygame.mouse.set_visible(not draw)
	
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
		screen.fill((255, 255, 255))
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
		pygame.mouse.set_visible(False)
		pygame.image.save(screen, "Picture.bmp")
		pygame.mouse.set_visible(not draw)	

	if rainbow:
		color+=1
		color%=6		


	pygame.display.set_caption("[Air Paint] Color: "+colorString[color]+", Brush Size: "+str(brushSize)+", Lifted: "+str(not draw))
	#Get position of brush
	x, y, found = brush.getPos(show, printpts)

	x = 1920 - 3*x
	y = 2*y

	if found:
		try:
			pygame.mouse.set_pos([x, y])
		except TypeError:
			pass
	
		if draw:
			try:
				pygame.draw.circle(screen, colors[color], [x, y], brushSize)
			except:
				pass
	
	pygame.display.flip()