from imutils import paths
import dlib
import cv2
from conf import Conf
from write_chinese import Write_chinese
    
settings = Conf("settings.json")
names = settings["image_names"]
xmls = settings["image_annotations"]
detectors_name = settings["image_detectors"]
test = settings["test_images"]
detectors = []
images = []


for testingPath in paths.list_images(test):
    images.append(cv2.imread(testingPath))
for image in images:
    img_string = ""
    for index in range(len(names)):
        detectors.append(dlib.simple_object_detector(detectors_name[index]))
        boxes = detectors[index](cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        for b in boxes:
            (x, y, w, h) = (b.left(), b.top(), b.right(), b.bottom())
            cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)
            img_string += " " + names[index]
            image = Write_chinese.write(image, "msjhbd.ttc", 40, (0, 0, 0), (b.left(), b.bottom()), img_string)

    
    cv2.imshow("Image", image)
    cv2.waitKey(0)


