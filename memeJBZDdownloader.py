import requests
from bs4 import BeautifulSoup
import urllib.request
from datetime import date
import os

# Source URLs for memes
sources = ["https://jbzd.com.pl/str/{}".format(i) for i in range(1, 8)]

# Separator for printing
separator = "=" * 20

# Today's date
today = date.today()
date_folder = today.strftime("%Y-%m-%d")
folder_name = f"{date_folder} - MEMES"

# Create folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Function to download memes
def download_memes(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")

    for link in soup.find_all("img", {"class": "article-image"}):
        image_src = link.get("src")
        meme_id = image_src.split("/")[-1][:-4]
        page_number = url.split("/")[-1]

        image_name = os.path.join(folder_name, f"MemeID_{meme_id}.jpg")

        if not os.path.exists(image_name):
            try:
                urllib.request.urlretrieve(image_src, image_name)
                print("{}\n"
                      ".... Downloading memes! ...\n"
                      "From JBZD.PL\n"
                      "Page: [{}]\n"
                      "Meme ID: [{}]\n"
                      "         [{}]\n"
                      "{}\n".format(separator, page_number, meme_id[:16], meme_id[16:32], separator))
            except Exception as e:
                print("Error occurred while downloading meme: {}".format(str(e)))
        else:
            print("File '{}' already exists. Skipping download.".format(image_name))

# Download memes from each source
for source in sources:
    download_memes(source)

# Print after download
print("\n{}\n"
      "Meme Download\n"
      "COMPLETED\n"
      "{}\n".format(separator, separator))

