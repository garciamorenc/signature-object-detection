import glob
from xml.etree import ElementTree
import numpy as np


class XmlPreprocessor(object):

    def __init__(self, data_path):
        self.path_prefix = data_path
        self.num_classes = 1
        self.data = dict()
        self._preprocess()

    def _preprocess(self):
        files = glob.glob(self.path_prefix + "/*.xml")
        for filename in files:
            bounding_boxes = []
            one_hot_classes = []
            tree = ElementTree.parse(filename)
            document = tree.find('{http://lamp.cfar.umd.edu/GEDI}DL_DOCUMENT')
            zones = tree.findall('.//{http://lamp.cfar.umd.edu/GEDI}DL_ZONE')
            for zone in zones:
                if zone.attrib['gedi_type'] == 'DLSignature':
                    y_min = zone.attrib['col']
                    x_min = zone.attrib['row']
                    x_max = zone.attrib['width']
                    y_max = zone.attrib['height']
                    bounding_box = [x_min, y_min, x_max, y_max]
                    bounding_boxes.append(bounding_box)
                    class_name = zone.attrib['gedi_type']
                    one_hot_class = self._to_one_hot(class_name)
                    one_hot_classes.append(one_hot_class)
            image_name = document.attrib['src']
            bounding_boxes = np.asarray(bounding_boxes)
            one_hot_classes = np.asarray(one_hot_classes)
            image_data = np.hstack((bounding_boxes, one_hot_classes))
            self.data[image_name] = image_data

    def _to_one_hot(self, name):
        one_hot_vector = [0] * self.num_classes
        if name == 'DLSignature':
            one_hot_vector[0] = 1
        else:
            print('unknown label: %s' % name)

        return one_hot_vector
