import cv2

# Read the image
img = cv2.imread("image.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image not found")
else:
    # Display original image
    cv2.imshow("Original Image", img)

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    # Display blurred image
    cv2.imshow("Gaussian Blur Image", blur)

    # Save the blurred image
    cv2.imwrite("blur_image.jpg", blur)

    print("Image blurred successfully.")

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()