import os
import numpy as np
import scipy as sc
import cv2 as cv
from scipy import ndimage
from skimage import filters
from matplotlib import pyplot as plt
# import seaborn as sns
from PIL import Image

class ImageConvlve():

    def __init__(self, image) -> None:
        self.image_array = np.asarray(image, np.int8)

    def getIntegralImage(self, image):
        self.image_array = np.asarray(image, np.int8)
        im_dims = image.shape
        im_height = 0
        im_width = 0
        im_channels = 0
        if (im_dims.size == 3):
            im_height = im_dims[0]
            im_width = im_dims[1]
            im_channels = im_dims[2]
        
        # Assume that we start at the top leftmost corner
        # We want to track a 2x2 box that slides across the entire image
        # Where m, n are the coordinates of the top left node in the 2x2 box
        m = 0
        n = 0
        sum = 0

        current_val = image[m + 1, n + 1]
        top_val = image[m + 1, n]
        left_val = image[m, n + 1]

        num_cells = image.size

        for k in num_cells:
            current_val = image[m + 1, n + 1]
            top_val = image[m + 1, n]
            left_val = image[m, n + 1]
            sum = current_val + top_val + left_val
            print("m: ", m, "\t n: ", n, "\t sum: ", sum)

            image[m + 1, n + 1] = sum