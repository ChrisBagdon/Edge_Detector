import argparse
import cv2
import os
import matplotlib.pyplot as plt

"""
Program to find edges in image files and create new images with edges highlighted. 

Args:
Input file Directory: String:Path
Output file Directory String:Path
Minimum threshold for edge detection Int
Maximum threshold for edge detection Int

Written by Christopher Bagdon - 08/21
"""
def write_edges(file, min, max, output):
    """
    Finds edges of image, writes them over top in blue in new image file
    :param file: Image to find edges from
    :param min: Minimum threshhold for edge detection
    :param max: Maximum threshhold for edge detection
    :param output: Filename of new image
    """
    # Read in image
    image = cv2.imread(file)
    # Convert to grayscale
    g_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Generate edges using canny
    edges = cv2.Canny(g_image, min, max)
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

    for file in os.listdir(args.image_dir):
        if file.endswith(".png") or file.endswith(".jpg"):
            output = args.output_dir + file[:-4] + "_edged" + file[-4:]
            input = args.image_dir + file
            try:
                write_edges(input, int(args.min_thresh), int(args.max_thresh), output)
            except:
                print(f"{file} could not have edges written to")
                continue
