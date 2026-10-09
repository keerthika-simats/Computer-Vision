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

    # Detect edges using Canny
    edges = cv2.Canny(gray, 100, 200)

    # Display outline image
    cv2.imshow("Canny Outline Image", edges)

    # Save the outline image
    cv2.imwrite("outline_image.jpg", edges)

    print("Image outline detected successfully.")

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()