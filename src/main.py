# 拡張子HEICをJPGに変換するプログラム
# EXIF情報を保持したまま変換する

import os
import glob
import piexif
from pillow_heif import open_heif
from PIL import Image
import filetype


# 指定したフォルダ内の画像ファイルを変換する
def edit_image(in_image_folder: str, out_image_folder: str):
    # 入力フォルダから、画像ファイルをすべて取り出す
    image_files = glob.glob(os.path.join(in_image_folder, "*.HEIC"))

    # 出力フォルダを作成
    os.makedirs(out_image_folder, exist_ok=True)

    # 画像ファイルをすべて変換する
    for image_file in image_files:
        edit_one_image(image_file, out_image_folder)




# １つの画像ファイルを変換する
def edit_one_image(in_image_path: str, out_image_folder_path: str):
    print(in_image_path)
    print(check_file_type(in_image_path))

    # # HEICを開く
    # original_image = open_heif(in_image_path)
    # image = Image.frombytes(original_image.mode, original_image.size, original_image.data)
    # Jpegファイルとして開く
    original_image = Image.open(in_image_path)
    image = original_image.copy()

    # EXIF情報を取得
    exif_data = original_image.info.get("exif")
    if exif_data:
        exif_dict = piexif.load(exif_data)
        exif_bytes = piexif.dump(exif_dict)
    else:
        exif_bytes = None

    # 出力ファイル名を取得
    # 下記の処理を施す
    #   - 拡張子をJPGに変更する
    #   - ファイル名を、exifの撮影日時を使用する
    #   - 撮影日時がない場合は、ファイル名を変更しない
    file_name = os.path.basename(in_image_path)
    if (exif_data):
        # Exifの撮影日時を取得
        datetime_original = exif_dict["Exif"].get(piexif.ExifIFD.DateTimeOriginal)
        if (datetime_original):
            exif_datetime_str = datetime_original.decode("utf-8")
            # 撮影日時をファイル名に使用
            file_name = exif_datetime_str.replace(":", "-")
            file_name = file_name.replace(" ", "_")
            file_name = file_name + ".jpg"

    out_image_path = os.path.join(out_image_folder_path, file_name.replace(".HEIC", ".jpg"))

    # JPGとして保存（EXIFを保持）
    image.save(out_image_path, "jpeg", exif=exif_bytes)
        


# ファイルの拡張子を確認する
def check_file_type(file_path: str) -> str:
    kind = filetype.guess(file_path)
    if kind is None:
        return "Unknown"
    return kind.mime





if __name__ == "__main__":
    # 画像フォルダを指定する
    in_image_folder = "C:\\Users\\yoichiro\\Desktop\\ふるさと館まつり\\ikeda\\in"
    out_image_folder = "C:\\Users\\yoichiro\\Desktop\\ふるさと館まつり\\ikeda\\out"

    edit_image(in_image_folder, out_image_folder)
