# AirPaint
Requires openCV, pygame, numpy and a working webcam (quality is not important).

A paint application that uses openCV and blob detection to replace the paint brush.
The frames captured from the webcam are first filtered for the color yellow and then
scanned for dark blobs. To view the keypoints being picked up, uncomment lines 94 and
95.

Viewing the console while main.py is running will show the coordinate of the brush
with respect to your webcam (as opposed to the pygame screen to which it is mapped).

Controls:
  Brush - your "brush" (*)
  
  Increase brush size - up
  Decrease brush size - down
  Reset brush size - left or right

  Clear Screen - Backspace

  Cycle through colors - Space
  Change to color:	
  	Black - b
  	Red - r
  	Green - g
  	Blue - b
  	Yellow - y
  	Purple - p
  	Turquoise - t

  Eraser - e
  
  Exit - Escape
  

*You need to make the brush. Mine is a yellow pen, with a black piece of paper attached to it.

![Brush](http://i.imgur.com/K6bKWJx.jpg "Brush")

