import cv2
import easyocr
import re
import os


def extract_gps(image_path):
    print("Looking for:", os.path.abspath(image_path))
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found")

    h, w, _ = img.shape

    # Crop bottom-right corner (adjust if needed)
    crop = img[int(h * 0.8):h, 0:int(w * 0.4)]

    # OCR
    reader = easyocr.Reader(['en'],gpu=False)
    text_list = reader.readtext(crop, detail=0)

    full_text = " ".join(text_list)
    print("OCR TEXT:", full_text)

    ''' # Regex for latitude & longitude
    numbers = re.findall(r'-?\d+\.\d+', full_text)

    latitude = numbers[0] if len(numbers) >= 1 else None
    longitude = numbers[1] if len(numbers) >= 2 else None

    return latitude, longitude'''

    # Extract ALL decimal numbers
    numbers = [float(n) for n in re.findall(r'-?\d+\.\d+', full_text)]

    latitude, longitude = None, None

    # Find valid GPS pair
    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i + 1]

        if -90 <= a <= 90 and 30 <= b <= 180:
            latitude, longitude = a, b
            break

    return latitude, longitude


'''# Run directly (for testing)
if __name__ == "__main__":
    lat, lon = extract_gps("../pole_project/test_images/latlonext.jpeg")
    print("Latitude:", lat)
    print("Longitude:", lon)'''

if __name__ == "__main__":
    image_dir = "../pole_project/test_images/geo_images"

    for file in os.listdir(image_dir):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(image_dir, file)
            print("\nTesting:", file)

            lat, lon = extract_gps(path)

            if lat and lon:
                print(f"✅ Latitude: {lat}, Longitude: {lon}")
            else:
                print("❌ GPS not found")