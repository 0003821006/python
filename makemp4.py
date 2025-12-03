# https://blog.fantom.co.jp/2019/12/30/create-video-from-multiple-images/
# https://qiita.com/sey323/items/d7da4cee448ed5be8149
import glob
# cv2をimportするには、pip install opencv-pythonが必要
import cv2

img_array = []
# for filename in sorted(glob.glob("images/*.jpg")):
for filename in sorted(glob.glob("result00*uy.png")):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

name = 'project.mp4'
# out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'MP4V'), 5.0, size) # MacだとMP4Vでは動かない。
out = cv2.VideoWriter(name, fourcc = cv2.VideoWriter_fourcc(*'mp4v'), fps = 5.0, frameSize = size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()