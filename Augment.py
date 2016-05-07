from Utility import *

def elastic(img, Verbose=False):
	""" 
	Perform  transformation using elastic deformation
	"""

	# Squeeze the singleton dimensional of image
	img   = np.squeeze(img)

	# Retrieve image shape
	shape = img.shape
	if Verbose:
		print "Shape: ", shape
		pass

	return img