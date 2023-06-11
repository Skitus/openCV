import cv2
import sys

def stitch_images(file_paths):
    print('files inside python', file_paths)
    # Read the images from the files
    images = [cv2.imread(fp) for fp in file_paths]
    print('images inside python', images)
    
    # Create a Stitcher class
    stitcher = cv2.Stitcher_create()

    # Use the stitcher to stitch the images
    status, result = stitcher.stitch(images)
    print('status', status)
    # If the status is OK (0), write the result to a file
    if status == cv2.Stitcher_OK:
        cv2.imwrite('./ortophoto.jpg', result)
    else:
        print('Error during stitching, status code =', status)

if __name__ == "__main__":
    # Get the file paths from the command line arguments
    file_paths = sys.argv[1:]

    # Call the function to stitch the images
    stitch_images(file_paths)
