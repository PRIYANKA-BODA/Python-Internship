import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

# ------------------------
# 1. Move all .jpg files from a folder to a new folder
# ------------------------
def move_jpg_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(".jpg"):
            shutil.move(os.path.join(source_folder, file_name),
                        os.path.join(destination_folder, file_name))
    print("✅ All .jpg files moved successfully!")

# ------------------------
# 2. Extract all email addresses from a .txt file
# ------------------------
def extract_emails(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)
    with open(output_file, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\n")
    print(f"✅ Extracted {len(emails)} emails to {output_file}")

# ------------------------
# 3. Scrape the title of a fixed webpage
# ------------------------
def scrape_website_title(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string.strip() if soup.title else "No Title Found"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(title)
    print(f"✅ Website title saved to {output_file}: {title}")

# ------------------------
# Example usage
# ------------------------
if __name__ == "__main__":
    # Example 1: Move JPG files
    # move_jpg_files("source_folder_path", "destination_folder_path")

    # Example 2: Extract emails from text file
    # extract_emails("input.txt", "emails.txt")

    # Example 3: Scrape title of webpage
    # scrape_website_title("https://www.codealpha.tech", "title.txt")
    pass
