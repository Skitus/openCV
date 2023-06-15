import cv2
import numpy as np
import sys

def stitch_images(file_paths):
    # Read the images
    images = [cv2.imread(file) for file in file_paths]
    print('1')
    # Check if images are loaded
    for i in range(len(images)):
        if images[i] is None:
            print('ERROR: Image ', file_paths[i], ' could not be read')
            exit()
    print('14')
    # Detect and describe features
    sift = cv2.SIFT_create()
    keypoints = []
    descriptors = []
    for image in images:
        kp, des = sift.detectAndCompute(image, None)
        keypoints.append(kp)
        descriptors.append(des)
    print('23')
    print('descriptors', descriptors)
    print('keypoints', keypoints)
    print('keypoints end')
    # Match features
    try:
        # Match features
        matcher = cv2.BFMatcher(cv2.NORM_L2)
        raw_matches = matcher.knnMatch(descriptors[0], descriptors[1], k=2)
    except Exception as e:
        print(e)

    print('27')
    # Filter matches
    good_matches = [m for m, n in raw_matches if m.distance < 0.7 * n.distance]
    print('30')
    # Compute homography
    src_pts = np.float32([keypoints[0][m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([keypoints[1][m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    print('34')
    M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    print('36')
    # Apply homography and stitch images
    result = cv2.warpPerspective(images[0], M, (images[0].shape[1] + images[1].shape[1], images[0].shape[0]))
    print('39')
    result[0:images[1].shape[0], 0:images[1].shape[1]] = images[1]
    print('result', result)
    cv2.imwrite('./result.jpg', result)

if __name__ == "__main__":
    # List of image file paths
    image_paths = ['/home/artur/Downloads/2/1.jpg','/home/artur/Downloads/2/2.jpg']
    
    # Call the function
    stitch_images(image_paths)