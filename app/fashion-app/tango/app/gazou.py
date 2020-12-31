import cv2
import numpy as np
#OpenCVのcv2.inRangeを使うことで, HSV色空間による色指定が行える

#とりあえず赤色のみで扱います(ピンクのマーカーもひっかかると思います)
# 赤色の検出
def detect_red_color(img_path):
    # staticに保存されている画像を取り出す
    img = cv2.imread(img_path)
    # 入力された画像をHSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #色相環において赤は-60°～60°くらいだが、0～360°で指定しないといけないので
    #色指定の値域が２つにわかれます(openCVでは上記の角度を0.5倍して表現)
    
    # 赤色のHSVの値域1
    #左からH(色相),S(再度),V(明度)
    hsv_min = np.array([0,64,0])
    hsv_max = np.array([30,255,255])
    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

    # 赤色のHSVの値域2
    hsv_min = np.array([150,64,0])
    hsv_max = np.array([179,255,255])
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max)

    # 赤色領域のマスク（255：赤色、0：赤色以外）    
    mask = mask1 + mask2

    # マスキング処理
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    return mask, masked_img










# 結果を出力
#cv2.imwrite("read_mask_.jpg", red_mask)
#cv2.imwrite("red_masked_img_.jpg", red_masked_img)
