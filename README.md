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
  
  
  I did not include a pytest file for two main reasons: First, I find it difficult to write a test file when I do have clearly distinguished goals for the program. I am mostly guessing as the exact objectives, expectations, and limitations of the challenge since I did receive the challange prompt. For example, I am not sure if the objective is to find all white edges, black edges, or both. Second, spefically for edge detection, it seems to me that visually checking the output is a quick and easy method of checking if the program is working as intended. Of course if there were a large number of images, this would be impractical. But also, if the images were more complex than grids, such as photos of people, I am not sure how a comprehensive test could be written and again visual checking by humans would work well. 
  
The edge detection threshold parameters did not seem to have much effect on the PNG images, but there was a very noticable effect on the JPG. This is why I also included a script for testing these parameters. 
  
  

