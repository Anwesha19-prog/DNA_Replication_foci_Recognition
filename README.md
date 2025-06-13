# DNA_Replication_foci_Recognition

**Author
Anwesha Sarkar**

# eplication Foci Analysis Toolkit (2D Microscopy Images)

This project is a simple Python-based pipeline to analyze DNA replication foci from grayscale 2D microscopy images (e.g., PNG or TIFF format). It performs segmentation of foci, extracts relevant spatial features, and generates an interactive 3D plot for visual exploration.

---

## Features

- Load 2D grayscale microscopy images
- Segment replication foci using Otsu thresholding
- Extract features such as area, intensity, and position
- Visualize results in an interactive 3D scatter plot
- Export data to CSV for downstream analysis

---

## Requirements

Install required libraries with:

```bash
pip install numpy matplotlib scikit-image plotly pandas biopython

----

**Input**
A single grayscale PNG image file named:

replication_foci.png


This image should contain clearly visible replication foci (bright spots).

**If your image is RGB, it will be automatically converted to grayscale**

----

**How to Run the Script**
Save your image as replication_foci.png in the project directory.

Run the Python script:

python analyze_replication_foci.py

----

**Output**
A 3D interactive scatter plot of replication foci will open in your web browser.

A CSV file called replication_foci_features.csv will be created, containing:

label	area	mean_intensity	centroid-0	centroid-1
1	120	0.84	105.2	310.3
2	98	0.79	250.7	390.1
...	...	...	...	...

-----

**Test with Simulated Data (No Real Image Required)**
Paste the code below into a Python script to generate a fake sample image:
from skimage.draw import disk
import numpy as np
from skimage.io import imsave

img = np.zeros((512, 512), dtype=np.uint8)

# Simulated circular foci
for center in [(100, 100), (300, 200), (400, 400)]:
    rr, cc = disk(center, 20)
    img[rr, cc] = 255

imsave("replication_foci.png", img)
Then run the main script to test it.
 -----
**Notes** 
This version supports 2D single-slice images only.

Future extensions could support 3D stacks, time-lapse, or chromatin/genome integration.

Designed for early prototyping and reproducible analysis.

