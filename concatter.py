import cv2
import numpy as np
import glob

def image_concatter(target_path):
    # 同一ディレクトリの画像読み込み
    imagelist = glob.glob(r"{}\*.bmp".format(target_path))
    print(imagelist)
    # 同一ディレクトリ画像リストをソート
    imagelist = sorted(imagelist, key=lambda x:int(x[-8:-4]))
    # 成果物画像一時保存用
    temp = None
    for i in range(len(imagelist)):
        if i == len(imagelist)-1:
            break
        # opencvで画像を1つずつ読み込み、tempの右端に足していく
        if temp is None:
            temp = cv2.imread(imagelist[i])
        else:
            dst = cv2.imread(imagelist[i])
            temp = cv2.hconcat([temp, dst])
    cv2.imwrite('{}\layer_concatted.jpg'.format(target_path), temp)

if __name__ == '__main__':
    print("plz input target path")
    target_path = input()
    image_concatter(target_path)