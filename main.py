import cv2
import numpy as np
import pygame

pygame.init()
SIZE = [1920, 1080]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Air Paint")
screen.fill((255, 255, 255))
done=False

colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
colorString = ["Black", "Red", "Green", "Blue", "Yellow", "Purple", "Turquoise", "Eraser"]
color=0
brushSize = 5
eraser = [False, 0, 5]

cap = cv2.VideoCapture(0)
x, y=0, 0

while not done:

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

	if pygame.key.get_pressed()[pygame.K_SPACE]:
		color+=1
		color%=(len(colors)-1)
		brushSize = eraser[2]

	if pygame.key.get_pressed()[pygame.K_b]:
		color = 0
	if pygame.key.get_pressed()[pygame.K_r]:
		color = 1
	if pygame.key.get_pressed()[pygame.K_g]:
		color = 2
	if pygame.key.get_pressed()[pygame.K_b]:
		color = 3
	if pygame.key.get_pressed()[pygame.K_y]:
		color = 4
	if pygame.key.get_pressed()[pygame.K_p]:
		color = 5
	if pygame.key.get_pressed()[pygame.K_t]:
		color = 6

	if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
		screen.fill((255, 255, 255))
		eraser[2] = 5
		brushSize = eraser[2]

	if pygame.key.get_pressed()[pygame.K_e]:
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

	pygame.display.set_caption("Air Paint Color: "+colorString[color]+", Brush Size: "+str(brushSize))
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower = np.array([20,20,20])
	upper = np.array([45,255,255])
	mask = cv2.inRange(hsv, lower, upper)
	res = cv2.bitwise_and(frame,frame, mask= mask)
	params = cv2.SimpleBlobDetector_Params()
	params.filterByArea = 1
	params.minArea = 100
	params.filterByColor = 1
	params.blobColor = 0
	detector = cv2.SimpleBlobDetector(params)
	keypoints = detector.detect(res)
	#im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	#cv2.imshow("Keypoints", im_with_keypoints)

	for kpt in keypoints:
		print str(kpt.pt[0])+" "+str(kpt.pt[1])
		x =int(keypoints[0].pt[0])
		y =int(keypoints[0].pt[1])

	pygame.draw.circle(screen, colors[color], [1920 - 3*x, 2*y], brushSize)
	pygame.display.flip()