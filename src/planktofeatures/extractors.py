#!/bin/python3

# Copyright 2025, A Baldwin, National Oceanography Centre
#
# This file is part of planktofeatures.
#
# planktofeatures is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# planktofeatures is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with planktofeatures.  If not, see <http://www.gnu.org/licenses/>.

import numpy
from PIL import Image

class WHOIVersion4Features:
    def __init__(self, image):
        self.image = image
        self.processed = False
        self.blob_image = None
        self.features_dict = None
        self.blob_im = None
        self.features = None

    def __get_values(self):
        if not self.processed:
            self.process_now()
        if self.features_dict is None:
            self.features_dict = {}
            for item in self.features:
                self.features_dict[item[0]] = float(item[1])
        return self.features_dict

    def __get_blob(self):
        if not self.processed:
            self.process_now()
        if self.blob_image is None:
            self.blob_image = Image.fromarray(self.blob_im.astype("uint8") * 255, "L")
        return self.blob_image

    values = property(
            fget = __get_values,
            doc = "Dynamically generated features dict"
        )

    blob = property(
            fget = __get_blob,
            doc = "Dynamically generated blob image"
        )

    def process_now(self):
        feat_tup = WHOIVersion4.compute_features(numpy.asarray(self.image), None, None)
        self.blob_im = feat_tup[0]
        self.features = feat_tup[1]
        self.processed = True

class WHOIVersion4:
    from .whoi_v4.all import compute_features

    def __init__(self):
        pass

    def process(self, image):
        return WHOIVersion4Features(image)
