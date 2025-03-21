# 拡張子HEICをJPGに変換するプログラム
# EXIF情報を保持したまま変換する


import os
import shutil
from datetime import datetime

from image_editor import edit_image_main
from movie_editor import edit_movie_main


# 写真と動画のファイルを、Exif情報から更新情報を読み取り、ファイル名に適用させる
# in_folder の中身は読むだけで編集しない
# 一時的に temp_folder を使い、最終的に out_folder にコピーする
def rename_image_and_movie(
    in_folder,
    temp_folder,
    out_folder,
    default_taken_dt,
    refresh_out_folder=True
):
    # refresh_out_folder が True の場合、出力フォルダを削除して、まっさらから作成
    if refresh_out_folder:
        # 出力フォルダを削除
        if os.path.exists(out_folder):
            shutil.rmtree(out_folder)
    
    # 中間フォルダ、出力フォルダを作成
    os.makedirs(temp_folder, exist_ok=True)
    os.makedirs(out_folder, exist_ok=True)

    # フォルダ内にあるファイルを仕分ける
    # 拡張子をすべて取得する
    extensions = set([os.path.splitext(file)[1].lower() for file in os.listdir(in_folder)])
    print(extensions)

    # 拡張子ごとに、写真か動かを判別し、処理を分ける
    # 画像・動画の拡張子リスト
    IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".heic"}
    VIDEO_EXTENSIONS = {".mov", ".mp4"}

    # in_folder 内の全ファイルをループして、編集する
    # 登録されていない拡張子は、対応しない
    for file in os.listdir(in_folder):
        # 拡張子を取得
        extension = os.path.splitext(file)[1].lower()

        # 画像か動画かを判別
        if extension in IMAGE_EXTENSIONS:
            # 画像の場合
            edit_image_main(
                os.path.join(in_folder, file),
                temp_folder,
                out_folder,
                default_taken_dt
            )
        elif extension in VIDEO_EXTENSIONS:
            # 動画の場合
            edit_movie_main(
                os.path.join(in_folder, file),
                temp_folder,
                out_folder,
                default_taken_dt
            )
        else:
            # 登録されていない拡張子は、対応しない
            print(f"W: 登録されていない拡張子のファイル: {file}")



if __name__ == "__main__":
    # 入力/出力フォルダを指定する
    # 写真と動画は一緒でよい
    in_image_folder = "./data/input"
    temp_image_folder = "./data/temp"
    out_image_folder = "./data/output"
    default_taken_dt = datetime(2025, 3, 2, 10, 0, 0)

    # edit_image(in_image_folder, out_image_folder)
    #edit_movie(in_image_folder, out_image_folder)
    rename_image_and_movie(in_image_folder, temp_image_folder, out_image_folder, default_taken_dt)
