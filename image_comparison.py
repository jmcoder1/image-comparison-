"""
This program is my first attempt to find duplicate images and similar images using python.

It will heavily use python hashing.

"""

import os 
import sys


from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ORIGINAL_IMG = os.path.join(SCRIPT_PATH, "swiss_blade.jpg")
RESIZED_IMG = os.path.join(SCRIPT_PATH, "swiss_blade1.jpg")

def normalise(arr):
	"""

	"""
	rng = arr.max()-arr.min()
	amin = arr.min()

	return (arr-amin)*255/rng


def compareImages(img1, img2):
	"""
	Parameters:
		img1: the first image.
		img2: the second image.

	Return:
		numerical representaiton of the difference between the images.
	"""
	img1 = normalise(img1)
	img2 = normalise(img2)
	# calculate the difference and its norms
	diff = img1 - img2  # elementwise for scipy arrays
	m_norm = sum(abs(diff))  # Manhattan norm
	z_norm = norm(diff.ravel(), 0)  # Zero norm
	return (m_norm, z_norm)


def toGrayscale(arr):
	"""
	Parameters: 
		arr: array representation of an image.


	This function convers the arr (3D image) to a greyscale image if it is a colour image(2D)
	
	"""
	if len(arr.shape) == 3:
		return average(arr, -1)  # average over the last axis (color channels)
	else:
		return arr


def main():
	original_img = toGrayscale(imread(ORIGINAL_IMG).astype(float))
	resized_img = toGrayscale(imread(RESIZED_IMG).astype(float))

	n_m, n_0 = compareImages(original_img, resized_img)

	print("Manhattan norm:", n_m, "/ per pixel:", n_m/img1.size)
	print("Zero norm:", n_0, "/ per pixel:", n_0*1.0/img1.size)


if __name__ == "__main__":

	main()


