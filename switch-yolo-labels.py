import os
import re
from PIL import Image

folder_holding_yolo_files = input("Enter the path to the yolo files: ").replace("'", "").strip()  # Images and Labels same folder
yolo_class_list_file = input("Enter the path to the file that has the yolo classes (typically classes.txt): ").strip()

# Get a list of all the classes used in the yolo format
with open(yolo_class_list_file) as f:
    yolo_classes = f.readlines()
array_of_yolo_classes = [x.strip() for x in yolo_classes]


# Description of Yolo Format values
# 15 0.448743 0.529142 0.051587 0.021081
# class_number x_yolo y_yolo yolo_width yolo_height

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


os.chdir(folder_holding_yolo_files)

if not os.path.exists(folder_holding_yolo_files + os.sep + 'Converted'):
    # If a Converted folder does not already exist, make one
    os.mkdir('Converted')

for each_yolo_file in os.listdir(folder_holding_yolo_files):
    if each_yolo_file.endswith("txt"):
        the_file = open(each_yolo_file, 'r')
        all_lines = the_file.readlines()
        image_name = each_yolo_file

        # Check to see if there is an image that matches the txt file
        if os.path.exists(each_yolo_file.replace('txt', 'jpeg')):
            image_name = each_yolo_file.replace('txt', 'jpeg')
        if os.path.exists(each_yolo_file.replace('txt', 'jpg')):
            image_name = each_yolo_file.replace('txt', 'jpg')
        if os.path.exists(each_yolo_file.replace('txt', 'png')):
            image_name = each_yolo_file.replace('txt', 'png')

        if not image_name == each_yolo_file:
            # If the image name is the same as the yolo filename
            # then we did NOT find an image that matches, and we will skip this code block
            orig_img = Image.open(image_name)  # open the image
            image_width = orig_img.width
            image_height = orig_img.height

            with open('Converted' + os.sep + each_yolo_file.replace('txt', 'txt'), 'w') as f:
                f.write('')

                for each_line in all_lines:
                    # regex to find the numbers in each line of the text file
                    yolo_array = re.split("\s", each_line.rstrip())  # remove any extra space from the end of the line

                    # initalize the variables
                    class_number = 0
                    x_yolo = 0.0
                    y_yolo = 0.0
                    yolo_width = 0.0
                    yolo_height = 0.0
                    yolo_array_contains_only_digits = True

                    # make sure the array has the correct number of items
                    if len(yolo_array) == 5:
                        for each_value in yolo_array:
                            # If a value is not a number, then the format is not correct, return false
                            if not is_number(each_value):
                                yolo_array_contains_only_digits = False

                        if yolo_array_contains_only_digits:
                            # assign the variables
                            class_number = int(yolo_array[0])
                            object_name = array_of_yolo_classes[class_number]
                            x_yolo = float(yolo_array[1])
                            y_yolo = float(yolo_array[2])
                            yolo_width = float(yolo_array[3])
                            yolo_height = float(yolo_array[4])

                            class_number = str(class_number)
                            x_yolo = str(x_yolo)
                            y_yolo = str(y_yolo)
                            yolo_width = str(yolo_width)
                            yolo_height = str(yolo_height)

                        # if class_number == "1":
                        #     pass
                        # elif class_number == "5":
                        #     pass
                        # elif class_number == "6":
                        #     pass
                        # elif class_number == "7":
                        #     pass

                            if class_number == "0":
                                class_number = "3"

                            elif class_number == "3":
                                class_number = "0"

                            elif class_number == "4":
                                class_number = "1"

                            elif class_number == "8":
                                class_number = "0"

                            elif class_number == "9":
                                class_number = "3"

                            elif class_number == "10":
                                class_number = "0"

                            else:
                                class_number = class_number

                            f.write(class_number + ' ' + x_yolo + ' ' + y_yolo + ' ' + yolo_width + ' ' + yolo_height)
                            f.write("\n")

                f.close()  # Close the file

# Check to make sure the sprite file is now in the folder
if os.path.exists("Converted"):
    print("Conversion complete")
else:
    print("There was a problem converting the files")