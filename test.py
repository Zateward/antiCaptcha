import pytesseract
import cv2

# Read the captcha image
image = cv2.imread("test.jpg")

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not load the image.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binarize the image
    thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # Perform OCR on the image
    text = pytesseract.image_to_string(thresh)

    # Print the OCR output
    print(text)
