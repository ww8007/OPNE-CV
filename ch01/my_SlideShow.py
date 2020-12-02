import sys
import glob
import cv2

#모든 이미지 파일 불러오기 : or 나 and 연산은 못하나?
img_files = glob.glob(".\\images\\*.jpg")
for i in img_files:
    print(i)

cnt = len(img_files)
idx=0

while True:
    img = cv2.imread(img_files[idx])
    cv2.imshow('image', img)
    if cv2.waitKey(1000) == 27:
        break
    idx+=1
    if idx>=cnt:
        idx=0

cv2.destroyAllWindows()