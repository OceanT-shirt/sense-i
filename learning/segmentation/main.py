import cv2
import numpy as np

# https://qiita.com/AtomJamesScott/items/ccef87b1092d7407de0d#%E4%BB%8A%E5%9B%9E%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA

img_src = cv2.imread('test.jpg')
gray = cv2.cvtColor(img_src, cv2.COLOR_RGB2GRAY)

#エッジ抽出
CANNY_THRESH_1 = 100.
CANNY_THRESH_2 = 200.
edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)


# 輪郭を付ける
contour_info = []
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for c in contours:
    contour_info.append((
        c,
        cv2.isContourConvex(c),
        cv2.contourArea(c),
    ))
contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
max_contour = contour_info[0]


#-- Create empty mask, draw filled polygon on it corresponding to largest contour ----
# Mask is black, polygon is white
mask = np.zeros(edges.shape)
cv2.fillConvexPoly(mask, max_contour[0], (255))

MASK_DILATE_ITER = 2
MASK_ERODE_ITER = 3
BLUR_SIZE = 5
mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
mask = cv2.GaussianBlur(mask, (BLUR_SIZE, BLUR_SIZE), 0)
cv2.imshow('mask', mask)


img_2 = img_src.copy()
img_2[mask==0] = [255, 255, 255]  # 背景塗りつぶし
cv2.imshow('result', img_2)
cv2.waitKey(0)
