import cv2
import numpy as np

def stitch_images(file_paths):
    # Read the images
    images = [cv2.imread(file) for file in file_paths]

    # Check if images are loaded
    for i, image in enumerate(images):
        if image is None:
            print(f'ERROR: Image {file_paths[i]} could not be read')
            return

    # Initialize OpenCV's image sticher object and then perform the image
    # stitching
    print("[INFO] stitching images...")
    stitcher = cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)

    # if the status is '0', then OpenCV successfully performed image
    # stitching
    if status == 0:
        # write the output stitched image to disk
        cv2.imwrite('./result.jpg', stitched)
        print("[INFO] image stitching successful")

    # otherwise the stitching failed, likely due to not enough keypoints)
    # being detected
    else:
        print("[INFO] image stitching failed ({})".format(status))


if __name__ == "__main__":
    # List of image file paths
    image_paths = ['/home/artur/Downloads/2/1.jpg', '/home/artur/Downloads/2/2.jpg']
    # Call the function
    stitch_images(image_paths)
