from PIL import Image
import os 
import shutil
import logging

input_folder = "./input"
output_folder = "./output"

def convert_images_to_webp(input_folder, output_folder): 
    for foldername, subfolder, filenames in os.walk(input_folder):
        rel_folder = os.path.relpath(foldername, input_folder)
        new_folder = os.path.join(output_folder, rel_folder)
        os.makedirs(new_folder, exist_ok=True)

        for filename in filenames:
            file_path = os.path.join(foldername, filename)

            if filename.lower().endswith(('.jpg', '.jpeg')):
                try: 
                    with Image.open(file_path) as img:
                        webp_path = os.path.join(new_folder, os.path.splitext(filename)[0] + ".webp")
                        img.save(webp_path, "WEBP")
                        print(f'Конвертировано {file_path} -> {webp_path}')
                except Exception as e: 
                    logging.fatal(f"Reading error {file_path}: {e}")
            else: 
                logging.error(f'File passed {file_path}')

convert_images_to_webp(input_folder, output_folder)
