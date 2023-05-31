import os
import sys
import time
import urllib.parse
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Set the search keyword
search_term = sys.argv[1]

# Set Firefox options
options = Options()
options.add_argument('--headless')

# Set the directory path to save the images
save_directory = "/home/taylor/Insync/taylor7337@byui.edu/OneDrive Biz/NewImages/" + search_term
if not os.path.exists(save_directory):
    os.mkdir(save_directory)
    print("Creating directory...")
else:
    print("Directory already exists")

# Create a new Firefox browser instance
browser = webdriver.Firefox(options=options)

# Navigate to Google Images
browser.get("https://www.google.com/imghp")

# Locate the search box element
search_box = browser.find_element(By.NAME, "q")

# Type the search term into the search box and submit
search_box.send_keys(search_term)
search_box.send_keys(Keys.RETURN)

# Scroll down to load more images
scroll_pause_time = 8  # Adjust the pause time between scrolls as needed
last_height = browser.execute_script("return document.body.scrollHeight")
print(last_height)
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img.rg_i")))
    time.sleep(scroll_pause_time)

    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find all image elements
images = browser.find_elements(By.CSS_SELECTOR, "img.rg_i")

# Set the number of images to download (modify this as needed)
num_images_to_download = 500

# Iterate over the images
downloaded_images = 0
for i, image in enumerate(images):
    if downloaded_images >= num_images_to_download:
        break

    image_url = image.get_attribute("src")

    try:
        response = urllib.request.urlopen(image_url, timeout=20)
    except Exception as e:
        print(f"Failed to download image {i}: {e}")
        continue

    if response is None:
        print(f"Failed to download image {i}: Response is None")
        continue

    try:
        image_data = response.read()
    except Exception as e:
        print(f"Failed to read image data {i}: {e}")
        continue

    # Extract the file extension from the image URL
    parsed_url = urllib.parse.urlparse(image_url)
    filename, extension = os.path.splitext(parsed_url.path)

    # Generate a unique filename using the image index and file extension
    filename = f"{search_term}_{i}{extension}"

    save_path = os.path.join(save_directory, filename)

    try:
        with open(save_path, "wb") as f:
            f.write(image_data)
        print(f"Downloaded image {filename}")
        downloaded_images += 1
    except Exception as e:
        print(f"Failed to save image {filename}: {e}")

# Close the browser
browser.quit()

