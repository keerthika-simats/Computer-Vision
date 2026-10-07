import cv2

# Read the image
img = cv2.imread("image.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image not found")
else:
    # Display original image
    cv2.imshow("Original Image", img)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display grayscale image
    cv2.imshow("Grayscale Image", gray)

    # Save grayscale image
    cv2.imwrite("gray_image.jpg", gray)

    print("Image converted to grayscale successfully.")

    # Wait for a key
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()