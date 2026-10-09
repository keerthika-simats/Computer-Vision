import cv2

# Read the image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Rotate the image 180 degrees
    rotated = cv2.rotate(img, cv2.ROTATE_180)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image - 180 Degrees", rotated)

    # Save the rotated image
    cv2.imwrite("rotated_180_image.jpg", rotated)

    print("Image rotated successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()