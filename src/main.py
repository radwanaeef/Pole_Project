import os
from detect_accessories import detect_accessories
from extract_gps import extract_gps
from save_excel import save_to_excel
from datetime import datetime

IMAGE_DIR = "../pole_project/data/dataset"

def run_pipeline():
    all_rows = []

    inspection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for file in os.listdir(IMAGE_DIR):
        if not file.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        image_path = os.path.join(IMAGE_DIR, file)
        print(f"\n🔍 Processing {file}")

        # Accessories
        accessories = detect_accessories(image_path)

        # GPS
        lat, lon = extract_gps(image_path)

        row = {
            "image_name": file,
            "latitude": lat,
            "longitude": lon,
            "inspection_time": inspection_time
        }

        # Add each detected accessory as a column
        for name, count in accessories.items():
            row[name] = count

        all_rows.append(row)


    save_to_excel(all_rows)

if __name__ == "__main__":
    run_pipeline()
