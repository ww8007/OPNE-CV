import sys
import time
import numpy as np
import cv2


img = cv2.imread('hongkong.jpg')

tm = cv2.TickMeter()

tm.reset()
tm.start()
t1 = time.time()
#edge검출 함수
#위 아래로 start와 stop을 적어주면 된다.
edge = cv2.Canny(img, 50, 150)

tm.stop()
ms=tm.getTimeMilli()
print('time:', (time.time() - t1) * 1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))

