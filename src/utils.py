
import filetype


# ファイルの拡張子を確認する
def check_file_type(file_path: str) -> str:
    kind = filetype.guess(file_path)
    if kind is None:
        return "Unknown"
    return kind.mime
