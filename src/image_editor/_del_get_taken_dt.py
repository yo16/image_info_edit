# Exif 情報から撮影日時を取得する

import piexif
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime


def get_taken_dt(
    image: Image.Image
):
    # Exif 情報を取得
    exif = image.getexif()
    
    # 撮影日時を取得
    taken_dt = datetime(2025, 3, 2, 10, 0, 0)   # exif 情報がない場合のデフォルト値
    if exif:
        # DateTimeOriginalのタグID（0x9003）
        datetime_original = exif.get(0x9003)
        if (datetime_original):
            exif_datetime_str = datetime_original.decode("utf-8")
            #print(exif_datetime_str)  # 2025:03:02 10:33:54
            
            # 撮影日時を datetime に変換
            taken_dt = datetime.strptime(exif_datetime_str, "%Y:%m:%d %H:%M:%S")
    else:
        print(f"W: Exif 情報がありません")

    return taken_dt


