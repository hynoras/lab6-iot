import requests
import base64
from picamera2 import Picamera2
import time

# Function to encode image to Base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image

url = 'http://172.31.10.20:8000/recog'

picam2 = Picamera2()
picam2.start()
time.sleep(2)  # Allow the camera to warm up
picam2.capture_file('Dataset/raw/vinhquang/libimage.png')
picam2.stop()
print("Image captured and saved to Dataset/raw/vinhquang/libimage.png")

image_path = 'Dataset/raw/vinhquang/libimage.png'
encoded_image_data = encode_image_to_base64(image_path)

# Parameters to send in the POST request
data = {
    'image': encoded_image_data,
    'w': 100,  # width
    'h': 100   # height
}

# Record the start time
start_time = time.time()

# Sending the POST request
response = requests.post(url, data=data)

# Record the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Printing the response
print("Response from server:")
print(response.text)
print(f"Total time taken for identification: {total_time:.2f} seconds")