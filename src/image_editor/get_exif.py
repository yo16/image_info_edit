# Exif 情報から、後に必要な情報を取得する
# 存在しない場合は、None を返す
# 取得できる情報は、以下の通り
# - 撮影日時(taken_dt)
# - 回転情報(orientation)

import piexif
from PIL import Image
from typing import Union
from pillow_heif import HeifFile
from datetime import datetime



def get_exif(
    image: Union[Image.Image, HeifFile]
) -> dict:
    taken_dt = None
    orientation = None

    # Exif 情報を取得
    exif_data = image.info.get("exif")
    exif_dict = None
    if exif_data:
        exif_dict = piexif.load(exif_data)

    # 撮影日時を取得
    exif_datetime_str = None
    if exif_dict:
        taken_dt_bin = exif_dict["Exif"].get(piexif.ExifIFD.DateTimeOriginal)

        if taken_dt_bin:
            exif_datetime_str = taken_dt_bin.decode("utf-8")
            # 撮影日時を datetime に変換
            taken_dt = datetime.strptime(exif_datetime_str, "%Y:%m:%d %H:%M:%S")
    
    # 回転情報を取得
    if exif_dict:
        orientation = exif_dict["0th"].get(piexif.ImageIFD.Orientation)
    
    #print(taken_dt)
    #print(exif_datetime_str)
    #print("orientation")
    #print(orientation)

    return {
        "taken_dt": taken_dt,
        "taken_dt_str": exif_datetime_str,
        "orientation": orientation
    }
    

