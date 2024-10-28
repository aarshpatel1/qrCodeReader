import cv2

# Load the QR Code detector
detector = cv2.QRCodeDetector()

# Read the image with the QR code
image = cv2.imread('qr.png')

# Detect and decode the QR code
data, vertices_array, _ = detector.detectAndDecode(image)

# If there is a QR code
if vertices_array is not None:
    print(f"QR Code data: {data}")
else:
    print("No QR Code detected.")
