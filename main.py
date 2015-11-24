import cv2
import numpy as np
import pygame

pygame.init()
SIZE = [1920, 1080]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Test blobs")
screen.fill((255, 255, 255))
done=False

colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
color=0
brushSize = 5
eraser = [False, 0]

cap = cv2.VideoCapture(0)
x, y=0, 0

while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				done = True
	if pygame.key.get_pressed()[pygame.K_SPACE]:
		color+=1
		color%=(len(colors)-1)
	if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
		screen.fill((255, 255, 255))	
	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		exit()
	if pygame.key.get_pressed()[pygame.K_c]:
		if eraser[0]:
			eraser[0] = False
			color = eraser[1]
			brushSize = 5

		else:
			eraser[0] = True
			eraser[1] = color
			color = len(colors)-1
			brushSize = 10

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