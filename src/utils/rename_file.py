# ファイル名が存在する間、ループして、ファイル名を変更する

import os

def rename_file(
    file_path: str
):
    # ファイル名と拡張子を取得
    file_name = os.path.basename(file_path)
    file_base_name = os.path.splitext(file_name)[0]
    file_extension = os.path.splitext(file_name)[1]
    # フォルダパスを取得
    file_dir_path = os.path.dirname(file_path)

    # すでに同じファイルが存在する場合は、"_1" などを追加する
    # ファイル名が存在する間、ループする
    i = 1
    while os.path.exists(file_path):
        new_file_name = f"{file_base_name}_{i}{file_extension}"
        # ファイル名を変更
        file_path = os.path.join(os.path.dirname(file_path), new_file_name)

        i += 1
    
    return file_path
