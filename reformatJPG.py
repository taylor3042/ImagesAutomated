import PIL
from PIL import Image
import os
import sys

# Set the directory containing the images
search_term = sys.argv[1]
image_directory = "/home/taylor/Insync/taylor7337@byui.edu/OneDrive Biz/Images/" + search_term

# Iterate over the files in the directory
for filename in os.listdir(image_directory):
    # Check if the file is an image
    image_path = os.path.join(image_directory, filename)
    #print(image_path)
    # Skip if the file is already a JPEG or matches the specific filename
    if (filename.lower().endswith((".jpg", ".jpeg"))) and filename != "AOLn63Him4p6m99L2fmZ0_mabqSoxg9_qFj8ILrXgJtcggs64-c-mo.jpg":
        print(f"Skipping {filename} (already a JPEG)")
        continue

    # Check if "vector", "192px", or "AOLn63Him" is present in the filename
    if "vector" in filename or "192px" in filename or "AOLn63Him" in filename:
        # Remove the file
        os.remove(image_path)
        print(f"Deleted {filename}")
        continue

    try:
        # Try opening the image with PIL
        image = Image.open(image_path)
        image.verify()  # Verify the image file integrity
    except (OSError, PIL.UnidentifiedImageError) as e:
        print(f"Error processing {filename}: {str(e)}")
        os.remove(image_path)  # Delete the file if opening fails
        print(f"Removed {filename}")
        continue

    try:
        if filename.lower().endswith(".png"):
            try:
                # Convert the PNG to JPEG
                image = image.convert("RGB")
                new_filename = os.path.splitext(filename)[0] + ".jpg"
                new_image_path = os.path.join(image_directory, new_filename)
                image.save(new_image_path, "JPEG")

                print(f"Converted {filename} to {new_filename}")
            except AttributeError as e:
                print(f"Error converting {filename} from PNG to JPEG: {str(e)}")
            finally:
                os.remove(image_path)  # Delete the PNG file whether conversion succeeds or fails
                print(f"Removed {filename}")
                continue
        elif filename.lower().endswith(".gif"):
            try:
                # Convert the GIF to JPEG
                with Image.open(image_path) as gif:
                    gif.seek(0)  # Seek to the first frame
                    gif.convert("RGB").save(image_path.replace(".gif", ".jpg"), "JPEG")
                    print(f"Converted {filename} to {filename.replace('.gif', '.jpg')}")
            except (OSError, PIL.UnidentifiedImageError) as e:
                print(f"Error converting {filename} from GIF to JPEG: {str(e)}")
            finally:
                os.remove(image_path)  # Delete the GIF file whether conversion succeeds or fails
                print(f"Removed {filename}")
                continue
        elif filename.lower().endswith(".webp"):
            try:
                # Convert the WebP to JPEG
                image = image.convert("RGB")
                new_filename = os.path.splitext(filename)[0] + ".jpg"
                new_image_path = os.path.join(image_directory, new_filename)
                image.save(new_image_path, "JPEG")
                print(f"Converted {filename} to {new_filename}")
            except (OSError, PIL.UnidentifiedImageError) as e:
                print(f"Error converting {filename} from WebP to JPEG: {str(e)}")
            finally:
                os.remove(image_path)  # Delete the WebP file whether conversion succeeds or fails
                print(f"Removed {filename}")
                continue
        elif filename.lower().endswith(".jfif"):
            try:
                # Convert the WebP to JPEG
                image = image.convert("RGB")
                new_filename = os.path.splitext(filename)[0] + ".jpg"
                new_image_path = os.path.join(image_directory, new_filename)
                image.save(new_image_path, "JPEG")
                print(f"Converted {filename} to {new_filename}")
            except (OSError, PIL.UnidentifiedImageError) as e:
                print(f"Error converting {filename} from jfif to JPEG: {str(e)}")
            finally:
                os.remove(image_path)  # Delete the jfif file whether conversion succeeds or fails
                print(f"Removed {filename}")
                continue
    except (OSError, PIL.UnidentifiedImageError) as e:
        print(f"Error saving {new_filename}: {str(e)}")

    # Close the image
    image.close()


