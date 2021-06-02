from instabot import Bot
import os
import requests
import time

USER = 'woodworkmaniacs'
PASS = '2s8a9cuz'

response = requests.get('https://zenquotes.io/api/random')
data = response.json()
caption = data[0]['q']
bot = Bot()
bot.login(username=USER, password=PASS)
destinations = []


def rename_files(folder):
    for count, filename in enumerate(os.listdir(folder)):
        dst = str(count) + ".jpg"
        src = 'images/' + filename
        dst = 'images/' + dst
        destinations.append(dst)
        # rename() function will
        # rename all the files
        os.rename(src, dst)


def upload_image():
    for des in destinations:
        bot.upload_photo(des, caption=caption)
        time.sleep(86400 / 6)


rename_files('images')
upload_image()
