
import cv2
import numpy as np
import matplotlib.pyplot as plt

class ImageProcessor:
    def __init__(self):
        pass

    def load_image(self, filepath):
        # Load an image from the given filepath and convert to grayscale
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        return image

    def compute_difference(self, image1, image2):
        # Compute the absolute difference between two images
        difference = cv2.absdiff(image1, image2)
        return difference

    def threshold_difference(self, difference, threshold=30):
        # Apply thresholding to highlight significant changes
        _, threshed = cv2.threshold(difference, threshold, 255, cv2.THRESH_BINARY)
        return threshed

    def detect_changes(self, image1, image2):
        # Detect significant changes between two images
        difference = self.compute_difference(image1, image2)
        threshed = self.threshold_difference(difference)
        return threshed

def main():
    # Paths to the two images for comparison
    image_path1 = 'path_to_first_image.jpg'
    image_path2 = 'path_to_second_image.jpg'

    # Create an instance of the ImageProcessor class
    processor = ImageProcessor()

    # Load the images
    image1 = processor.load_image(image_path1)
    image2 = processor.load_image(image_path2)

    # Detect changes
    changes = processor.detect_changes(image1, image2)

    # Display the changes
    plt.imshow(changes, cmap='gray')
    plt.title('Detected Changes')
    plt.show()

if __name__ == '__main__':
    main()
