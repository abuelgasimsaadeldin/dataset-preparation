# dataset-preparation
MIO-TCD Dataset conversion to YOLO format and Switching class labels

### MIO-TCD Dataset conversion to YOLO format annotations
```bash
python format_mio-tcd_yolo.py
```

### Switching Class Labels in YOLO format annotations
```bash
python switch-yolo-labels.py
```

The script will ask you for the path to the folder that holds both the images and .txt yolo format (these are expected to exist in the same folder).
It will also ask for the path to the class names. This file is usally named something like "classes.txt" or "obj.names"
