import argparse
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def write_edges(file, min, max, output):
    # Read in image
    image = cv2.imread(file)
    # Convert to grayscale
    g_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Generate edges using canny
    edges = cv2.Canny(g_image, min, max)
    #figure, ax = plt.subplots(1, figsize=(12,8))
    # test edge detection
    plt.imshow(edges, cmap="Greys")
    # Find contours
    contours = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # Draw Contours on original image
    cv2.drawContours(image, contours[0], -1, (255,0,0), thickness=3)
    figure, ax = plt.subplots(1, figsize=(12, 8))
    plt.imshow(image)
    # Write to file
    cv2.imwrite(output, image)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_dir")
    parser.add_argument("output_dir")
    parser.add_argument("min_thresh")
    parser.add_argument("max_thresh")
    args = parser.parse_args()


