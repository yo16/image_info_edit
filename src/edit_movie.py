

import os
import glob
import subprocess
import json
import shutil
from datetime import datetime, timedelta

from utils import check_file_type



# 指定したフォルダ内の動画ファイルを変換する
def edit_movie(in_movie_folder: str, out_movie_folder: str):
    # 入力フォルダから、動画ファイルをすべて取り出す
    movie_files = glob.glob(os.path.join(in_movie_folder, "*.MOV"))

    # 出力フォルダを作成
    os.makedirs(out_movie_folder, exist_ok=True)

    # 動画ファイルをすべて変換する
    for movie_file in movie_files:
        edit_one_movie(movie_file, out_movie_folder)




# １つの動画ファイルを変換する
def edit_one_movie(in_movie_path: str, out_movie_folder_path: str):
    print(in_movie_path)
    print(check_file_type(in_movie_path))

    # 撮影日時を取得する
    create_date = None
    try:
        result = subprocess.run(
            ["exiftool", "-json", in_movie_path],
            capture_output=True, text=True, check=True, encoding="utf-8"
        )
        metadata = json.loads(result.stdout)
        create_date = metadata[0].get("CreateDate", "撮影日時が取得できません")

        # 撮影日時がUTCで取得されるため、JSTに変換する
        create_date = datetime.strptime(create_date, "%Y:%m:%d %H:%M:%S")
        create_date = create_date + timedelta(hours=9)
        create_date = create_date.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print(e)
        return f"エラー: {e}"
    # print(create_date)

    # 出力ファイル名を決定
    file_name = os.path.basename(in_movie_path)
    if (create_date):
        file_name = create_date.replace(":", "-")
        file_name = file_name.replace(" ", "_")
        file_name = file_name + ".mov"

    out_movie_path = os.path.join(out_movie_folder_path, file_name)

    # ファイルをコピーする
    shutil.copy(in_movie_path, out_movie_path)



