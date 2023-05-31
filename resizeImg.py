from PIL import Image
import os

input_directory = "/home/taylor/Insync/taylor7337@byui.edu/OneDrive Biz/Images/Crock Pot"
output_directory = "/home/taylor/Insync/taylor7337@byui.edu/OneDrive Biz/NewImages/crock_pot"
max_width = 500
max_height = 700

for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        input_path = os.path.join(input_directory, filename)
        encoded_filename = filename.encode('utf-8')
        decoded_filename = encoded_filename.decode('utf-8')

        image = Image.open(input_path)

        width, height = image.size
        if width > max_width or height > max_height:
            aspect_ratio = width / height
            new_height = min(height, max_height)
            new_width = int(new_height * aspect_ratio)
            if new_width > max_width:
                new_width = max_width
                new_height = int(new_width / aspect_ratio)

            resized_image = image.resize((new_width, new_height))
            resized_image = resized_image.convert("RGB")
            output_path = os.path.join(output_directory, decoded_filename)
            resized_image.save(output_path)
        else:
            output_path = os.path.join(output_directory, decoded_filename)
            image = image.convert("RGB")  # Convert the image to 'RGB' mode
            image.save(output_path)


