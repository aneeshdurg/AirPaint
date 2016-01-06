# AirPaint
Requires openCV, pygame, numpy and a working webcam (quality is not important).
It is reccomended that you are in a well illuminated environment while you use
AirPaint.

A paint application that uses openCV and blob detection to replace the paint brush.
The frames captured from the webcam are first filtered for the color yellow and then
scanned for dark blobs. To change the color being filtered, run main.py with the 
argument '-c' and enter the BGR values for the new color.

To view the keypoints being detected, run main.py with the argument '-v'
  
By running main.py with the argument '-p', viewing the console while main.py is running 
will show the coordinate of the brush with respect to your webcam 
(as opposed to the pygame screen to which it is mapped).

To view the keypoints being picked up and the coordinates of the keypoints, use the 
argument '-a'

To change the dimensions of the output window, use the argument '-s'

Controls:
  Brush - your "brush" (*)
  
  Lift/place brush - Return
  
  Increase brush size - Up
  
  Decrease brush size - Down
  
  Reset brush size - Left or Right

  Clear Screen - Backspace

  Cycle through colors - Space
  
  Disco mode - Tab

  Draw Line - Hold brush still for 3s to start drawing a line, 3s to stop
  
  Change to color:	
  
  	Black - d
  	
  	Red - r
  	
  	Green - g
  	
  	Blue - b
  	
  	Yellow - y
  	
  	Purple - p
  	
  	Turquoise - t

  Eraser - e
  
  Save image - s (saves to Picture.bmp)

  Exit - Escape 
  

*You need to make the brush. Mine is a yellow pen, with a black piece of paper attached to it.

![Brush](http://i.imgur.com/K6bKWJx.jpg "Brush")

