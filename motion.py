import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

class ImageProcessor:
    def __init__(self, target_size=(500, 500)):
        self.target_size = target_size

    def load_image(self, filepath):
        # Load an image from the given filepath and convert to grayscale
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            # Resize the image to the target size
            image = cv2.resize(image, self.target_size)
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
    files = os.listdir(folder_path)
    lakes = set(file.split('_')[0] for file in files if 'Before' in file or 'After' in file)
    
    processor = ImageProcessor(target_size=(500, 500))  # Set a common target size

    for lake in lakes:
        before_files = [f for f in files if f.startswith(lake) and 'Before' in f]
        after_files = [f for f in files if f.startswith(lake) and 'After' in f]
        
        for before_file, after_file in zip(before_files, after_files):
            before_path = os.path.join(folder_path, before_file)
            after_path = os.path.join(folder_path, after_file)
            image1 = processor.load_image(before_path)
            image2 = processor.load_image(after_path)

            if image1 is not None and image2 is not None:
                changes = processor.detect_changes(image1, image2)
                plt.imshow(changes, cmap='gray')
                plt.title(f'Detected Changes in {lake}')
                plt.show()
            else:
                print(f"Error loading images for {lake}")

def main():
    script_dir = os.path.dirname(__file__)  # Gets the directory where the script is located
    images_folder = os.path.join(script_dir, 'images')
    process_images(images_folder)

if __name__ == '__main__':
    main()
