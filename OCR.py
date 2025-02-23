import os
import numpy as np
from PIL import Image
import requests
import cv2
import json
from dotenv import load_dotenv

load_dotenv()
ocr_token = os.getenv("OCR_SPACE_API")

# Function to resize an image while maintaining aspect ratio
def resize(input_path, output_path, target_size=1 * 1024 * 1024):
    with Image.open(input_path) as img:
        img_format = img.format  # Preserve the original image format
        ratio = (target_size / os.path.getsize(input_path)) ** 0.5
        new_width = max(1, int(img.width * ratio))
        new_height = max(1, int(img.height * ratio))
        img = img.resize((new_width, new_height), Image.LANCZOS)
        img.save(output_path, quality=85, format=img_format)

# Function to check image size and resize if necessary
def size_check(image):
    if os.path.getsize(image) > 1 * 1024 * 1024:
        resized_path = "resized_" + os.path.basename(image)
        resize(image, resized_path)
        return resized_path
    return image

# Function to check image type and convert if it's a NumPy array
def type_check(image):
    if isinstance(image, np.ndarray):
        img = Image.fromarray(image)
        converted_path = "converted_image.jpg"
        img.save(converted_path)
        return converted_path
    return image

# Function to process the image (check type and size)
def deal_with_image(image_path):
    processed_image = type_check(image_path)
    return size_check(processed_image)

# Function to send an image to OCR.space API and retrieve text
def ocr_space_file(filename, language='eng'):
    payload = {
        'apikey': ocr_token,  # Replace with your API key
        'language': language,
        'isOverlayRequired': False
    }

    with open(filename, 'rb') as f:
        response = requests.post('https://api.ocr.space/parse/image',
                                 files={filename: f},
                                 data=payload)
    return response.content.decode()

# Function to extract text from an image
def ImageOCR(img):
    image = deal_with_image(img)
    json_format = ocr_space_file(image, language='eng')

    try:
        result_json = json.loads(json_format)
        parsed_results = result_json.get('ParsedResults', [])
        parsed_text = parsed_results[0].get('ParsedText', '') if parsed_results else ''
    except (json.JSONDecodeError, IndexError, AttributeError):
        parsed_text = 'there is something wrong'

    # Remove temporary files related to the process
    for file in ["resized_" + os.path.basename(img), "converted_image.jpg"]:
        if os.path.exists(file):
            os.remove(file)

    return parsed_text

# Function to extract text from a video using OCR on frames
def VideoOCR(video):
    OCR_for_frames = []
    cap = cv2.VideoCapture(video)

    frame_count = 0
    frame_skip = 10  # Process every 10th frame to reduce load

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_skip == 0:  # Skip some frames for better performance
            OCR_frame = ImageOCR(frame)
            OCR_for_frames.append(OCR_frame)

        frame_count += 1

    cap.release()
    return OCR_for_frames
