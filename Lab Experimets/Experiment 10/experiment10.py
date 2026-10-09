import cv2

# Read the image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Rotate the image 90 degrees clockwise
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Display the original and rotated images
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image - 90 Degrees Clockwise", rotated)

    # Save the rotated image
    cv2.imwrite("rotated_image.jpg", rotated)

    print("Image rotated successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()