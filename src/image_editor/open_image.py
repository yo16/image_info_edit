# 画像ファイルを開く
# 拡張子ごとに、特別な開き方があることを想定して、関数を分けている
# 特に .HEIC だが、いま入手しているファイルでは、Image.open で開けることを確認しているのでそうしている
# dictで、Image.Imageと、exif情報を返す

import os
from PIL import Image
from pillow_heif import open_heif as pillow_open_heif

from .get_exif import get_exif


def open_image(
    file_path: str
) -> dict:
    # 拡張子を取得
    extension = os.path.splitext(file_path)[1].lower()
    
    # 画像ファイルを開く
    if extension == ".jpg":
        dict_image = open_jpg(file_path)
    elif extension == ".heic":
        dict_image = open_heic(file_path)
    elif extension == ".png":
        dict_image = open_png(file_path)
    else:
        # 登録されていない拡張子は、対応しない
        print(f"E: 登録されていない拡張子の画僧ファイル: {file_path}")
        return None

    return dict_image   



# JPG ファイルを開く
def open_jpg(
    file_path: str,
    use_rotate: bool = True
) -> dict:
    # 画像ファイルを開く
    image = Image.open(file_path)

    # Exif 情報を取得
    exif_info = get_exif(image)

    # use_rotate が False の場合は、 orientation をNoneにする
    if not use_rotate:
        exif_info["orientation"] = None

    return {
        "image": image,
        "exif_info": exif_info
    }



# HEIC ファイルを開く
def open_heic(
    file_path: str
) -> dict:
    # 拡張子がheicでも、jpegのときがあるので、調べる
    if is_jpeg(file_path):
        # jpeg の場合は、open_jpg で開く
        return open_jpg(file_path, use_rotate=False)
    
    # 画像ファイルを開く
    heif_file = pillow_open_heif(file_path)

    # heif_file を Image.Image に変換
    image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)

    # Exif 情報を取得
    exif_info = get_exif(heif_file)

    return {
        "image": image,
        "exif_info": exif_info
    }



# PNG ファイルを開く
def open_png(
    file_path: str
) -> dict:
    # 画像ファイルを開く
    image = Image.open(file_path)

    # Exif 情報を取得
    exif_info = get_exif(image)

    return {
        "image": image,
        "exif_info": exif_info
    }




# SOIマーカー（Start of Image）を見て、Jpegかそうでないかを確認する
def is_jpeg(
    file_path: str
) -> bool:
    with open(file_path, "rb") as f:
        f.seek(0)
        return f.read(2) == b"\xFF\xD8"


