# -*- coding: utf-8 -*-
"""
Created on Tue May 27 11:23:57 2025

@author: DELL
"""

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, filters, measure, morphology
from skimage.segmentation import clear_border
import pandas as pd
import plotly.express as px
from Bio import SeqIO  # Keep this if you plan to parse FASTA later; otherwise, can be removed

# --- Load 2D image (e.g. PNG) ---
image_2d = io.imread("replication_foci.png", as_gray=True)

# --- Preprocess and segment foci ---
def segment_foci(image):
    threshold = filters.threshold_otsu(image)
    binary = image > threshold
    binary = morphology.remove_small_objects(binary, min_size=50)
    binary = clear_border(binary)
    return binary

# --- Extract quantitative features ---
def extract_features(image, binary_mask):
    labeled = measure.label(binary_mask)
    props = measure.regionprops_table(
        labeled,
        intensity_image=image,
        properties=['label', 'area', 'mean_intensity', 'centroid']
    )
    return pd.DataFrame(props)

# --- Run segmentation and extraction ---
binary_mask = segment_foci(image_2d)
features_df = extract_features(image_2d, binary_mask)

# --- Visualization in 3D (z-axis shows area as height) ---

import plotly.io as pio
pio.renderers.default = 'browser'  # Open figure in browser

fig = px.scatter_3d(
    features_df,
    x="centroid-0",
    y="centroid-1",
    z="area",
    color="mean_intensity",
    size="area",
    title="Replication Foci Features (No Genomic Overlap)"
)
fig.show()

# --- Optional: Export to CSV ---
features_df.to_csv("replication_foci_features.csv", index=False)
