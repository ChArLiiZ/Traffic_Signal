import cv2
from test_detector import detect
from conf import Conf

settings = Conf("settings.json")

video = cv2.VideoCapture(settings["test_video"])

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter(settings["output_video"], fourcc, 30, (width, height))
while(video.isOpened()):
    ret, frame = video.read()
    out.write(detect(frame))
video.release()
out.release()
cv2.destroyAllWindows()

