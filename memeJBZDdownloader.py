
import requests
from bs4 import BeautifulSoup
import urllib.request
import random
from datetime import date

# -------------------------------------------
# Sources of memes
# -------------------------------------------

source1 = "https://jbzd.com.pl/str/1"
source2 = "https://jbzd.com.pl/str/2"
source3 = "https://jbzd.com.pl/str/3"
source4 = "https://jbzd.com.pl/str/4"
source5 = "https://jbzd.com.pl/str/5"
source6 = "https://jbzd.com.pl/str/6"
source7 = "https://jbzd.com.pl/str/7"
# -------------------------------------------



# -------------------------------------------
# Prints
# -------------------------------------------


emoji1time = "\U0001F606"
emoji = "\U0001F606""\U0001F606""\U0001F606""\U0001F606""\U0001F606""\U0001F606""\U0001F606""\U0001F606""\U0001F606""\U0001F606"
breakPrint = "===================="


# -------------------------------------------
# Today date
# -------------------------------------------
today = date.today()
d1 = today.strftime("%d/%m/%Y")



# -------------------------------------------
# Print after download
# -------------------------------------------
print(breakPrint)
print(emoji)
print("Pobieranie memów".center(20))
print("z dnia:".center(20))
print(d1.center(20))
print(emoji)
print(breakPrint)

# -------------------------------------------
#   Main code
# -------------------------------------------


def memes(input):
 links=[input]
 for url in links:
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")

 for link in soup.find_all("img",{"class":"article-image"}):
    src = link.get('src')
    img_number = src[47:79]
    img_page = input[24]

    full_name = "MemeID_"+img_number+".jpg"


    urllib.request.urlretrieve(src, full_name)

# -------------------------------------------
# Downloading print
# -------------------------------------------

    img_numberInconsole1 = img_number[0:16]
    img_numberInconsole2 = img_number[16:32]



    print(breakPrint)
    print("....................")
    print(". Pobieram memy !  .")
    print(".Ze strony JBZD.PL .")
    print("........"+emoji1time+"..........")
    print("....................")
    print("......Strona:.......")
    print("........["+img_page+"].........")
    print("....................")
    print("......ID mema:......")
    print(".["+img_numberInconsole1+"].")
    print(".["+img_numberInconsole2+"].")
    print("....................")
    print(breakPrint)
    # print(".......Źródło:......")
    # print("."+src+".")
    # print("....................")


# -------------------------------------------


# -------------------------------------------
# Function using sorce
# -------------------------------------------


memes(input=source1)
memes(input=source2)
memes(input=source3)
memes(input=source4)
memes(input=source5)
memes(input=source6)
memes(input=source7)


# -------------------------------------------
# Pring after download
# -------------------------------------------

print(emoji)
print(breakPrint)
print("Pobieranie memów".center(20))
print("ZAKOŃCZONE".center(20))
print(breakPrint)
print(emoji)
print(breakPrint)
print("PAAA".center(5))
print("PAAA".center(10))
print("PAAA".center(15))
print("PAAA".center(20))
print("PAAA".center(25))
print("PAAA".center(30))
print(breakPrint)
print(emoji)
print(breakPrint)

# -------------------------------------------

# test