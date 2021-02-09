import requests
from PIL import ImageTk, Image
import io


def get_avatar():
    p = requests.get("https://thispersondoesnotexist.com/image")
    img = p.content
    return img
