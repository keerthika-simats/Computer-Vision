import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(gray, kernel, iterations=1)

    # Display original and dilated images
    cv2.imshow("Original Grayscale Image", gray)
    cv2.imshow("Dilated Image", dilated)

    # Save the dilated image
    cv2.imwrite("dilated_image.jpg", dilated)

    print("Image dilation completed successfully!")

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()