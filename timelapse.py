import cv2
import sys
import time 

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)

frame_width = int(source.get(3))
frame_height = int(source.get(4))
# name = time.asctime() + ".mp4"

out_mp4 = cv2.VideoWriter("smth.mp4", cv2.VideoWriter_fourcc(*"XVID"), 30, (frame_width, frame_height))

win_name = 'Camera Preview'
# cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# while cv2.waitKey(1) != 27: # Escape
for i in range(0,450):
    has_frame, frame = source.read()
    if not has_frame:
        break
    # cv2.imshow(win_name, frame)
    out_mp4.write(frame)
    time.sleep(1)

source.release()
out_mp4.release()
# cv2.destroyWindow(win_name) 
#
