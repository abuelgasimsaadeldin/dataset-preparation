#
# Copyright (c) 2021 CertifAI Sdn. Bhd.
#
# This program is part of OSRFramework. You can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import cv2


def Yolo2Annotation(image_path, x, y, w, h):
    im = cv2.imread(image_path)
    # Get shape
    size= im.shape
    
    dw = 1.0/size[1]
    dh = 1.0/size[0]

    x = (x/dw)*2.0
    w = w/dw
    y = (y/dh)*2.0
    h = h/dh

    x_min = int((x - w)/2.0)
    x_max = int(w + x_min)
    y_min = int((y - h)/2.0)
    y_max = int(h + y_min)

    return x_min, x_max, y_min, y_max


def Annotation2Yolo(image_path, x_min, x_max, y_min, y_max):
    box = (float(x_min), float(x_max), float(y_min), float(y_max))
    im = cv2.imread(image_path)
    # Get shape
    size = im.shape

    dw = 1.0/size[1]
    dh = 1.0/size[0]
    x = (box[0]+box[1])/2.0
    y = (box[2]+box[3])/2.0
    w = box[1]-box[0]
    h = box[3]-box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return x, y, w, h

if __name__ == "__main__":
    pass