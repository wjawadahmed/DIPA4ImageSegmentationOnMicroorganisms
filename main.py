import os
import cv2
import matplotlib.pyplot as plt

from threshold_segmentation import threshold_segmentation
from canny_edge_detection import canny_edge_detection
from contour_detection import contour_detection
from kmeans_segmentation import kmeans_segmentation
from watershed_segmentation import watershed_segmentation

# Base directory (current project folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths to input images (relative paths)
img_paths = [
    os.path.join(BASE_DIR, 'test_data', 'EMDS5-g01-40.png'),
    os.path.join(BASE_DIR, 'test_data', 'EMDS5-g02-21.png')
]

# Output directory
output_dir = os.path.join(BASE_DIR, 'segmentation_results')
os.makedirs(output_dir, exist_ok=True)

# Segmentation functions
segmentation_functions = [
    ("Threshold Segmentation", threshold_segmentation),
    ("Canny Edge Detection", canny_edge_detection),
    ("Contour Detection", contour_detection),
    ("K-means Segmentation", kmeans_segmentation),
    ("Watershed Segmentation", watershed_segmentation)
]

results = []

for img_path in img_paths:
    img_name = os.path.splitext(os.path.basename(img_path))[0]
    img_results = []

    for seg_name, segmentation_func in segmentation_functions:
        segmented_img = segmentation_func(img_path)
        img_results.append((seg_name, segmented_img))

    results.append((img_name, img_results))

# Visualization
num_imgs = len(img_paths)
num_segs = len(segmentation_functions)

fig, axes = plt.subplots(num_imgs, num_segs, figsize=(16, 12))

for i, (img_name, img_results) in enumerate(results):
    for j, (seg_name, result) in enumerate(img_results):
        ax = axes[i, j] if num_imgs > 1 else axes[j]
        ax.imshow(result, cmap='gray')
        ax.axis('off')
        ax.set_title(seg_name)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'segmentation_results.png'))
plt.show()
