import os
from PIL import Image

CLASSES = {"articulated_truck": 0,
           "bicycle": 1,
           "bus": 2,
           "car": 3,
           "motorcycle": 4,
           "motorized_vehicle": 5,
           "non-motorized_vehicle": 6,
           "pedestrian": 7,
           "pickup_truck": 8,
           "single_unit_truck": 9,
           "work_van": 10}

if __name__ == "__main__":
    folder = r'C:\Users\Abuelgasim\Desktop\Data\MIO-TCD-Dataset\train'  # E:\darknet-master\data\mio

    with open(r'C:\Users\Abuelgasim\Desktop\Data\MIO-TCD-Dataset\gt_train.csv') as csv:  # E:\_Dataset\MIO-TCD-Localization\gt_train.csv

        file_id = 0
        lines_to_write = ""

        for i, line in enumerate(csv):

            f_id_s, cl, left, top, right, bot = line.split(",")
            f_id = int(f_id_s)

            if (file_id != f_id):
                txt_path = os.path.sep.join([folder, f + ".txt"])
                with open(txt_path, "w") as txt:
                    txt.write(lines_to_write)
                lines_to_write = ""
                file_id = f_id

            f = f_id_s.zfill(8)

            cl = CLASSES[cl]

            width = int(right) - int(left)
            height = int(bot) - int(top)
            x_center = int(left) + (int(width) / 2)
            y_center = int(top) + (int(height) / 2)

            f_fp = os.path.sep.join([folder, f + ".jpg"])
            W, H = Image.open(f_fp).size

            rel_width = width / W
            rel_height = height / H
            rel_x_center = x_center / W
            rel_y_center = y_center / H

            lines_to_write += "{:} {:.6f} {:.6f} {:.6f} {:.6f}\n".format(cl, rel_x_center, rel_y_center, rel_width, rel_height)

        txt_path = os.path.sep.join([folder, f + ".txt"])
        with open(txt_path, "w") as txt:
            txt.write(lines_to_write)

