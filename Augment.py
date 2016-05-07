from Utility import *


def elastic(image, label, Verbose=False):
	""" 
	Perform  transformation using elastic deformation
	"""

	# Squeeze the singleton dimensional of image
	# image   = np.squeeze(image)
	# label 	= np.squeeze(label)

	# 012 to 120
	# image = np.transpose(image, (1, 2, 0))
	# label = np.transpose(label, (1, 2, 0))

	# Retrieve image shape
	assert((image.shape[0] == label.shape[0]) and (image.shape[1] == label.shape[1]))

	shape = image.shape
	if Verbose:
		print "Perform  transformation using elastic deformation"
		print "Shape of image: ", image.shape
		print "Shape of label: ", label.shape
		pass

	dimx = shape[0]
	dimy = shape[1]

	# size = 8#np.int(dimx/8)
	# print size
	# disp = np.random.randint(size, size=(size, 2))
	# print disp
	# X, Y = np.meshgrid(np.arange(0, dimx), np.arange(0, dimy))
	# plt.quiver(X, Y)
	# plt.show()

	# http://stackoverflow.com/questions/11379214/random-vector-plot-in-matplotlib
	# x, y, u, v= np.random.random((4,10))
	# plt.quiver(x, y, u, v)
	# plt.show()
	size = 16
	ampl = 10
	du = np.random.uniform(-ampl, ampl, size=(size, size))
	dv = np.random.uniform(-ampl, ampl, size=(size, size))

	# Done distort at boundary
	du[ 0,:] = 0
	du[-1,:] = 0
	du[:, 0] = 0
	du[:,-1] = 0
	dv[ 0,:] = 0
	dv[-1,:] = 0
	dv[:, 0] = 0
	dv[:,-1] = 0

	plt.quiver(du, dv)
	plt.show()

	# Interpolate du
	DU = cv2.resize(du, (dimx, dimx)) 
	DV = cv2.resize(dv, (dimx, dimx)) 
	# DU = scipy.interpolate.interp2d(dimx, dimy, du, kind='cubic')
	# DV = scipy.interpolate.interp2d(dimx, dimy, dv, kind='cubic')

	# plt.quiver(DU, DV)
	# plt.show()
	X, Y = np.meshgrid(np.arange(shape[0]), np.arange(shape[1]))
	indices = np.reshape(Y+DV, (-1, 1)), np.reshape(X+DU, (-1, 1))
	label0 = label
	image = map_coordinates(image, indices, order=1).reshape(shape)
	label = map_coordinates(label, indices, order=1).reshape(shape)
	print np.median(label)
	# image = image.astype(np.uint8)
	# label = label.astype(np.uint8)

	print indices
	# image = scipy.interpolate.interp2d(DU, DV, image, kind='cubic')
	plt.imshow(np.hstack( (
							np.squeeze(label0), 
							np.squeeze(label), 
							np.squeeze(label0-label)
						  ), 
						  ) , cmap = plt.get_cmap('gray'))
	plt.show()
	
	# U = map_coordinates(u, (X, Y))
	# V = map_coordinates(v, (X, Y))
	# U, V = scipy.interpolate.RectBivariateSpline.ev(x, y)
	# plt.quiver(X, Y, U, V)
	plt.show()
	# 012 to 201
	# image = np.transpose(image, (2, 0, 1))
	# label = np.transpose(label, (2, 0, 1))

	return image, label