import requests
from io import BytesIO
from PIL import ImageTk, Image


def xuly_image(url, dai: int, rong: int):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = image.resize((dai, rong))  # Thay đổi kích thước ảnh
    photo = ImageTk.PhotoImage(image)
    return photo
