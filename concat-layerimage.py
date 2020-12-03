import cv2
import glob
import numpy as np


def image_concatter(target_path):
    # 指定ディレクトリの画像読み込み
    imagelist = glob.glob(r"{}\*.bmp".format(target_path))
    print(imagelist)
    # 読み込んだ画像リストをソート
    imagelist = sorted(imagelist, key=lambda x: int(x[-8:-4]))
    # 成果物画像一時保存用
    temp = None
    for image_path in imagelist:
        # opencvで画像を1つずつ読み込み、tempの右端に足していく
        if temp is None:
            temp = cv2.imread(image_path)
        else:
            dst = cv2.imread(image_path)
            temp = cv2.hconcat([temp, dst])
    cv2.imwrite('{}\layer_concatted.jpg'.format(target_path), temp)


if __name__ == '__main__':
    print("plz input target path")
    # 連番bmpを配置したフォルダを入力する
    target_path = input()
    image_concatter(target_path)
