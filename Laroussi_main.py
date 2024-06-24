#!/usr/bin/env python3.12.1
# Laroussi TestPoint T-REX Tool (c) Laroussi.Boulanouar, 2024
# Based of Pyside6 (c) GPLv3 License Algeria-Ouled Djellal
# Licensed under GPLv3 License.

import sys
import os
import platform
import getpass
import fitz  # PyMuPDF
import winreg
from datetime import datetime
from PySide6.QtGui import QPixmap, QImage, QIcon, QMouseEvent, QDesktopServices, QMovie
from PySide6.QtCore import Qt, QUrl, Slot, QPropertyAnimation, QRect, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QMessageBox, QGraphicsScene, QGraphicsPixmapItem, QLabel, QVBoxLayout
from ui_ResponsiveTP import Ui_MainWindow

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # If the application is running from a bundle (PyInstaller)
        base_path = sys._MEIPASS
    except Exception:
        # If the application is running in a development environment
        base_path = os.path.abspath(os.path.dirname(__file__))  # Adjust this as necessary for your project structure

    # Handle paths within .qrc
    if relative_path.startswith(":/"):
        return relative_path
    else:
        # Construct the full path for other relative paths
        return os.path.join(base_path, relative_path)

def get_windows_edition():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        edition, _ = winreg.QueryValueEx(key, "EditionID")
        return edition
    except Exception as e:
        return "Unknown"

def update_labels(time_label, system_label, user_label):
    # Update time label
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.setText(f"{current_time}")

    # Update system label
    system_info = platform.system()
    if system_info == 'Windows':
        # Get more detailed Windows version information
        version_info = platform.win32_ver()
        edition = get_windows_edition()
        system_label.setText(f"Windows {version_info[0]} {edition} {version_info[1]}")
    else:
        system_label.setText(f"{system_info}")

    # Update user label
    user_label.setText(f"{getpass.getuser()}")

class T_point_Window(QMainWindow):

    ##################################################
    ############# Test Point List Model's ############
    
    def TP_xiaomi_list(self):
        self.TP_phone_models = ["Xiaomi Redmi A1+"]
        
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()

    def TP_samsung_list(self):
        self.TP_phone_models = ["Samsung Galaxy A02"]
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()

    def TP_huawei_list(self):
        self.TP_phone_models = ["Huawei P20 Lite Dual SIM"]
        
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()

    def TP_vivo_list(self):
        self.TP_phone_models = ["Vivo Y50"]
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()

    def TP_oppo_list(self):
        self.TP_phone_models = ["Oppo Find X5 Lite"]
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()

    def TP_lenovo_list(self):
        self.TP_phone_models = ["Lenovo K13"]
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()

    def TP_Vsmart_list(self):
        self.TP_phone_models = ["VSMART V640A LIVE 4 TEST POINT"]
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()

    def TP_nokia_list(self):
        self.TP_phone_models = ["Nokia 2 Dual SIM TA-1029"]
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()

    def TP_azus_list(self):
        self.TP_phone_models = ["ASUS ZENFONE 3 ZE520KL/ASUS Z017D"]
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()

    def TP_lg_list(self):
        self.TP_phone_models = ["LG K40S"]
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()

    def TP_meizu_list(self):
        self.TP_phone_models = ["MEIZU M6 Note MSM8953"]
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()

    def TP_motorola_list(self):
        self.TP_phone_models = ["Motorola Moto E13 2023"]
        self.all_TP_phone_models = self.TP_phone_models
        self.TP_phone_list()

    def TP_phone_list(self):
        self.ui.TP_Phone_List.clear()  # Clear previous items in the list
        for model in self.TP_phone_models:
            item = QListWidgetItem(model)
            self.ui.TP_Phone_List.addItem(item)

    def get_TP_brand_name(self, index):
        item = self.ui.TP_Phone_List.itemFromIndex(index)
        if item is not None:
            selected_TP_model = item.text()
            self.ui.TP_brand_name_label.setText(selected_TP_model)  # Set the full text

    #################################################
    ############# ISP Pinout List Model's ###########

    def ISP_xiaomi_list(self):
        self.ISP_phone_models = ["XIAOMI MI MAX"]
        self.all_ISP_phone_models = self.ISP_phone_models
        self.ISP_phone_list()

    def ISP_samsung_list(self):
        self.ISP_phone_models = ["SAMSUNG A01 CORE (SM-A013)"]
        self.all_ISP_phone_models = self.ISP_phone_models
        self.ISP_phone_list()

    def ISP_huawei_list(self):
        self.ISP_phone_models = ["HUAWEI ASCEND G300 U8815 eMMC"]
        self.all_ISP_phone_models = self.ISP_phone_models
        self.ISP_phone_list()

    def ISP_vivo_list(self):
        self.ISP_phone_models = ["VIVO V7 PLUS ISP Pinout"]
        self.all_ISP_phone_models = self.ISP_phone_models
        self.ISP_phone_list()

    def ISP_oppo_list(self):
        self.ISP_phone_models = ["OPPO A5 2020 (CPH1931) ISP Pinout"]
        self.all_ISP_phone_models = self.ISP_phone_models
        self.ISP_phone_list()

    def ISP_lenovo_list(self):
        self.ISP_phone_models = ["LENOVO IDEATAB 2A7-10F eMMC"]
        self.all_ISP_phone_models = self.ISP_phone_models
        self.ISP_phone_list()

    def ISP_Vsmart_list(self):
        self.ISP_phone_models = ["Vsmart No image"]
        self.all_ISP_phone_models = self.ISP_phone_models
        self.ISP_phone_list()

    def ISP_nokia_list(self):
        self.ISP_phone_models = ["NOKIA 5.4/3.4 ISP PINOUT"]
        self.all_ISP_phone_models = self.ISP_phone_models
        self.ISP_phone_list()

    def ISP_azus_list(self):
        self.ISP_phone_models = ["ASUS ZENFONE 5Q 5 LITE (X017DA)"]
        self.all_ISP_phone_models = self.ISP_phone_models
        self.ISP_phone_list()

    def ISP_lg_list(self):
        self.ISP_phone_models = ["LG H791 eMMC PINOUT"]
        self.all_ISP_phone_models = self.ISP_phone_models
        self.ISP_phone_list()

    def ISP_meizu_list(self):
        self.ISP_phone_models = ["MEIZU 15 eMMC PINOUT"]
        self.all_ISP_phone_models = self.ISP_phone_models
        self.ISP_phone_list()

    def ISP_motorola_list(self):
        self.ISP_phone_models = ["Motorola No image"]
        self.all_ISP_phone_models = self.ISP_phone_models
        self.ISP_phone_list()

    def ISP_phone_list(self):
        self.ui.ISP_Phone_List.clear()  # Clear previous items in the list
        for model in self.ISP_phone_models:
            item = QListWidgetItem(model)
            self.ui.ISP_Phone_List.addItem(item)

    def get_ISP_brand_name(self, index):
        item = self.ui.ISP_Phone_List.itemFromIndex(index)
        if item is not None:
            selected_ISP_model = item.text()
            self.ui.ISP_brand_name_label.setText(selected_ISP_model)  # Set the full text

    ############################################################
    ############# Hardware Solution List Model's ###############

    def HS_xiaomi_list(self):
        self.HS_phone_models = ["Mi Max 3 Touch Screen Ways"]
        self.all_HS_phone_models = self.HS_phone_models
        self.HS_phone_list()

    def HS_samsung_list(self):
        self.HS_phone_models = ["Samsung A50 Charging Ways"]
        self.all_HS_phone_models = self.HS_phone_models
        self.HS_phone_list()

    def HS_huawei_list(self):
        self.HS_phone_models = ["Huawei Ascend G6 Microphone"]
        self.all_HS_phone_models = self.HS_phone_models
        self.HS_phone_list()

    def HS_vivo_list(self):
        self.HS_phone_models = ["Vivo V5 Plus Repair Not Charging"]
        self.all_HS_phone_models = self.HS_phone_models
        self.HS_phone_list()

    def HS_oppo_list(self):
        self.HS_phone_models = ["OPPO A3s Charging Line Supply"]
        self.all_HS_phone_models = self.HS_phone_models
        self.HS_phone_list()

    def HS_lenovo_list(self):
        self.HS_phone_models = [""]
        self.all_HS_phone_models = self.HS_phone_models
        self.HS_phone_list()

    def HS_Vsmart_list(self):
        self.HS_phone_models = [""]
        self.all_HS_phone_models = self.HS_phone_models
        self.HS_phone_list()

    def HS_nokia_list(self):
        self.HS_phone_models = [""]
        self.all_HS_phone_models = self.HS_phone_models
        self.HS_phone_list()

    def HS_azus_list(self):
        self.HS_phone_models = [""]
        self.all_HS_phone_models = self.HS_phone_models
        self.HS_phone_list()

    def HS_lg_list(self):
        self.HS_phone_models = [""]
        self.all_HS_phone_models = self.HS_phone_models
        self.HS_phone_list()

    def HS_meizu_list(self):
        self.HS_phone_models = [""]
        self.all_HS_phone_models = self.HS_phone_models
        self.HS_phone_list()

    def HS_motorola_list(self):
        self.HS_phone_models = [""]
        self.all_HS_phone_models = self.HS_phone_models
        self.HS_phone_list()

    def HS_phone_list(self):
        self.ui.HS_Phone_List.clear()  # Clear previous items in the list
        for model in self.HS_phone_models:
            item = QListWidgetItem(model)
            self.ui.HS_Phone_List.addItem(item)

    def get_HS_brand_name(self, index):
        item = self.ui.HS_Phone_List.itemFromIndex(index)
        if item is not None:
            selected_HS_model = item.text()
            self.ui.HS_brand_name_label.setText(selected_HS_model)  # Set the full text

    def __init__(self):
        super(T_point_Window, self).__init__()
        self.ui = Ui_MainWindow()  # Use Ui_T_point_Window to set up the UI
        self.ui.setupUi(self)

        self.ui.tabWidget.setCurrentIndex(0)
        # Remove Windows Default Title Bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Assing Exit Button
        self.ui.exit_btn.clicked.connect(self.close)
        # Assing Minimize Button
        self.ui.minimize_btn.clicked.connect(self.showMinimized)
        # Assing Maximize Button
        self.ui.maximize_btn.clicked.connect(self.toggleMaximizeRestore)  
        # Define the path to the restore icon
        self.restore_icon_path = "icons/restore-maximize.png"
        self.restore_icon = QIcon(self.restore_icon_path)    
        # Store the default maximize icon set in Qt Designer
        self.maximize_icon = self.ui.maximize_btn.icon()

        # Store the default window geometry (size and position)
        self.default_geometry = self.geometry()

        # Set Custom Navigation Bar
        self.ui.Menu_Frame.mousePressEvent = self.mousePressEvent
        self.ui.Menu_Frame.mouseMoveEvent = self.mouseMoveEvent
        self.ui.Menu_Frame.mouseReleaseEvent = self.mouseReleaseEvent

        # Add this line to store the click position
        self.clickPosition = None

        # Connect tab change signal to a function
        #self.ui.tabWidget.currentChanged.connect(self.on_tab_changed)

        # Initialize zoom counter and limit
        self.zoom_counter = 0
        self.max_zoom_count = 3
        
        # Connect double-click event to Zoom
        self.ui.TP_IMG_graphicsView.mouseDoubleClickEvent = self.TP_zoom_toggle
        self.ui.ISP_IMG_graphicsView.mouseDoubleClickEvent = self.ISP_zoom_toggle
        self.ui.HS_IMG_graphicsView.mouseDoubleClickEvent = self.HS_zoom_toggle

        # Connect the itemClicked signal to the custom slot
        self.ui.treeWidget.itemClicked.connect(self.get_SD_brand_name)

        # Load image and fit it to the view
        self.TP_load_image()
        self.ISP_load_image()
        self.HS_load_image()

        # Connect function to update labels
        self.update_labels()

        # Initialize all_TP_phone_models attribute
        self.all_TP_phone_models = []
        self.all_ISP_phone_models = []
        self.all_HS_phone_models = []

        # Assing Search Phone Models
        self.ui.TP_Search_lineEdit.textChanged.connect(self.filter_TP_phone_list)
        self.ui.ISP_Search_lineEdit.textChanged.connect(self.filter_ISP_phone_list)
        self.ui.HS_Search_lineEdit.textChanged.connect(self.filter_HS_phone_list)

        # Open the URL in the default web browser
        self.ui.SUPPORT_BTN.clicked.connect(self.openSupport)
        self.ui.SOURCE_BTN.clicked.connect(self.openContact)
        self.ui.Video_BTN.clicked.connect(self.openViveo)
        self.ui.SUPPORT_BTN_2.clicked.connect(self.openSupport)
        self.ui.SOURCE_BTN_2.clicked.connect(self.openContact)
        self.ui.Video_BTN1.clicked.connect(self.openViveo)
        self.ui.SUPPORT_BTN_3.clicked.connect(self.openSupport)
        self.ui.SOURCE_BTN_3.clicked.connect(self.openContact)
        self.ui.Video_BTN2.clicked.connect(self.openViveo)
        self.ui.SUPPORT_BTN_4.clicked.connect(self.openSupport)
        self.ui.SOURCE_BTN_4.clicked.connect(self.openContact)
        self.ui.Video_BTN3.clicked.connect(self.openViveo)

        # Assing TP Phone Models Button's
        self.ui.TP_XIAOMI_BTN.clicked.connect(self.TP_xiaomi_list)
        self.ui.TP_SAMSUNG_BTN.clicked.connect(self.TP_samsung_list)
        self.ui.TP_HUAWEI_BTN.clicked.connect(self.TP_huawei_list)
        self.ui.TP_VIVO_BTN.clicked.connect(self.TP_vivo_list)
        self.ui.TP_OPPO_BTN.clicked.connect(self.TP_oppo_list)
        self.ui.TP_LENOVO_BTN.clicked.connect(self.TP_lenovo_list)
        self.ui.TP_VSMART_BTN.clicked.connect(self.TP_Vsmart_list)
        self.ui.TP_NOKIA_BTN.clicked.connect(self.TP_nokia_list)
        self.ui.TP_AZUS_BTN.clicked.connect(self.TP_azus_list)
        self.ui.TP_LG_BTN.clicked.connect(self.TP_lg_list)
        self.ui.TP_MEIZU_BTN.clicked.connect(self.TP_meizu_list)
        self.ui.TP_MOTOROLA_BTN.clicked.connect(self.TP_motorola_list)

        # Assing ISP Phone Models Button's
        self.ui.ISP_XIAOMI_BTN.clicked.connect(self.ISP_xiaomi_list)
        self.ui.ISP_SAMSUNG_BTN.clicked.connect(self.ISP_samsung_list)
        self.ui.ISP_HUAWEI_BTN.clicked.connect(self.ISP_huawei_list)
        self.ui.ISP_VIVO_BTN.clicked.connect(self.ISP_vivo_list)
        self.ui.ISP_OPPO_BTN.clicked.connect(self.ISP_oppo_list)
        self.ui.ISP_LENOVO_BTN.clicked.connect(self.ISP_lenovo_list)
        self.ui.ISP_VSMART_BTN.clicked.connect(self.ISP_Vsmart_list)
        self.ui.ISP_NOKIA_BTN.clicked.connect(self.ISP_nokia_list)
        self.ui.ISP_AZUS_BTN.clicked.connect(self.ISP_azus_list)
        self.ui.ISP_LG_BTN.clicked.connect(self.ISP_lg_list)
        self.ui.ISP_MEIZU_BTN.clicked.connect(self.ISP_meizu_list)
        self.ui.ISP_MOTOROLA_BTN.clicked.connect(self.ISP_motorola_list)
        
        # Assing HS Phone Models Button's
        self.ui.HS_XIAOMI_BTN.clicked.connect(self.HS_xiaomi_list)
        self.ui.HS_SAMSUNG_BTN.clicked.connect(self.HS_samsung_list)
        self.ui.HS_HUAWEI_BTN.clicked.connect(self.HS_huawei_list)
        self.ui.HS_VIVO_BTN.clicked.connect(self.HS_vivo_list)
        self.ui.HS_OPPO_BTN.clicked.connect(self.HS_oppo_list)
        self.ui.HS_LENOVO_BTN.clicked.connect(self.HS_lenovo_list)
        self.ui.HS_VSMART_BTN.clicked.connect(self.HS_Vsmart_list)
        self.ui.HS_NOKIA_BTN.clicked.connect(self.HS_nokia_list)
        self.ui.HS_AZUS_BTN.clicked.connect(self.HS_azus_list)
        self.ui.HS_LG_BTN.clicked.connect(self.HS_lg_list)
        self.ui.HS_MEIZU_BTN.clicked.connect(self.HS_meizu_list)
        self.ui.HS_MOTOROLA_BTN.clicked.connect(self.HS_motorola_list)

        # Connect Phone List clicked signal to display_image method
        self.ui.TP_Phone_List.clicked.connect(self.TP_display_image)
        self.ui.ISP_Phone_List.clicked.connect(self.ISP_display_image)
        self.ui.HS_Phone_List.clicked.connect(self.HS_display_image)

        # Connect Phone List clicked signal to get brand name method
        self.ui.TP_Phone_List.clicked.connect(self.get_TP_brand_name)
        self.ui.ISP_Phone_List.clicked.connect(self.get_ISP_brand_name)
        self.ui.HS_Phone_List.clicked.connect(self.get_HS_brand_name)

        ###############################################
        ############# Test Point's ####################

        # Dictionary to map phone models to image paths
        self.TP_image_paths = {
            # Add Xiaomi Images Paths
            "Xiaomi Redmi A1+": resource_path ("TestPoint/Xiaomi/No image.png"),

            # Add Samsung Images Paths
            "Samsung Galaxy A02": resource_path ("TestPoint/Samsung/No image.png"),

            # Add Huawei Images Paths 
            "Huawei P20 Lite Dual SIM": resource_path ("TestPoint/Huawei/No image.png"),

            # Add Vivo Images Paths
            "Vivo Y50": resource_path ("TestPoint/Vivo/No image.png"),

            # Add Oppo Images Paths
            "Oppo Find X5 Lite": resource_path ("TestPoint/Oppo/No image.png"),

            # Add Lenovo Images Paths
            "Lenovo K13": resource_path ("TestPoint/Lenovo/No image.png"),

            # Add Vsmart Images Paths
            "VSMART V640A LIVE 4 TEST POINT": resource_path ("TestPoint/Vsmart/No image.png"),
            
            # Add Nokia Images Paths
            "Nokia C21 Plus": resource_path ("TestPoint/Nokia/No image.png"),

            # Add Asus Images Paths
            "ASUS ZENFONE 3 ZE520KL/ASUS Z017D": resource_path ("TestPoint/Asus/No image.png"),

            # Add LG Images Paths
            "LG K40S": resource_path ("TestPoint/LG/No image.png"),

            # Add Meizu Images Paths
            "MEIZU M6 Note MSM8953": resource_path ("TestPoint/Meizu/No image.png"),

            # Add Motorola Images Paths
            "Motorola Moto E13 2023": resource_path ("TestPoint/Motorola/No image.png"),

        }
        self.TP_phone_models = []  # Initialize TP_phone_models list

        ###############################################
        ############# ISP Pinout ######################

        # Dictionary to map phone models to image paths
        self.ISP_image_paths = {
            # Add IPS Xiaomi Images Paths
            "XIAOMI MI MAX": resource_path ("ISP/Xiaomi/No image.png"),

            # Add IPS Samsung Images Paths
            "SAMSUNG A01 CORE (SM-A013)": resource_path ("ISP/Samsung/No image.png"),

            # Add IPS Huawei Images Paths
            "HUAWEI ASCEND G300 U8815 eMMC": resource_path ("ISP/Huawei/No image.png"),

            # Add IPS Vivo Images Paths
            "VIVO V7 PLUS ISP Pinout": resource_path ("ISP/Vivo/No image.png"),

            # Add IPS Oppo Images Paths
            "OPPO A5 2020 (CPH1931) ISP Pinout": resource_path ("ISP/Oppo/No image.png"),

            # Add IPS Lenovo Images Paths
            "LENOVO IDEATAB 2A7-10F eMMC": resource_path ("ISP/Lenovo/No image.png"),
            
            # Add IPS Vsmart Images Paths
            "Vsmart No image": resource_path (":ISP/Vsmart/No image.png"),            

            # Add IPS Nokia Images Paths
            "NOKIA 5.4/3.4 ISP PINOUT" : resource_path ("ISP/Nokia/No image.png"),

            # Add IPS Asus Images Paths
            "ASUS ZENFONE 5Q 5 LITE (X017DA)" : resource_path ("ISP/Asus/No image.png"),

            # Add IPS LG Images Paths
            "LG H791 eMMC PINOUT" : resource_path ("ISP/LG/No image.png"),

            # Add IPS Meizu Images Paths
            "MEIZU 15 eMMC PINOUT" : resource_path ("ISP/Meizu/No image.png"),

            # Add IPS Motorola Images Paths
            "Motorola No image" : resource_path ("ISP/Motorola/No image.png"),

        }
        self.ISP_phone_models = []  # Initialize TP_phone_models list

        ###############################################
        ############# Hardware Solution ###############

        self.HS_image_paths = {
            # Add HS Xiaomi Images Paths
            "Mi Max 3 Touch Screen Ways": resource_path ("HSolution/Xiaomi/No image.png"),
                        
            # Add HS Samsung Images Paths
            "Samsung A50 Charging Ways": resource_path ("HSolution/Samsung/No image.png"),

            # Add HS Huawei Images Paths
            "Huawei Ascend G6 Microphone": resource_path ("HSolution/Huawei/No image.png"),

            # Add HS Vivo Images Paths
            "Vivo V5 Plus Repair Not Charging": resource_path ("HSolution/Vivo/No image.png"),

            # Add HS Oppo Images Paths
            "OPPO A3s Charging Line Supply" : resource_path ("HSolution/Oppo/No image.png"),

            # Add HS Lenovo Images Paths
            "": resource_path ("HSolution/Lenovo/.png"),

            # Add HS Vsmart Images Paths
            "": resource_path ("HSolution/Vsmart/.png"),

            # Add HS Nokia Images Paths
            "": resource_path ("HSolution/Nokia/.png"),

            # Add HS Azus Images Paths
            "": resource_path ("HSolution/Azus/.png"),

            # Add HS LG Images Paths
            "": resource_path ("HSolution/LG/.png"),

            # Add HS Meizu Images Paths
            "": resource_path ("HSolution/Meizu/.png"),

            # Add HS Motorola Images Paths
            "": resource_path ("HSolution/Motorola/.png"),

        }
        self.HS_phone_models = []  # Initialize HS_phone_models list

        ###############################################
        ############# Schematic Diagram ###############

        # Access widgets
        self.treeWidget = self.ui.treeWidget
        # Initialize the scene for the QGraphicsView
        self.scene = QGraphicsScene()
        self.ui.SD_PDF_graphicsView.setScene(self.scene)
        self.treeWidget.itemClicked.connect(self.on_item_clicked)
        # Connect double-click event for zooming
        self.ui.SD_PDF_graphicsView.mouseDoubleClickEvent = self.on_mouse_double_click

        self.base_dpi = 150  # Higher base DPI for better quality
        self.current_dpi = self.base_dpi
        self.pdf_path = None

        # Set up the spinner as a QLabel with QMovie
        self.spinner_label = QLabel(self)
        self.spinner_label.setAlignment(Qt.AlignCenter)
        self.spinner_label.setStyleSheet("background-color: transparent; border: none;")
        spinner_path = resource_path ("icons/ZKZg.gif")
        self.spinner_movie = QMovie(spinner_path)
        self.spinner_label.setMovie(self.spinner_movie)
        self.spinner_label.hide()

        # Layout to overlay the spinner on the graphics view
        layout = QVBoxLayout(self.ui.SD_PDF_graphicsView)
        layout.addWidget(self.spinner_label, alignment=Qt.AlignCenter)

        self.pdf_paths = {

            "HUAWEI Agassi2 MB Circuit schematic": {
                "Hello.pdf": resource_path("SDiagram/Huawei/schematic/Hello.pdf"),
            },

            "Samsung Galaxy A01 A015F Schematic": {
                "Hello.pdf": resource_path("SDiagram/Samsung/schematic/Hello.pdf"),
            },


            "Oppo A11w (Joy 3) Schematic & Layout Diagrams": {
                "Hello.pdf": resource_path("SDiagram/Oppo/schematic/Hello.pdf"),

        },

            "Lenovo A278T Schematic Diagrams": {
                "Hello.pdf": resource_path("SDiagram/Lenovo/schematic/Hello.pdf"),
            },

            "LG ID2750 Service & Schematics": {
                "Hello.pdf": resource_path("SDiagram/LG/schematic/Hello.pdf"),
            },

            "Meizu 16s schematics": {
                "Hello.pdf": resource_path("SDiagram/Meizu/schematic/Hello.pdf"),
            },

            "Nokia lumia 510 Schematic": {
                "Hello.pdf": resource_path("SDiagram/Nokia/schematic/Hello.pdf"),
            },

            "Xiaomi Redmi 8 (olive) Schematic": {
                "Hello.pdf": resource_path("SDiagram/Xiaomi/schematic/Hello.pdf"),
         },


        "iPhone 2 N82 820-2186 Schematics Diagram": {
            "Hello.pdf": resource_path("SDiagram/iPhone/schematic/Hello.pdf"),
        },

        "Apple ipad 2 K94 Chopin MLB 820-3069-A": {
            "Hello.pdf": resource_path("SDiagram/iPad/schematic/Hello.pdf"),
        },

    }

    # Call the Position of the window To Center
    def showEvent(self, event):
        super().showEvent(event)
        self.centerWindow()

    def centerWindow(self):
        screen = QApplication.primaryScreen()
        if screen is not None:
            # Get available screen geometry (excluding taskbar)
            screen_geometry = screen.availableGeometry()
            # Calculate center position considering taskbar height
            x = (screen_geometry.width() - self.width()) / 2
            y = (screen_geometry.height() - self.height()) / 2
            # Set the position of the window
            self.move(x, y)

    # Handle Mouse Move Window On the click position Menu Bar
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clickPosition = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.clickPosition is not None:
            if self.isMaximized():
                return  # Skip moving logic if the window is maximized
            self.move(event.globalPosition().toPoint() - self.clickPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clickPosition = None
            event.accept()

    # Get Toggle Minimize & Maximize 
    def toggleMaximizeRestore(self):
        if self.isMaximized():
            self.ui.maximize_btn.setIcon(self.maximize_icon)
            self.animateRestore()
        else:
            self.default_geometry = self.geometry()  # Update default geometry before maximizing
            self.ui.maximize_btn.setIcon(self.restore_icon)
            self.animateMaximize()

    def animateMaximize(self):
        # Animate maximizing the window
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(200)  # Duration in milliseconds
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(screen_geometry)
        self.animation.finished.connect(self.showMaximized)  # Maximize after animation
        self.animation.start()

    def animateRestore(self):
        # Animate restoring the window
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(200)  # Duration in milliseconds
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(self.default_geometry)
        self.animation.finished.connect(self.showNormal)  # Restore normal after animation
        self.animation.start()

    def animateMinimize(self):
        # Animate minimizing the window
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        minimized_geometry = QRect(self.geometry().x(), screen_geometry.bottom(), self.width(), 0)

        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(200)  # Duration in milliseconds
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(minimized_geometry)
        self.animation.finished.connect(self.showMinimized)  # Minimize after animation
        self.animation.start()

        self.pdf_path = ""


    def show_spinner(self):
        self.spinner_label.show()
        self.spinner_movie.start()

    def hide_spinner(self):
        self.spinner_label.hide()
        self.spinner_movie.stop()

    def on_item_clicked(self, item, column):
        item_text = item.text(0)
        parent_item = item.parent()

        if parent_item:
            parent_text = parent_item.text(0)
            if parent_text in self.pdf_paths:
                if item_text in self.pdf_paths[parent_text]:
                    self.pdf_path = self.pdf_paths[parent_text][item_text]
                    print(f"Resolved file path: {self.pdf_path}")
                    if os.path.exists(self.pdf_path):
                        self.show_spinner()
                        QTimer.singleShot(800, self.render_pdf)  # Delay rendering to show spinner
                    else:
                        print(f"File does not exist: {self.pdf_path}")
                        QMessageBox.critical(self, "Error", f"File does not exist: {self.pdf_path}")

    def render_pdf(self):
        if self.pdf_path:
            doc = fitz.open(self.pdf_path)
            self.scene.clear()  # Clear the scene before rendering new pages
            y_offset = 0  # To keep track of where to place the next page
            for page_number in range(len(doc)):
                page = doc.load_page(page_number)
                img = page.get_pixmap(matrix=fitz.Matrix(self.current_dpi / 72, self.current_dpi / 72))
                qimage = QImage(img.samples, img.width, img.height, img.stride, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qimage)
                item = QGraphicsPixmapItem(pixmap)
                item.setPos(0, y_offset)  # Set position of the item
                self.scene.addItem(item)
                y_offset += img.height  # Update offset for the next page
            self.hide_spinner()

    def on_mouse_double_click(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:  # Zoom in on double left click
            self.current_dpi += 30  # Increase DPI for zooming in
            self.show_spinner()
            QTimer.singleShot(500, self.render_pdf)  # Delay rendering to show spinner
        elif event.button() == Qt.RightButton:  # Zoom out on double right click
            self.current_dpi = max(30, self.current_dpi - 30)  # Decrease DPI but keep it positive
            self.show_spinner()
            QTimer.singleShot(500, self.render_pdf)  # Delay rendering to show spinner

    def get_SD_brand_name(self, item, column):
        selected_SD_model = item.text(column)
        self.ui.SD_brand_name_label.setText(selected_SD_model)  # Set the full text

    def openSupport(self):
        # Specify the URL you want to open
        url = QUrl("https://t.me/UncleAnonymous")
        # Open the URL in the default web browser
        QDesktopServices.openUrl(url)

    def openContact(self):
        # Specify the URL you want to open
        url = QUrl("https://www.facebook.com/Laroussi.Br")
        # Open the URL in the default web browser
        QDesktopServices.openUrl(url)

    def openViveo(self):
        # Specify the URL you want to open
        url = QUrl("https://www.youtube.com/@LaroussiHRJ")
        # Open the URL in the default web browser
        QDesktopServices.openUrl(url)

    # Call the function time, systemInfo, user
    def update_labels(self):
        # Call the function to update labels
        update_labels(self.ui.time_label, self.ui.system_label, self.ui.user_label)

    # Load TP image and fit it to the view
    def TP_load_image(self):
        pixmap = QPixmap()
        scene = QGraphicsScene(self)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        pixmap_item.setTransformationMode(Qt.SmoothTransformation)
        scene.addItem(pixmap_item)
        self.ui.TP_IMG_graphicsView.setScene(scene)
        self.ui.TP_IMG_graphicsView.fitInView(pixmap_item, Qt.KeepAspectRatio)

    # ISP Toggle zoom level on double-click
    def TP_zoom_toggle(self, event):
        if event.button() == Qt.LeftButton:
            if self.zoom_counter % 2 == 0:
                self.ui.TP_IMG_graphicsView.resetTransform()
            else:
                self.ui.TP_IMG_graphicsView.scale(1.5, 1.5)
            self.zoom_counter += 1

    # Load ISP image and fit it to the view
    def ISP_load_image(self):
        pixmap = QPixmap()
        scene = QGraphicsScene(self)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        pixmap_item.setTransformationMode(Qt.SmoothTransformation)
        scene.addItem(pixmap_item)
        self.ui.ISP_IMG_graphicsView.setScene(scene)
        self.ui.ISP_IMG_graphicsView.fitInView(pixmap_item, Qt.KeepAspectRatio)

    # ISP Toggle zoom level on double-click
    def ISP_zoom_toggle(self, event):
        if event.button() == Qt.LeftButton:
            if self.zoom_counter % 2 == 0:
                self.ui.ISP_IMG_graphicsView.resetTransform()
            else:
                self.ui.ISP_IMG_graphicsView.scale(1.5, 1.5)
            self.zoom_counter += 1

    # Load HS image and fit it to the view
    def HS_load_image(self):
        pixmap = QPixmap()
        scene = QGraphicsScene(self)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        pixmap_item.setTransformationMode(Qt.SmoothTransformation)
        scene.addItem(pixmap_item)
        self.ui.HS_IMG_graphicsView.setScene(scene)
        self.ui.HS_IMG_graphicsView.fitInView(pixmap_item, Qt.KeepAspectRatio)

    # HS Toggle zoom level on double-click
    def HS_zoom_toggle(self, event):
        if event.button() == Qt.LeftButton:
            if self.zoom_counter % 2 == 0:
                self.ui.HS_IMG_graphicsView.resetTransform()
            else:
                self.ui.HS_IMG_graphicsView.scale(1.5, 1.5)
            self.zoom_counter += 1

    ###############################################
    ############# Test Point's ####################

    @Slot(str)
    def filter_TP_phone_list(self, text):
        filtered_models = [model for model in self.all_TP_phone_models if text.lower() in model.lower()]
        self.TP_phone_models = filtered_models
        self.TP_phone_list()

    def TP_display_image(self, index):
        item = self.ui.TP_Phone_List.itemFromIndex(index)
        if item is not None:
            selected_model = item.text()
            if selected_model in self.TP_image_paths:
                image_path = self.TP_image_paths[selected_model]
                pixmap = QPixmap(image_path)
                if pixmap.isNull():
                    QMessageBox.warning(self, "Image Not Found", "The image for this phone model is not found.")
                else:
                    # Get the viewport rectangle
                    viewport_rect = self.ui.TP_IMG_graphicsView.viewport().rect()

                    scene = QGraphicsScene(self)
                    pixmap_item = QGraphicsPixmapItem(pixmap)

                    # Scale pixmap to fit the viewport
                    pixmap_item.setTransformOriginPoint(pixmap.width() / 2, pixmap.height() / 2)
                    pixmap_item.setScale(min(viewport_rect.width() / pixmap.width(), viewport_rect.height() / pixmap.height()))

                    scene.addItem(pixmap_item)
                    self.ui.TP_IMG_graphicsView.setScene(scene)
            else:
                QMessageBox.warning(self, "Image Not Found", "No image found for this phone model.") 
    ###############################################
    ############# ISP Pinout ######################

    @Slot(str)
    def filter_ISP_phone_list(self, text):
        filtered_models = [model for model in self.all_ISP_phone_models if text.lower() in model.lower()]
        self.ISP_phone_models = filtered_models
        self.ISP_phone_list()

    def ISP_display_image(self, index):
        item = self.ui.ISP_Phone_List.itemFromIndex(index)
        if item is not None:
            selected_model = item.text()
            if selected_model in self.ISP_image_paths:
                image_path = self.ISP_image_paths[selected_model]
                pixmap = QPixmap(image_path)
                if pixmap.isNull():
                    QMessageBox.warning(self, "Image Not Found", "The image for this phone model is not found.")
                else:
                    # Get the viewport rectangle
                    viewport_rect = self.ui.ISP_IMG_graphicsView.viewport().rect()

                    scene = QGraphicsScene(self)
                    pixmap_item = QGraphicsPixmapItem(pixmap)

                    # Scale pixmap to fit the viewport
                    pixmap_item.setTransformOriginPoint(pixmap.width() / 2, pixmap.height() / 2)
                    pixmap_item.setScale(min(viewport_rect.width() / pixmap.width(), viewport_rect.height() / pixmap.height()))

                    scene.addItem(pixmap_item)
                    self.ui.ISP_IMG_graphicsView.setScene(scene)
            else:
                QMessageBox.warning(self, "Image Not Found", "No image found for this phone model.")  

    ###############################################
    ############# Hardware Solution ###############

    @Slot(str)
    def filter_HS_phone_list(self, text):
        filtered_models = [model for model in self.all_HS_phone_models if text.lower() in model.lower()]
        self.HS_phone_models = filtered_models
        self.HS_phone_list()

    def HS_display_image(self, index):
        item = self.ui.HS_Phone_List.itemFromIndex(index)
        if item is not None:
            selected_model = item.text()
            if selected_model in self.HS_image_paths:
                image_path = self.HS_image_paths[selected_model]
                pixmap = QPixmap(image_path)
                if pixmap.isNull():
                    QMessageBox.warning(self, "Image Not Found", "The image for this phone model is not found.")
                else:
                    # Get the viewport rectangle
                    viewport_rect = self.ui.HS_IMG_graphicsView.viewport().rect()

                    scene = QGraphicsScene(self)
                    pixmap_item = QGraphicsPixmapItem(pixmap)

                    # Scale pixmap to fit the viewport
                    pixmap_item.setTransformOriginPoint(pixmap.width() / 2, pixmap.height() / 2)
                    pixmap_item.setScale(min(viewport_rect.width() / pixmap.width(), viewport_rect.height() / pixmap.height()))

                    scene.addItem(pixmap_item)
                    self.ui.HS_IMG_graphicsView.setScene(scene)
            else:
                QMessageBox.warning(self, "Image Not Found", "No image found for this phone model.")



if __name__ == '__main__': 
    app = QApplication(sys.argv)
    win = T_point_Window()
    win.show() 
    # Run loop the app
    app.exec()
