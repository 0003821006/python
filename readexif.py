from PIL import Image
from PIL.ExifTags import TAGS

filename ='DSC_0006'

# 画像ファイルを開く
im = Image.open(filename+'.JPG')
# EXIF情報を得る
exif = im._getexif()

# 出力先のファイルを開く（新しく作成するか、既存のものを上書き）
with open(filename+'.txt', 'w') as output_file:
    # 一覧で表示
    for tag, value in exif.items():
        # ExifTags.TAGSはタグ番号とタグ名称が紐づいた辞書 eg. 256: 'ImageWidth'
        # getで番号がtagのタグ名称を取得、キーが存在しない時はtag番号のまま eg. when tag == 256, tag_name = 'ImageWidth'
        tag_name = TAGS.get(tag, tag)
        output_file.write(f"{tag_name}: {value}\n")

print('Exifデータを'+filename+'.txtに保存しました。')
