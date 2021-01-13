import cv2
import matplotlib.pyplot as plt
# % matplotlib inline

# https://github.com/opencv/opencv/tree/master/data/haarcascades からダウンロードすること！
cascade_path = "haarcascade_frontalface_default.xml"

def face_detector(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cascade = cv2.CascadeClassifier(cascade_path)
    faces = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=2, minSize=(80, 80)) # minNeighborsは人数
    print(faces)
    if len(faces) < 0: print("No faces detected!!")
    return faces[0]


def blur_img(img, x,y,w,h, size = 30):
    blurred_img = cv2.blur(img, ksize=(size,size))
    result = img.copy()
    result[y:y+w, x:x+w] = blurred_img[y:y+w, x:x+w]
    return result

fname = "lenna.jpg"
# fname = "test2.jpg"
img = cv2.imread(fname)
x,y,w,h = face_detector(img)
result = blur_img(img, x,y,w,h)
cv2.imshow("test", result)
cv2.waitKey(0)

