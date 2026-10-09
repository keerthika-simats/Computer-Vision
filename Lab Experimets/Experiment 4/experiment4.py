import cv2

# Read the image
img = cv2.imread("image.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Display the original grayscale image
    cv2.imshow("Original Grayscale Image", gray)

    # Display the histogram equalized image
    cv2.imshow("Histogram Equalized Image", equalized)

    # Save the equalized image
    cv2.imwrite("equalized_image.jpg", equalized)

    print("Histogram equalization completed successfully!")

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()