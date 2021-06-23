from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import numpy as np
import argparse
import cv2
import os
from imutils import paths

print("[INFO] loading images...")
imagePaths = list(paths.list_images("/content/data_upload_v3/train/non"))
data = []

# loop over the image paths
for imagePath in imagePaths:
	# extract the class label from the filename
	label = imagePath.split(os.path.sep)[-2]

	# load the image, swap color channels, and resize it to be a fixed
	# 224x224 pixels while ignoring aspect ratio
	image = cv2.imread(imagePath)
	# update the data and labels lists, respectively
	data.append(image)
for image in data:
	# load the input image, convert it to a NumPy array, and then
	# reshape it to have an extra dimension
	print("[INFO] loading example image...")
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)

	# construct the image generator for data augmentation then
	# initialize the total number of images generated thus far
	aug = ImageDataGenerator(
		rotation_range=30,
		zoom_range=0.15,
		width_shift_range=0.2,
		height_shift_range=0.2,
		shear_range=0.15,
		horizontal_flip=True,
		fill_mode="nearest")
	total = 0

	# construct the actual Python generator
	print("[INFO] generating images...")
	#imageGen = aug.flow(image, batch_size=1, save_to_dir="/content/drive/MyDrive/generated_dataset/train/non",
		save_prefix="image", save_format="jpg")

	# loop over examples from image data augmentation generator
	for image in imageGen:
		# increment counter
		total += 1

		# if we have reached the specified number of examples, break
		# from the loop
		if total == 50: #total no of generated augmented imgs from each image
			break