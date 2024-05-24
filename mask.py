"""
bitwise_and (bottom_image, top_image), where top_image is a mask where:
- BLACK is mask
- WHITE is where bottom image appears

both bottom_image and top_image must be same size!!!
"""
import cv2 
import sys

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)

img = cv2.imread("png.png")

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

backSub = cv2.createBackgroundSubtractorMOG2()


while cv2.waitKey(1) != 27: # Escape
    has_frame, frame = source.read()
    if not has_frame:
        break
    fgMask = backSub.apply(frame)
    
    result = cv2.bitwise_and(frame, img)

    cv2.imshow(win_name, result)
    cv2.imshow('FG Mask', fgMask)

source.release()    
cv2.destroyAllWindows()


