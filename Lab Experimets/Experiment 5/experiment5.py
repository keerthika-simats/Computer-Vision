import cv2
import matplotlib.pyplot as plt

# Function to analyze the color histogram
def analyze_histogram(image_path):
    # Read the input image
    img = cv2.imread(image_path)

    # Check whether the image is loaded
    if img is None:
        print("Error: Image not found!")
        return

    # Convert BGR image to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display the original image
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis("off")

    # Calculate histograms for Red, Green and Blue
    colors = ('r', 'g', 'b')
    channels = (2, 1, 0)

    plt.subplot(1, 2, 2)

    for color, channel in zip(colors, channels):
        histogram = cv2.calcHist(
            [img], [channel], None, [256], [0, 256]
        )

        plt.plot(histogram, color=color)

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.tight_layout()
    plt.show()

    print("Color histogram analysis completed successfully.")

# Call the function
analyze_histogram("image.jpg")