# Edge_Detector


Installation:

1. <code> pip install opencv-python </code>
2. <code> pip install matplotlib </code>

Use:

1. Optimal edge detection thresholds can be found using threshold_tester.py:

	X: Maximum value for minimum edge detection threshold
	
	Y: Increment increase for minimum edge detection threshold
	
	I: Maximum value for maximum edge detection threshold
	
	J: Increment increase for maximum edge detection threshold
	
	<code>python threshold_tester.py "PATH/TO/IMAGE" X Y I J </code>
	
  Script will display edge detection for each combination of min and max edge detection threshold. Careful not to to enter too many at once as it is exponential.
  
2. Directory of images can have edges written to them using edge_detector.py:

	<code>python edge_detector.py "PATH/TO/IMAGE/DIR" "PATH/TO/OUTPUT/DIR" minthresh maxthresh</code>
	
  Script will create new images in output directory with edges highlighted from images in input directory. Only accepts PNG or JPG images. 
  
  

