# Laroussi Android Board Tool V1.1.0
is a free tool coding by "Laroussi Boulanouar" that includes most of the Test Point images, and the “ISP Point”, “Hardware Solution”, “Schematic Diagram” of the most important and famous modern Android phones. 
is specially designed for “Vivo”, “Xiaomi”, and “Oppo”, “iPhone”, “iPad”, and more phones. 
basically, saves you the effort of searching and the effort you spend every time you search for Test Point and ISP images on the Internet.

![2024-06-26_182925](https://github.com/devloperltd/Laroussi-Android-Board-TP-ISP-Schematic/assets/94921918/a110db30-b51f-452f-9fbe-669de1090969)


## Watch Finale Project Video :

[![Watch the video](images/video_thumbnail.png)](https://fb.watch/sVHNr3aEI8/)

## Credits :
- !/usr/bin/env python3.12.1
- Laroussi TestPoint T-REX Tool (c) Laroussi.Boulanouar, 2024
- Based of Pyside6 (c) GPLv3 License Algeria-Ouled Djellal
- Licensed under GPLv3 License.

## Installation

- Install python >= 3.12.1

```sh
pip install PySide6
pip install PyMuPDF
```
# Supported Brands :
- Xiaomi
- Samsung
- Huawei
- Lenovo
- Nokia
- Vivo
- OPPO
- LG
- Asus
- Vsmart
- Meizu
- Motorola
- iPhone
- iPad

# Features of Laroussi Board Tool :
- Test Points
- Hardware Solution
- ISP Point
- Schematic Diagram
- Service Code ==>> Next Update

# Example to Add Models in List :

```sh
    def TP_xiaomi_list(self):
        self.TP_phone_models = ["Xiaomi Redmi A1+", "Add New Model Here"]
        
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()
```
# Example to Add more Images Paths :

```sh
        self.TP_image_paths = {
            # Add Xiaomi Images Paths
            "Xiaomi Redmi A1+": resource_path ("TestPoint/Xiaomi/No image.png"),
            "Add new image": resource_path ("TestPoint/Xiaomi/new image.png"),
```

# Example to Add more PDF Files Paths :

```sh
        self.pdf_paths = {

            "HUAWEI1 MB Circuit schematic": {
                "Hello1.pdf": resource_path("SDiagram/Huawei/schematic1/Hello1.pdf"),
                "Hello2.pdf": resource_path("SDiagram/Huawei/schematic1/Hello2.pdf"),
            },

            "HUAWEI2 MB Circuit schematic": {
                "Hello1.pdf": resource_path("SDiagram/Huawei/schematic2/Hello1.pdf"),
                "Hello2.pdf": resource_path("SDiagram/Huawei/schematic2/Hello2.pdf"),
            },
```

# Qtreewidget add item use qt designer :

![2024-06-26_184333](https://github.com/devloperltd/Laroussi-Android-Board-TP-ISP-Schematic/assets/94921918/f4564ca1-2e77-4b05-b386-29db018fa636)

# Convert a QtDesigner QRC file to Python :

```sh
pyside6-rcc ico.qrc -o rc_ico.py
pyside6-rcc img.qrc -o rc_img.py
```
