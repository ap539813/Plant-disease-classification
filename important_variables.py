from keras import backend as K

# Define the hight and width of the images as required

img_width, img_height = 128, 128

# dimensions of our images.
img_width, img_height = 128, 128
if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)