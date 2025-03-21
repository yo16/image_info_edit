# Exif情報に画像の回転情報がある場合は変更する
# Exif情報がない場合、またはあっても回転情報がない場合は、コピーして新しい `Image.Image` を返す

from PIL import Image
from PIL.ExifTags import TAGS
from typing import Union



def correct_orientation(
    img_original: Image.Image,
    orientation: Union[int, None]
):
    img = img_original.copy()

    # Orientation タグをベースにimgを修正
    if orientation:
        if orientation == 3:
            img = img.rotate(180, expand=True)
        elif orientation == 6:
            #img = img.rotate(270, expand=True)  # 反時計回り90度
            pass
        elif orientation == 8:
            img = img.rotate(90, expand=True)   # 時計回り90度
            
    return img
