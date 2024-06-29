import cv2

# Specify the image file name (assuming it's in the same directory as this script)
image_file = "example.jpg"

# Read the image
image = cv2.imread(image_file)

# Check if the image file exists
if image is None:
    print(f"Error: Image file '{image_file}' not found in the current directory.")
    exit()

# Calculate the desired pixel dimensions for 2x2 inches (assuming 300 DPI)
desired_width = int(2 * 300)  # 2 inches * 300 DPI
desired_height = int(1.5 * 300) # 2 inches * 300 DPI

# Resize the image to the desired dimensions
resized_image = cv2.resize(image, (desired_width, desired_height))

# Display the resized image
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
