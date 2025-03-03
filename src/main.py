# 拡張子HEICをJPGに変換するプログラム
# EXIF情報を保持したまま変換する



from edit_image import edit_image
from edit_movie import edit_movie



if __name__ == "__main__":
    # 画像フォルダを指定する
    in_image_folder = "C:\\Users\\yoichiro\\Desktop\\ふるさと館まつり\\ikeda\\in"
    out_image_folder = "C:\\Users\\yoichiro\\Desktop\\ふるさと館まつり\\ikeda\\out"

    # edit_image(in_image_folder, out_image_folder)

    edit_movie(in_image_folder, out_image_folder)
