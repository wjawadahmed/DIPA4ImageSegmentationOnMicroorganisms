# Classical Image Segmentation on Microorganisms

**Digital Image Processing (CEN-444) – Group Project**

## Group Members

* **Wazir Jawad Ahmed**
* **Abdul Hadi**
* **Jaleel Haider**
* **Abdul Sattar**

**Department:** Computer Science
**University:** Bahria University, Islamabad

---

## Project Overview

This project implements a collection of **classical image segmentation algorithms** using **Python**.
The goal is to analyze and compare different **Digital Image Processing (DIP)** techniques for segmenting microorganism images.

The project demonstrates practical application of:

* Image preprocessing
* Thresholding
* Edge detection
* Clustering
* Morphological and region-based segmentation

---

## Segmentation Algorithms Implemented

The following algorithms are included in this project:

1. **Fast Marching Segmentation**
   Implemented using **SimpleITK** for region-based segmentation.

2. **Threshold Segmentation**
   Global thresholding using **OpenCV**.

3. **Canny Edge Detection**
   Edge-based segmentation using gradient information.

4. **Contour Detection**
   Object boundary extraction using OpenCV contours.

5. **K-Means Segmentation**
   Clustering-based image segmentation.

6. **Watershed Segmentation**
   Marker-based region separation technique.

Each algorithm is implemented in a **separate Python file** for clarity and modular design.

---

## Folder Structure (Base Directory)

**Base Folder Path:**

```
D:\DIPASSIGNMENT4\ImageSegmentationOnMicroorganisms
```

Key folders include:

* `input_images/` – Test images
* `segmentation_results/` – Output results
* `main.py` – Main execution file
* Individual `.py` files for each algorithm

---

## Usage Instructions

Follow the steps below to run the project:

### 1. Navigate to the project directory

```bash
cd D:\DIPASSIGNMENT4\ImageSegmentationOnMicroorganisms
```

### 2. Install required dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the main program

```bash
python main.py
```

---

## Results Visualization

The project generates segmented outputs for each algorithm using the same input images.
Results are stored in the **segmentation_results** folder and allow visual comparison of different techniques.

These results help evaluate:

* Accuracy of segmentation
* Boundary detection quality
* Noise sensitivity of each method

---

## Applications

The implemented segmentation techniques can be applied in:

* Medical image analysis
* Microorganism detection
* Object extraction
* General image processing tasks

---

## References

* OpenCV – [https://opencv.org/](https://opencv.org/)
* SimpleITK – [https://simpleitk.org/](https://simpleitk.org/)

---

**Note:**
This project is developed as part of the **CEN-444 Digital Image Processing course** and focuses on **classical DIP techniques**, not deep learning.
