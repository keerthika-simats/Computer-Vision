import cv2

# Read the image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Resize to a bigger size
    bigger = cv2.resize(img, None, fx=2, fy=2,
                        interpolation=cv2.INTER_LINEAR)

    # Resize to a smaller size
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5,
                         interpolation=cv2.INTER_AREA)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    # Save the resized images
    cv2.imwrite("bigger_image.jpg", bigger)
    cv2.imwrite("smaller_image.jpg", smaller)

    print("Image scaling completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()