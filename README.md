# bullpen
The bullpen is a collection of homemade functions and procedures for general use.
It's contents include:
  1) entropyFunction.ipynb
    This notebook contains a homemade entropy() function which calulated the Entropy from a list of item counts of a collection of objects.  It's used to manually decide   splitting when building a decision tree.
  
  2)main_function_with_variable_numArguments.py
	This function is a template for how to define arguments to pass to a python script, as well as
	how to make some optional, and to pass variable numbers of arguments to the main call and into the
	script execution.
	
  3) master_caller directory contains caller.py and master.py
		They exist as a simple template examle of one script calling another.
		master has a function that computes a factorial.  caller just calls the master script.
		
   4) fractal.py
		Script takes no arguments.  It contains two functions (rgb_conv(iterator) and (mandelbrot()).  
		The former converts pixel values based on an iterator in the mandelbrot function.
		The later takes x & y pixel coordinates and generates a corresponding complex number
		using numpy.complex().  The script will iterate over a range of 1000 (step 1) and the final output is an image of the mandelbrot fractal both displayed and
		saved to the current directory ("mandelbrot.png").
		
	5) opencv_videostream.py
		Simple use of the python cv2 modele to stream your webcam.  Video is 
		imported as RGB numpy array and displayed realtime in a while loop.  Image feed can
		be converted to grayscale (see comments).  Press q to close the loop
		and the video stream.