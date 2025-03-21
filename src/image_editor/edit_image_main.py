# 画像ファイルを編集する

import os
from datetime import datetime

from .open_image import open_image
from .save_image import save_image_as_jpg
from .correct_orientation import correct_orientation
from utils import rename_file


def edit_image_main(
    in_file_path: str,
    temp_dir_path: str,
    out_dir_path: str,
    default_taken_dt: datetime
):
    print(f"I: 画像ファイルを編集します: {in_file_path}")

    # 画像ファイルを開く
    dict_image = open_image(in_file_path)
    if dict_image is None:
        print(f"E: 画像ファイルを開けませんでした: {in_file_path}")
        return
    img = dict_image["image"]

    # 画像の回転情報がある場合は変更する
    # 回転情報がない場合は、コピーして新しい `Image.Image` を返す
    img = correct_orientation(img, dict_image["exif_info"]["orientation"])
    
    # 撮影日時を取得
    taken_at = dict_image["exif_info"]["taken_dt"]
    if taken_at is None:
        taken_at = default_taken_dt

    # ファイル名を作成
    file_name = taken_at.strftime("%Y%m%d_%H%M%S") + ".jpg"
    file_path = os.path.join(out_dir_path, file_name)
    # すでに同じファイルが存在する場合は、"_1" などを追加する
    file_path = rename_file(file_path)

    # 画像を保存
    save_image_as_jpg(img, file_path)

