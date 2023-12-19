import easyocr
import matplotlib.pyplot as plt
import cv2

# Function to load and process the image
def load_and_process_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to RGB (EasyOCR requires RGB format)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image_rgb

# Function to draw bounding boxes and text on the image
def draw_boxes_on_image(image, detections):
    for detection in detections:
        # Extract coordinates and text from detection
        top_left = tuple(map(int, detection[0][0]))
        bottom_right = tuple(map(int, detection[0][2]))
        text = detection[1]

        # Draw bounding boxes and text on the image
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 5)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, text, top_left, font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    return image

# Load the EasyOCR reader
reader = easyocr.Reader(['en'])  # You can specify multiple languages here

# Path to your image file
image_path = r'C:\Users\srita\Downloads\drdo project\EasyOCR\durf.png'

# Load and process the image
image_rgb = load_and_process_image(image_path)

# Use EasyOCR to extract text
result = reader.readtext(image_rgb)

# Draw bounding boxes and text on the image
image_with_boxes = draw_boxes_on_image(image_rgb.copy(), result)

# Display the image with detected text
plt.figure(figsize=(10, 10))
plt.imshow(image_with_boxes)
plt.axis('off')  # Hide axis
plt.show()
