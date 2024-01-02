import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

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

def process_images(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    lakes = set([file.split('_')[0] for file in files])
    processor = ImageProcessor()
    
    for lake in lakes:
        before_path = os.path.join(folder_path, f'{lake}_Before.jpg')
        after_path = os.path.join(folder_path, f'{lake}_After.jpg')
        image1 = processor.load_image(before_path)
        image2 = processor.load_image(after_path)
        changes = processor.detect_changes(image1, image2)
        plt.imshow(changes, cmap='gray')
        plt.title(f'Detected Changes in {lake}')
        plt.show()

def main():
    images_folder = 'path_to_images_folder'  # Update with the path to your 'images' folder
    process_images(images_folder)

if __name__ == '__main__':
    main()
