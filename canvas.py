import numpy as np
from PIL import Image

class Canvas:
    """The canvas where all the shapes are going to be drawn"""
    def __init__(self, height, width, color):
        # The color of each pixel
        self.color = color
        # rows of the array
        self.height = height
        # pixels in each row
        self.width = width
        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change the [0, 0, 0] black color of each pixel with the user given value for color
        self.data[:] = self.color
    
    def make(self, imagepath):
        """Converts the current numpy array into an image file"""
        image = Image.fromarray(self.data, "RGB")
        image.save(imagepath)