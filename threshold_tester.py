import cv2
import matplotlib.pyplot as plt
import argparse
""""
Program for finder min and max threshold for edge detection
"""
def test_edges(file, min, max):
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
    #print(f"Min: {min} \n Max: {max} \n")
    plt.imshow(image)
    plt.title(f"Min: {min} \n Max: {max} \n")
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image")
    parser.add_argument("min_thresh")
    parser.add_argument("min_thresh_inc")
    parser.add_argument("max_thresh")
    parser.add_argument("max_thresh_inc")

    args = parser.parse_args()

    for min in range(0, int(args.min_thresh)+1, int(args.min_thresh_inc)):
        for max in range(0, int(args.max_thresh)+1, int(args.max_thresh_inc)):
            if max <= min:
                continue
            else:
                test_edges(args.image, min, max)
