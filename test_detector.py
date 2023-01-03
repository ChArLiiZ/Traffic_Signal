from imutils import paths
import dlib
import cv2
from conf import Conf
from write_chinese import Write_chinese
    
settings = Conf("settings.json")
names = settings["image_names"]
detectors_name = settings["image_detectors"]
test = settings["test_images"]
detectors = []
images = []


def detect(image):
    img_string = ""
    for index in range(len(names)):
        boxes = detectors[index](cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        for b in boxes:
            (x, y, w, h) = (b.left(), b.top(), b.right(), b.bottom())
            cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)
            img_string += " " + names[index]
            image = Write_chinese.write(image, "msjhbd.ttc", 40, (255, 0, 255), (b.left(), b.bottom()), img_string)
    return image


for testingPath in paths.list_images(test):
    images.append(cv2.imread(testingPath))

for index in range(len(names)):
    detectors.append(dlib.simple_object_detector(detectors_name[index]))

for image in images:
    image = detect(image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)



