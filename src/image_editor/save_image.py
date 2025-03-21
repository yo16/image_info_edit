# 画像を保存する

import os
from PIL import Image



# JPG 画像として保存する
def save_image_as_jpg(
    image: Image.Image,
    file_path: str
):
    # 画像を保存
    image.save(file_path, "jpeg")

