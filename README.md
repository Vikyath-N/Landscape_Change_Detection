# California Lake Landscape Change Detection

## Project Overview

This project aims to assess landscape changes around various lakes in California over approximately 5 years. Utilizing the power of Python and advanced image-processing AI tools, the project focuses on detecting significant changes in the landscapes of these lakes. The primary goal is to quantify and visualize the environmental changes that have occurred, providing insights into the effects of climate change, human activities, or natural factors on these ecosystems.

## How It Works

The project uses a set of images of different lakes in California, captured at two different points in time (approximately 5 years apart). Each lake has a pair of images: one representing the 'Before' state and another showing the 'After' state. The Python script processes these images to detect and highlight changes in the landscape.

Key features of the project include:
- Image processing to handle differences in image sizes and formats.
- Change detection to identify areas in the landscape that have changed over the years.
- Visual representation of changes with highlighted areas.
- Calculation of the percentage of change for each lake, providing a quantitative measure of the change.

## Setup and Usage

### Prerequisites
- Python 3.7.0+
- Libraries: OpenCV, NumPy, Matplotlib

### Installation
1. Clone the repository or download the source code.
2. Install the required Python libraries:
   ```bash
   pip install opencv-python numpy matplotlib

### Running the Script
1. Place the 'Before' and 'After' images of each lake in the 'images' folder. Ensure that the images are named according to the format: LakeName_Before.filetype and LakeName_After.filetype.
2. Run the script motion.py:
    ```bash
    python3 motion.py

### Contributing
Contributions to this project are welcome. Please feel free to fork the repository and submit pull requests.

### License
This project is open-sourced under the MIT License.


### Acknowledgements
Special thanks to KTLA 5 news website for their images.
Images linked: https://ktla.com/news/local-news/before-and-after-satellite-imaging-shows-californias-reservoir-levels-over-time/
Source used for educational and non-profit use only!
