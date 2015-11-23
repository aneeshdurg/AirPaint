import cv2
import numpy as np
import pygame
pygame.init()
SIZE = [1920, 1080]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Test blobs")
colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
color=0
done=False
x, y=0, 0
cap = cv2.VideoCapture(0)
screen.fill((255, 255, 255))
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
		color = len(colors)-1	
	# Take each frame
	#screen.fill((0, 0, 0))
	_, frame = cap.read()
	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)# define range of blue color in HSV
	lower_blue = np.array([20,20,20])
	upper_blue = np.array([45,255,255])
	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask= mask)
	#cv2.imshow('frame',frame)
	#cv2.imshow('mask',mask)
	#cv2.imshow('res',res)
	params = cv2.SimpleBlobDetector_Params()
	params.filterByArea = 1
	params.minArea = 100
	params.filterByColor = 1
	params.blobColor = 0
	detector = cv2.SimpleBlobDetector(params)
	keypoints = detector.detect(res)
	im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	#cv2.imshow("Keypoints", im_with_keypoints)

	for kpt in keypoints:
		print str(kpt.pt[0])+" "+str(kpt.pt[1])
		x =int(keypoints[0].pt[0])
		y =int(keypoints[0].pt[1])
	pygame.draw.circle(screen, colors[color], [1920 - 3*x, 2*y], 5)
	pygame.display.flip()

cv2.destroyAllWindows()