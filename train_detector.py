from __future__ import print_function
from conf import Conf
import dlib

settings = Conf("settings.json")
xmls = settings["image_annotations"]
detectors = settings["image_detectors"]

print("[INFO] training detector...")
options = dlib.simple_object_detector_training_options()
options.C = settings["C"]
options.num_threads = settings["num_threads"]
options.epsilon = settings["epsilon"]
options.be_verbose = True
for index in range(len(xmls)):
    dlib.train_simple_object_detector(xmls[index], detectors[index], options)
    print("[INFO] training accuracy: {}".format(dlib.test_simple_object_detector(xmls[index], detectors[index])))


