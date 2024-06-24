# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResponsiveTPEqXpLo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import rc_ico
import rc_ico

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1140, 592)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/chip.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_12 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setStyleSheet(u"background-color: rgb(27, 38, 49);")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.background)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Menu_Frame = QFrame(self.background)
        self.Menu_Frame.setObjectName(u"Menu_Frame")
        self.Menu_Frame.setMinimumSize(QSize(0, 35))
        self.Menu_Frame.setMaximumSize(QSize(16777215, 35))
        self.Menu_Frame.setStyleSheet(u"background-color: rgb(23, 32, 42);\n"
"color: rgb(145, 145, 145);")
        self.Menu_Frame.setFrameShape(QFrame.StyledPanel)
        self.Menu_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Menu_Frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.window_ico = QPushButton(self.Menu_Frame)
        self.window_ico.setObjectName(u"window_ico")
        self.window_ico.setMinimumSize(QSize(30, 30))
        self.window_ico.setMaximumSize(QSize(30, 30))
        self.window_ico.setStyleSheet(u"border:0;")
        self.window_ico.setIcon(icon)
        self.window_ico.setFlat(True)

        self.horizontalLayout_6.addWidget(self.window_ico)

        self.label = QLabel(self.Menu_Frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(693, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.frame_4 = QFrame(self.Menu_Frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 35))
        self.frame_4.setMaximumSize(QSize(16777215, 35))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(16)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.frame_4)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMaximumSize(QSize(30, 30))
        self.minimize_btn.setStyleSheet(u"QPushButton{\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	border:0;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(27, 38, 49);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon1)
        self.minimize_btn.setFlat(False)

        self.horizontalLayout_5.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.frame_4)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setMaximumSize(QSize(30, 30))
        self.maximize_btn.setStyleSheet(u"QPushButton{\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	border:0;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(27, 38, 49);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon2)
        self.maximize_btn.setFlat(False)

        self.horizontalLayout_5.addWidget(self.maximize_btn)

        self.exit_btn = QPushButton(self.frame_4)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMaximumSize(QSize(30, 30))
        self.exit_btn.setStyleSheet(u"QPushButton{\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	border:0;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(235, 59, 90);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon3)
        self.exit_btn.setFlat(False)

        self.horizontalLayout_5.addWidget(self.exit_btn)


        self.horizontalLayout_6.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.Menu_Frame)

        self.header = QFrame(self.background)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 60))
        self.header.setStyleSheet(u"QFrame{\n"
"	border-image: url(:/newPrefix/icons/Header.png);\n"
"}")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.pushButton_12 = QPushButton(self.header)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(10, 14, 361, 31))
        font = QFont()
        font.setFamilies([u"Ubuntu Kurdish"])
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	background-color: 0;\n"
"	color: rgb(248, 248, 248);\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	padding-left:0px;\n"
"	padding-top: 0px;\n"
"	background-color: 0;\n"
"	border:0;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/LB.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon4)
        self.pushButton_12.setIconSize(QSize(60, 60))
        self.pushButton_12.setFlat(True)
        self.pushButton = QPushButton(self.header)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 20, 281, 24))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: 0;\n"
"	color: rgb(248, 248, 248);\n"
"	border:0;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	padding-left:0px;\n"
"	padding-top: 0px;\n"
"	background-color: 0;\n"
"	border:0;\n"
"}")
        self.pushButton.setFlat(True)

        self.verticalLayout.addWidget(self.header)

        self.body = QFrame(self.background)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.body)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 0, 6, 0)
        self.tabWidget = QTabWidget(self.body)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.tabWidget.setFont(font2)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"   padding-bottom:5px;\n"
"}\n"
"QTabBar::tab {\n"
"	background-color: rgb(23, 32, 42);\n"
"	padding:10px;\n"
"	color: rgb(243, 243, 243);\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color:rgb(46, 66, 84);\n"
"}")
        self.TP_TAB = QWidget()
        self.TP_TAB.setObjectName(u"TP_TAB")
        self.horizontalLayout = QHBoxLayout(self.TP_TAB)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 6, 0, 0)
        self.TP_frame = QFrame(self.TP_TAB)
        self.TP_frame.setObjectName(u"TP_frame")
        self.TP_frame.setMinimumSize(QSize(200, 0))
        self.TP_frame.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setBold(False)
        self.TP_frame.setFont(font3)
        self.TP_frame.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(61, 61, 61);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:8px;\n"
"	color: rgb(214, 219, 223);\n"
"	border-radius: 2px;\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:1px;\n"
"	padding-top: 1px;\n"
"	background-color:rgb(21, 30, 38);\n"
"}")
        self.TP_frame.setFrameShape(QFrame.StyledPanel)
        self.TP_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.TP_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.TP_XIAOMI_BTN = QPushButton(self.TP_frame)
        self.TP_XIAOMI_BTN.setObjectName(u"TP_XIAOMI_BTN")

        self.verticalLayout_5.addWidget(self.TP_XIAOMI_BTN)

        self.TP_SAMSUNG_BTN = QPushButton(self.TP_frame)
        self.TP_SAMSUNG_BTN.setObjectName(u"TP_SAMSUNG_BTN")

        self.verticalLayout_5.addWidget(self.TP_SAMSUNG_BTN)

        self.TP_HUAWEI_BTN = QPushButton(self.TP_frame)
        self.TP_HUAWEI_BTN.setObjectName(u"TP_HUAWEI_BTN")

        self.verticalLayout_5.addWidget(self.TP_HUAWEI_BTN)

        self.TP_VIVO_BTN = QPushButton(self.TP_frame)
        self.TP_VIVO_BTN.setObjectName(u"TP_VIVO_BTN")

        self.verticalLayout_5.addWidget(self.TP_VIVO_BTN)

        self.TP_OPPO_BTN = QPushButton(self.TP_frame)
        self.TP_OPPO_BTN.setObjectName(u"TP_OPPO_BTN")

        self.verticalLayout_5.addWidget(self.TP_OPPO_BTN)

        self.TP_LENOVO_BTN = QPushButton(self.TP_frame)
        self.TP_LENOVO_BTN.setObjectName(u"TP_LENOVO_BTN")

        self.verticalLayout_5.addWidget(self.TP_LENOVO_BTN)

        self.TP_VSMART_BTN = QPushButton(self.TP_frame)
        self.TP_VSMART_BTN.setObjectName(u"TP_VSMART_BTN")

        self.verticalLayout_5.addWidget(self.TP_VSMART_BTN)

        self.TP_NOKIA_BTN = QPushButton(self.TP_frame)
        self.TP_NOKIA_BTN.setObjectName(u"TP_NOKIA_BTN")

        self.verticalLayout_5.addWidget(self.TP_NOKIA_BTN)

        self.TP_AZUS_BTN = QPushButton(self.TP_frame)
        self.TP_AZUS_BTN.setObjectName(u"TP_AZUS_BTN")

        self.verticalLayout_5.addWidget(self.TP_AZUS_BTN)

        self.TP_LG_BTN = QPushButton(self.TP_frame)
        self.TP_LG_BTN.setObjectName(u"TP_LG_BTN")

        self.verticalLayout_5.addWidget(self.TP_LG_BTN)

        self.TP_MEIZU_BTN = QPushButton(self.TP_frame)
        self.TP_MEIZU_BTN.setObjectName(u"TP_MEIZU_BTN")

        self.verticalLayout_5.addWidget(self.TP_MEIZU_BTN)

        self.TP_MOTOROLA_BTN = QPushButton(self.TP_frame)
        self.TP_MOTOROLA_BTN.setObjectName(u"TP_MOTOROLA_BTN")

        self.verticalLayout_5.addWidget(self.TP_MOTOROLA_BTN)

        self.TP_INFINIX_BTN = QPushButton(self.TP_frame)
        self.TP_INFINIX_BTN.setObjectName(u"TP_INFINIX_BTN")

        self.verticalLayout_5.addWidget(self.TP_INFINIX_BTN)


        self.horizontalLayout.addWidget(self.TP_frame)

        self.frame_6 = QFrame(self.TP_TAB)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(300, 16777215))
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(61, 61, 61);\n"
"	border-radius:5px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.TP_Search_lineEdit = QLineEdit(self.frame_9)
        self.TP_Search_lineEdit.setObjectName(u"TP_Search_lineEdit")
        self.TP_Search_lineEdit.setStyleSheet(u"background-color: rgb(28, 40, 51);\n"
"image: url(:/newPrefix/icons/search.png);\n"
"image-position:right;\n"
"border:none;\n"
"border-bottom:1px solid #99A3A4;\n"
"color: rgb(149, 149, 149);\n"
"padding:5px;\n"
"")

        self.verticalLayout_3.addWidget(self.TP_Search_lineEdit)

        self.TP_Phone_List = QListWidget(self.frame_9)
        self.TP_Phone_List.setObjectName(u"TP_Phone_List")
        self.TP_Phone_List.setStyleSheet(u"QListWidget#TP_Phone_List {\n"
"	background-color: rgb(21, 30, 38);\n"
"	color: rgb(214, 219, 223);\n"
"	padding:5px 0 0 5px;\n"
"}\n"
"/* ScrollBar Vertical */\n"
"\n"
"QScrollBar::vertical{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	width:10px;\n"
"	margin:10px 0 10px 0;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	height:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-top-right-radius:2px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	height:10px;\n"
"	border-bottom-left-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	backgro"
                        "und:none;\n"
"}	\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background:none;\n"
"}	\n"
"\n"
"/* ScrollBar Horizontal */\n"
"\n"
"QScrollBar::horizontal{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	height:10px;\n"
"	margin:0 10px 0 10px;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::horizontal{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	width:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-bottom-left-radius:2px;\n"
"	subcontrol-position:left;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	width:10px;\n"
"	border-top-right-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:right;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"	background:non"
                        "e;\n"
"}	\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background:none;\n"
"}")
        self.TP_Phone_List.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.TP_Phone_List.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.verticalLayout_3.addWidget(self.TP_Phone_List)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(61, 61, 61);\n"
"	border-radius:5px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"color: rgb(145, 145, 145);\n"
"border:0;\n"
"font: 700 9pt \"Segoe UI\";")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 9, 0)
        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setItalic(False)
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(39, 55, 70);\n"
"	padding:7px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font: 700 8pt \"Segoe UI\";\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.TP_brand_name_label = QLabel(self.frame_11)
        self.TP_brand_name_label.setObjectName(u"TP_brand_name_label")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setItalic(False)
        self.TP_brand_name_label.setFont(font5)
        self.TP_brand_name_label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_3.addWidget(self.TP_brand_name_label, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_11, 0, Qt.AlignLeft)

        self.TP_IMG_graphicsView = QGraphicsView(self.frame_10)
        self.TP_IMG_graphicsView.setObjectName(u"TP_IMG_graphicsView")
        self.TP_IMG_graphicsView.setStyleSheet(u"/* ScrollBar Vertical */\n"
"\n"
"QScrollBar::vertical{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	width:10px;\n"
"	margin:10px 0 10px 0;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	height:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-top-right-radius:2px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	height:10px;\n"
"	border-bottom-left-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	background:none;\n"
"}	\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background:none;\n"
"}	\n"
"\n"
"/* ScrollBar Ho"
                        "rizontal */\n"
"\n"
"QScrollBar::horizontal{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	height:10px;\n"
"	margin:0 10px 0 10px;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::horizontal{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	width:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-bottom-left-radius:2px;\n"
"	subcontrol-position:left;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	width:10px;\n"
"	border-top-right-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:right;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"	background:none;\n"
"}	\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background:none;\n"
"}")
        self.TP_IMG_graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.TP_IMG_graphicsView.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        self.verticalLayout_4.addWidget(self.TP_IMG_graphicsView)


        self.horizontalLayout_2.addWidget(self.frame_10)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 40))
        self.frame_8.setMaximumSize(QSize(16777215, 40))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.SUPPORT_BTN = QPushButton(self.frame_8)
        self.SUPPORT_BTN.setObjectName(u"SUPPORT_BTN")
        self.SUPPORT_BTN.setGeometry(QRect(2, 8, 111, 31))
        self.SUPPORT_BTN.setLayoutDirection(Qt.LeftToRight)
        self.SUPPORT_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(21, 30, 38);\n"
"}\n"
"QPushButton::pressed{	\n"
"	background-color: rgb(46, 65, 84);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/global-security.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SUPPORT_BTN.setIcon(icon6)
        self.SOURCE_BTN = QPushButton(self.frame_8)
        self.SOURCE_BTN.setObjectName(u"SOURCE_BTN")
        self.SOURCE_BTN.setGeometry(QRect(121, 8, 111, 31))
        self.SOURCE_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(21, 30, 38);\n"
"}\n"
"QPushButton::pressed{	\n"
"	background-color: rgb(46, 65, 84);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/coding.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SOURCE_BTN.setIcon(icon7)
        self.Video_BTN = QPushButton(self.frame_8)
        self.Video_BTN.setObjectName(u"Video_BTN")
        self.Video_BTN.setGeometry(QRect(239, 8, 121, 31))
        self.Video_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(21, 30, 38);\n"
"}\n"
"QPushButton::pressed{	\n"
"	background-color: rgb(46, 65, 84);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Video_BTN.setIcon(icon8)

        self.verticalLayout_2.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_6)

        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/icons/paper-pin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.TP_TAB, icon9, "")
        self.ISP_TAB = QWidget()
        self.ISP_TAB.setObjectName(u"ISP_TAB")
        self.horizontalLayout_9 = QHBoxLayout(self.ISP_TAB)
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 6, 0, 0)
        self.ISP_frame = QFrame(self.ISP_TAB)
        self.ISP_frame.setObjectName(u"ISP_frame")
        self.ISP_frame.setMinimumSize(QSize(200, 0))
        self.ISP_frame.setMaximumSize(QSize(200, 16777215))
        self.ISP_frame.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(61, 61, 61);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:8px;\n"
"	color: rgb(214, 219, 223);\n"
"	border-radius: 2px;\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:1px;\n"
"	padding-top: 1px;\n"
"	background-color:rgb(21, 30, 38);\n"
"}")
        self.ISP_frame.setFrameShape(QFrame.StyledPanel)
        self.ISP_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ISP_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ISP_XIAOMI_BTN = QPushButton(self.ISP_frame)
        self.ISP_XIAOMI_BTN.setObjectName(u"ISP_XIAOMI_BTN")

        self.verticalLayout_6.addWidget(self.ISP_XIAOMI_BTN)

        self.ISP_SAMSUNG_BTN = QPushButton(self.ISP_frame)
        self.ISP_SAMSUNG_BTN.setObjectName(u"ISP_SAMSUNG_BTN")

        self.verticalLayout_6.addWidget(self.ISP_SAMSUNG_BTN)

        self.ISP_HUAWEI_BTN = QPushButton(self.ISP_frame)
        self.ISP_HUAWEI_BTN.setObjectName(u"ISP_HUAWEI_BTN")

        self.verticalLayout_6.addWidget(self.ISP_HUAWEI_BTN)

        self.ISP_VIVO_BTN = QPushButton(self.ISP_frame)
        self.ISP_VIVO_BTN.setObjectName(u"ISP_VIVO_BTN")

        self.verticalLayout_6.addWidget(self.ISP_VIVO_BTN)

        self.ISP_OPPO_BTN = QPushButton(self.ISP_frame)
        self.ISP_OPPO_BTN.setObjectName(u"ISP_OPPO_BTN")

        self.verticalLayout_6.addWidget(self.ISP_OPPO_BTN)

        self.ISP_LENOVO_BTN = QPushButton(self.ISP_frame)
        self.ISP_LENOVO_BTN.setObjectName(u"ISP_LENOVO_BTN")

        self.verticalLayout_6.addWidget(self.ISP_LENOVO_BTN)

        self.ISP_VSMART_BTN = QPushButton(self.ISP_frame)
        self.ISP_VSMART_BTN.setObjectName(u"ISP_VSMART_BTN")

        self.verticalLayout_6.addWidget(self.ISP_VSMART_BTN)

        self.ISP_NOKIA_BTN = QPushButton(self.ISP_frame)
        self.ISP_NOKIA_BTN.setObjectName(u"ISP_NOKIA_BTN")

        self.verticalLayout_6.addWidget(self.ISP_NOKIA_BTN)

        self.ISP_AZUS_BTN = QPushButton(self.ISP_frame)
        self.ISP_AZUS_BTN.setObjectName(u"ISP_AZUS_BTN")

        self.verticalLayout_6.addWidget(self.ISP_AZUS_BTN)

        self.ISP_LG_BTN = QPushButton(self.ISP_frame)
        self.ISP_LG_BTN.setObjectName(u"ISP_LG_BTN")

        self.verticalLayout_6.addWidget(self.ISP_LG_BTN)

        self.ISP_MEIZU_BTN = QPushButton(self.ISP_frame)
        self.ISP_MEIZU_BTN.setObjectName(u"ISP_MEIZU_BTN")

        self.verticalLayout_6.addWidget(self.ISP_MEIZU_BTN)

        self.ISP_MOTOROLA_BTN = QPushButton(self.ISP_frame)
        self.ISP_MOTOROLA_BTN.setObjectName(u"ISP_MOTOROLA_BTN")

        self.verticalLayout_6.addWidget(self.ISP_MOTOROLA_BTN)

        self.ISP_INFINIX_BTN = QPushButton(self.ISP_frame)
        self.ISP_INFINIX_BTN.setObjectName(u"ISP_INFINIX_BTN")

        self.verticalLayout_6.addWidget(self.ISP_INFINIX_BTN)


        self.horizontalLayout_9.addWidget(self.ISP_frame)

        self.frame_16 = QFrame(self.ISP_TAB)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_16)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(300, 16777215))
        self.frame_18.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(61, 61, 61);\n"
"	border-radius:5px;\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_18)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.ISP_Search_lineEdit = QLineEdit(self.frame_18)
        self.ISP_Search_lineEdit.setObjectName(u"ISP_Search_lineEdit")
        self.ISP_Search_lineEdit.setStyleSheet(u"background-color: rgb(28, 40, 51);\n"
"image: url(:/newPrefix/icons/search.png);\n"
"image-position:right;\n"
"border:none;\n"
"border-bottom:1px solid #99A3A4;\n"
"color: rgb(149, 149, 149);\n"
"padding:5px;\n"
"")

        self.verticalLayout_8.addWidget(self.ISP_Search_lineEdit)

        self.ISP_Phone_List = QListWidget(self.frame_18)
        self.ISP_Phone_List.setObjectName(u"ISP_Phone_List")
        self.ISP_Phone_List.setStyleSheet(u"QListWidget#ISP_Phone_List {\n"
"	background-color: rgb(21, 30, 38);\n"
"	color: rgb(214, 219, 223);\n"
"	padding:5px 0 0 5px;\n"
"}\n"
"/* ScrollBar Vertical */\n"
"\n"
"QScrollBar::vertical{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	width:10px;\n"
"	margin:10px 0 10px 0;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	height:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-top-right-radius:2px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	height:10px;\n"
"	border-bottom-left-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	backgr"
                        "ound:none;\n"
"}	\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background:none;\n"
"}	\n"
"\n"
"/* ScrollBar Horizontal */\n"
"\n"
"QScrollBar::horizontal{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	height:10px;\n"
"	margin:0 10px 0 10px;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::horizontal{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	width:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-bottom-left-radius:2px;\n"
"	subcontrol-position:left;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	width:10px;\n"
"	border-top-right-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:right;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"	background:no"
                        "ne;\n"
"}	\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background:none;\n"
"}")

        self.verticalLayout_8.addWidget(self.ISP_Phone_List)


        self.horizontalLayout_7.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(61, 61, 61);\n"
"	border-radius:5px;\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_19)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"color: rgb(145, 145, 145);\n"
"border:0;\n"
"font: 700 9pt \"Segoe UI\";")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, -1, 0)
        self.pushButton_3 = QPushButton(self.frame_20)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(39, 55, 70);\n"
"	padding:7px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font: 700 8pt \"Segoe UI\";\n"
"}\n"
"")
        self.pushButton_3.setIcon(icon5)

        self.horizontalLayout_8.addWidget(self.pushButton_3)

        self.ISP_brand_name_label = QLabel(self.frame_20)
        self.ISP_brand_name_label.setObjectName(u"ISP_brand_name_label")
        self.ISP_brand_name_label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.ISP_brand_name_label, 0, Qt.AlignLeft)


        self.verticalLayout_9.addWidget(self.frame_20, 0, Qt.AlignLeft)

        self.ISP_IMG_graphicsView = QGraphicsView(self.frame_19)
        self.ISP_IMG_graphicsView.setObjectName(u"ISP_IMG_graphicsView")
        self.ISP_IMG_graphicsView.setStyleSheet(u"/* ScrollBar Vertical */\n"
"\n"
"QScrollBar::vertical{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	width:10px;\n"
"	margin:10px 0 10px 0;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	height:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-top-right-radius:2px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	height:10px;\n"
"	border-bottom-left-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	background:none;\n"
"}	\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background:none;\n"
"}	\n"
"\n"
"/* ScrollBar Ho"
                        "rizontal */\n"
"\n"
"QScrollBar::horizontal{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	height:10px;\n"
"	margin:0 10px 0 10px;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::horizontal{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	width:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-bottom-left-radius:2px;\n"
"	subcontrol-position:left;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	width:10px;\n"
"	border-top-right-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:right;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"	background:none;\n"
"}	\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background:none;\n"
"}")
        self.ISP_IMG_graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.ISP_IMG_graphicsView.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        self.verticalLayout_9.addWidget(self.ISP_IMG_graphicsView)


        self.horizontalLayout_7.addWidget(self.frame_19)


        self.verticalLayout_7.addWidget(self.frame_17)

        self.frame_21 = QFrame(self.frame_16)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 40))
        self.frame_21.setMaximumSize(QSize(16777215, 40))
        self.frame_21.setStyleSheet(u"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.SUPPORT_BTN_2 = QPushButton(self.frame_21)
        self.SUPPORT_BTN_2.setObjectName(u"SUPPORT_BTN_2")
        self.SUPPORT_BTN_2.setGeometry(QRect(2, 8, 111, 31))
        self.SUPPORT_BTN_2.setLayoutDirection(Qt.LeftToRight)
        self.SUPPORT_BTN_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(21, 30, 38);\n"
"}\n"
"QPushButton::pressed{	\n"
"	background-color: rgb(46, 65, 84);\n"
"}")
        self.SUPPORT_BTN_2.setIcon(icon6)
        self.SOURCE_BTN_2 = QPushButton(self.frame_21)
        self.SOURCE_BTN_2.setObjectName(u"SOURCE_BTN_2")
        self.SOURCE_BTN_2.setGeometry(QRect(121, 8, 111, 31))
        self.SOURCE_BTN_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(21, 30, 38);\n"
"}\n"
"QPushButton::pressed{	\n"
"	background-color: rgb(46, 65, 84);\n"
"}")
        self.SOURCE_BTN_2.setIcon(icon7)
        self.Video_BTN1 = QPushButton(self.frame_21)
        self.Video_BTN1.setObjectName(u"Video_BTN1")
        self.Video_BTN1.setGeometry(QRect(239, 8, 121, 31))
        self.Video_BTN1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(21, 30, 38);\n"
"}\n"
"QPushButton::pressed{	\n"
"	background-color: rgb(46, 65, 84);\n"
"}")
        self.Video_BTN1.setIcon(icon8)

        self.verticalLayout_7.addWidget(self.frame_21)


        self.horizontalLayout_9.addWidget(self.frame_16)

        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/icons/cpu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.ISP_TAB, icon10, "")
        self.HS_TAB = QWidget()
        self.HS_TAB.setObjectName(u"HS_TAB")
        self.horizontalLayout_13 = QHBoxLayout(self.HS_TAB)
        self.horizontalLayout_13.setSpacing(4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 6, 0, 0)
        self.HS_frame = QFrame(self.HS_TAB)
        self.HS_frame.setObjectName(u"HS_frame")
        self.HS_frame.setMinimumSize(QSize(200, 0))
        self.HS_frame.setMaximumSize(QSize(200, 16777215))
        self.HS_frame.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(61, 61, 61);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:8px;\n"
"	color: rgb(214, 219, 223);\n"
"	border-radius: 2px;\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(92, 209, 115);\n"
"}\n"
"QPushButton::pressed{\n"
"	padding-left:1px;\n"
"	padding-top: 1px;\n"
"	background-color:rgb(21, 30, 38);\n"
"}")
        self.HS_frame.setFrameShape(QFrame.StyledPanel)
        self.HS_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.HS_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.HS_XIAOMI_BTN = QPushButton(self.HS_frame)
        self.HS_XIAOMI_BTN.setObjectName(u"HS_XIAOMI_BTN")

        self.verticalLayout_10.addWidget(self.HS_XIAOMI_BTN)

        self.HS_SAMSUNG_BTN = QPushButton(self.HS_frame)
        self.HS_SAMSUNG_BTN.setObjectName(u"HS_SAMSUNG_BTN")

        self.verticalLayout_10.addWidget(self.HS_SAMSUNG_BTN)

        self.HS_HUAWEI_BTN = QPushButton(self.HS_frame)
        self.HS_HUAWEI_BTN.setObjectName(u"HS_HUAWEI_BTN")

        self.verticalLayout_10.addWidget(self.HS_HUAWEI_BTN)

        self.HS_VIVO_BTN = QPushButton(self.HS_frame)
        self.HS_VIVO_BTN.setObjectName(u"HS_VIVO_BTN")

        self.verticalLayout_10.addWidget(self.HS_VIVO_BTN)

        self.HS_OPPO_BTN = QPushButton(self.HS_frame)
        self.HS_OPPO_BTN.setObjectName(u"HS_OPPO_BTN")

        self.verticalLayout_10.addWidget(self.HS_OPPO_BTN)

        self.HS_LENOVO_BTN = QPushButton(self.HS_frame)
        self.HS_LENOVO_BTN.setObjectName(u"HS_LENOVO_BTN")

        self.verticalLayout_10.addWidget(self.HS_LENOVO_BTN)

        self.HS_VSMART_BTN = QPushButton(self.HS_frame)
        self.HS_VSMART_BTN.setObjectName(u"HS_VSMART_BTN")

        self.verticalLayout_10.addWidget(self.HS_VSMART_BTN)

        self.HS_NOKIA_BTN = QPushButton(self.HS_frame)
        self.HS_NOKIA_BTN.setObjectName(u"HS_NOKIA_BTN")

        self.verticalLayout_10.addWidget(self.HS_NOKIA_BTN)

        self.HS_AZUS_BTN = QPushButton(self.HS_frame)
        self.HS_AZUS_BTN.setObjectName(u"HS_AZUS_BTN")

        self.verticalLayout_10.addWidget(self.HS_AZUS_BTN)

        self.HS_LG_BTN = QPushButton(self.HS_frame)
        self.HS_LG_BTN.setObjectName(u"HS_LG_BTN")

        self.verticalLayout_10.addWidget(self.HS_LG_BTN)

        self.HS_MEIZU_BTN = QPushButton(self.HS_frame)
        self.HS_MEIZU_BTN.setObjectName(u"HS_MEIZU_BTN")

        self.verticalLayout_10.addWidget(self.HS_MEIZU_BTN)

        self.HS_MOTOROLA_BTN = QPushButton(self.HS_frame)
        self.HS_MOTOROLA_BTN.setObjectName(u"HS_MOTOROLA_BTN")

        self.verticalLayout_10.addWidget(self.HS_MOTOROLA_BTN)

        self.HS_INFINIX_BTN = QPushButton(self.HS_frame)
        self.HS_INFINIX_BTN.setObjectName(u"HS_INFINIX_BTN")

        self.verticalLayout_10.addWidget(self.HS_INFINIX_BTN)


        self.horizontalLayout_13.addWidget(self.HS_frame)

        self.frame_23 = QFrame(self.HS_TAB)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_23)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(300, 16777215))
        self.frame_25.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(61, 61, 61);\n"
"	border-radius:5px;\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_25)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.HS_Search_lineEdit = QLineEdit(self.frame_25)
        self.HS_Search_lineEdit.setObjectName(u"HS_Search_lineEdit")
        self.HS_Search_lineEdit.setStyleSheet(u"background-color: rgb(28, 40, 51);\n"
"image: url(:/newPrefix/icons/search.png);\n"
"image-position:right;\n"
"border:none;\n"
"border-bottom:1px solid #99A3A4;\n"
"color: rgb(149, 149, 149);\n"
"padding:5px;\n"
"")

        self.verticalLayout_12.addWidget(self.HS_Search_lineEdit)

        self.HS_Phone_List = QListWidget(self.frame_25)
        self.HS_Phone_List.setObjectName(u"HS_Phone_List")
        self.HS_Phone_List.setStyleSheet(u"QListWidget#HS_Phone_List {\n"
"	background-color: rgb(21, 30, 38);\n"
"	color: rgb(214, 219, 223);\n"
"	padding:5px 0 0 5px;\n"
"}\n"
"/* ScrollBar Vertical */\n"
"\n"
"QScrollBar::vertical{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	width:10px;\n"
"	margin:10px 0 10px 0;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	height:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-top-right-radius:2px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	height:10px;\n"
"	border-bottom-left-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	backgro"
                        "und:none;\n"
"}	\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background:none;\n"
"}	\n"
"\n"
"/* ScrollBar Horizontal */\n"
"\n"
"QScrollBar::horizontal{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	height:10px;\n"
"	margin:0 10px 0 10px;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::horizontal{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	width:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-bottom-left-radius:2px;\n"
"	subcontrol-position:left;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	width:10px;\n"
"	border-top-right-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:right;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"	background:non"
                        "e;\n"
"}	\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background:none;\n"
"}")

        self.verticalLayout_12.addWidget(self.HS_Phone_List)


        self.horizontalLayout_10.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(61, 61, 61);\n"
"	border-radius:5px;\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_26)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"color: rgb(145, 145, 145);\n"
"border:0;\n"
"font: 700 9pt \"Segoe UI\";")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, -1, 0)
        self.pushButton_4 = QPushButton(self.frame_27)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(39, 55, 70);\n"
"	padding:7px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font: 700 8pt \"Segoe UI\";\n"
"}\n"
"")
        self.pushButton_4.setIcon(icon5)

        self.horizontalLayout_11.addWidget(self.pushButton_4)

        self.HS_brand_name_label = QLabel(self.frame_27)
        self.HS_brand_name_label.setObjectName(u"HS_brand_name_label")
        self.HS_brand_name_label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_11.addWidget(self.HS_brand_name_label, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.frame_27, 0, Qt.AlignLeft)

        self.HS_IMG_graphicsView = QGraphicsView(self.frame_26)
        self.HS_IMG_graphicsView.setObjectName(u"HS_IMG_graphicsView")
        self.HS_IMG_graphicsView.setStyleSheet(u"/* ScrollBar Vertical */\n"
"\n"
"QScrollBar::vertical{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	width:10px;\n"
"	margin:10px 0 10px 0;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	height:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-top-right-radius:2px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	height:10px;\n"
"	border-bottom-left-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	background:none;\n"
"}	\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background:none;\n"
"}	\n"
"\n"
"/* ScrollBar Ho"
                        "rizontal */\n"
"\n"
"QScrollBar::horizontal{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	height:10px;\n"
"	margin:0 10px 0 10px;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::horizontal{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	width:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-bottom-left-radius:2px;\n"
"	subcontrol-position:left;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	width:10px;\n"
"	border-top-right-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:right;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"	background:none;\n"
"}	\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background:none;\n"
"}")
        self.HS_IMG_graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.HS_IMG_graphicsView.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        self.verticalLayout_13.addWidget(self.HS_IMG_graphicsView)


        self.horizontalLayout_10.addWidget(self.frame_26)


        self.verticalLayout_11.addWidget(self.frame_24)

        self.frame_28 = QFrame(self.frame_23)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 40))
        self.frame_28.setMaximumSize(QSize(16777215, 40))
        self.frame_28.setStyleSheet(u"")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.SUPPORT_BTN_3 = QPushButton(self.frame_28)
        self.SUPPORT_BTN_3.setObjectName(u"SUPPORT_BTN_3")
        self.SUPPORT_BTN_3.setGeometry(QRect(2, 8, 111, 31))
        self.SUPPORT_BTN_3.setLayoutDirection(Qt.LeftToRight)
        self.SUPPORT_BTN_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(21, 30, 38);\n"
"}\n"
"QPushButton::pressed{	\n"
"	background-color: rgb(46, 65, 84);\n"
"}")
        self.SUPPORT_BTN_3.setIcon(icon6)
        self.SOURCE_BTN_3 = QPushButton(self.frame_28)
        self.SOURCE_BTN_3.setObjectName(u"SOURCE_BTN_3")
        self.SOURCE_BTN_3.setGeometry(QRect(121, 8, 111, 31))
        self.SOURCE_BTN_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(21, 30, 38);\n"
"}\n"
"QPushButton::pressed{	\n"
"	background-color: rgb(46, 65, 84);\n"
"}")
        self.SOURCE_BTN_3.setIcon(icon7)
        self.Video_BTN2 = QPushButton(self.frame_28)
        self.Video_BTN2.setObjectName(u"Video_BTN2")
        self.Video_BTN2.setGeometry(QRect(239, 8, 121, 31))
        self.Video_BTN2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(21, 30, 38);\n"
"}\n"
"QPushButton::pressed{\n"
"	\n"
"	background-color: rgb(46, 65, 84);\n"
"}")
        self.Video_BTN2.setIcon(icon8)

        self.verticalLayout_11.addWidget(self.frame_28)


        self.horizontalLayout_13.addWidget(self.frame_23)

        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/icons/tools.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.HS_TAB, icon11, "")
        self.SD_TAB = QWidget()
        self.SD_TAB.setObjectName(u"SD_TAB")
        self.gridLayout = QGridLayout(self.SD_TAB)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 6, 0, 0)
        self.frame_29 = QFrame(self.SD_TAB)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(300, 0))
        self.frame_29.setMaximumSize(QSize(300, 16777215))
        self.frame_29.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(61, 61, 61);\n"
"	border-radius:5px;\n"
"}\n"
"")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_29)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.SD_Search_lineEdit = QLineEdit(self.frame_29)
        self.SD_Search_lineEdit.setObjectName(u"SD_Search_lineEdit")
        self.SD_Search_lineEdit.setStyleSheet(u"background-color: rgb(28, 40, 51);\n"
"image: url(:/newPrefix/icons/search.png);\n"
"image-position:right;\n"
"border:none;\n"
"border-bottom:1px solid #99A3A4;\n"
"color: rgb(149, 149, 149);\n"
"padding:5px;\n"
"")

        self.verticalLayout_14.addWidget(self.SD_Search_lineEdit)

        self.treeWidget = QTreeWidget(self.frame_29)
        icon12 = QIcon()
        icon12.addFile(u":/newPrefix/icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        icon13 = QIcon()
        icon13.addFile(u":/newPrefix/icons/app.png", QSize(), QIcon.Normal, QIcon.Off)
        icon14 = QIcon()
        icon14.addFile(u":/newPrefix/icons/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        icon15 = QIcon()
        icon15.addFile(u":/newPrefix/icons/Appel_folder.png", QSize(), QIcon.Normal, QIcon.Off)
        icon16 = QIcon()
        icon16.addFile(u":/newPrefix/icons/iPhone.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem.setIcon(0, icon12);
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1.setIcon(0, icon13);
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setIcon(0, icon14);
        __qtreewidgetitem3 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem3.setIcon(0, icon12);
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem4.setIcon(0, icon13);
        __qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5.setIcon(0, icon14);
        __qtreewidgetitem6 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem6.setIcon(0, icon12);
        __qtreewidgetitem7 = QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7.setIcon(0, icon13);
        __qtreewidgetitem8 = QTreeWidgetItem(__qtreewidgetitem7)
        __qtreewidgetitem8.setIcon(0, icon14);
        __qtreewidgetitem9 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem9.setIcon(0, icon12);
        __qtreewidgetitem10 = QTreeWidgetItem(__qtreewidgetitem9)
        __qtreewidgetitem10.setIcon(0, icon13);
        __qtreewidgetitem11 = QTreeWidgetItem(__qtreewidgetitem10)
        __qtreewidgetitem11.setIcon(0, icon14);
        __qtreewidgetitem12 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem12.setIcon(0, icon12);
        __qtreewidgetitem13 = QTreeWidgetItem(__qtreewidgetitem12)
        __qtreewidgetitem13.setIcon(0, icon13);
        __qtreewidgetitem14 = QTreeWidgetItem(__qtreewidgetitem13)
        __qtreewidgetitem14.setIcon(0, icon14);
        __qtreewidgetitem15 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem15.setIcon(0, icon12);
        __qtreewidgetitem16 = QTreeWidgetItem(__qtreewidgetitem15)
        __qtreewidgetitem16.setIcon(0, icon13);
        __qtreewidgetitem17 = QTreeWidgetItem(__qtreewidgetitem16)
        __qtreewidgetitem17.setIcon(0, icon14);
        __qtreewidgetitem18 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem18.setIcon(0, icon12);
        __qtreewidgetitem19 = QTreeWidgetItem(__qtreewidgetitem18)
        __qtreewidgetitem19.setIcon(0, icon13);
        __qtreewidgetitem20 = QTreeWidgetItem(__qtreewidgetitem19)
        __qtreewidgetitem20.setIcon(0, icon14);
        __qtreewidgetitem21 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem21.setIcon(0, icon12);
        __qtreewidgetitem22 = QTreeWidgetItem(__qtreewidgetitem21)
        __qtreewidgetitem22.setIcon(0, icon13);
        __qtreewidgetitem23 = QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem23.setIcon(0, icon14);
        __qtreewidgetitem24 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem24.setIcon(0, icon15);
        __qtreewidgetitem25 = QTreeWidgetItem(__qtreewidgetitem24)
        __qtreewidgetitem25.setIcon(0, icon16);
        __qtreewidgetitem26 = QTreeWidgetItem(__qtreewidgetitem25)
        __qtreewidgetitem26.setIcon(0, icon14);
        __qtreewidgetitem27 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem27.setIcon(0, icon15);
        __qtreewidgetitem28 = QTreeWidgetItem(__qtreewidgetitem27)
        __qtreewidgetitem28.setIcon(0, icon16);
        __qtreewidgetitem29 = QTreeWidgetItem(__qtreewidgetitem28)
        __qtreewidgetitem29.setIcon(0, icon14);
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setStyleSheet(u"QTreeWidget#treeWidget {\n"
"	border:1px solid rgb(61, 61, 61);\n"
"	color: rgb(214, 219, 223);\n"
"	padding-top:10px;\n"
"}\n"
"/* ScrollBar Vertical */\n"
"\n"
"QScrollBar::vertical{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	width:10px;\n"
"	margin:10px 0 10px 0;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	height:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-top-right-radius:2px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	height:10px;\n"
"	border-bottom-left-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	background:non"
                        "e;\n"
"}	\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background:none;\n"
"}	\n"
"\n"
"/* ScrollBar Horizontal */\n"
"\n"
"QScrollBar::horizontal{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	height:10px;\n"
"	margin:0 10px 0 10px;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::horizontal{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	width:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-bottom-left-radius:2px;\n"
"	subcontrol-position:left;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	width:10px;\n"
"	border-top-right-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:right;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"	background:none;\n"
""
                        "}	\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background:none;\n"
"}")
        self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.treeWidget.setIconSize(QSize(16, 16))
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setAnimated(True)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setCascadingSectionResizes(False)

        self.verticalLayout_14.addWidget(self.treeWidget)


        self.gridLayout.addWidget(self.frame_29, 0, 0, 1, 1)

        self.frame_30 = QFrame(self.SD_TAB)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_30)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"QFrame{\n"
"	border:1px solid rgb(61, 61, 61);\n"
"	border-radius:5px;\n"
"}")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_33)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"color: rgb(145, 145, 145);\n"
"border:0;\n"
"font: 700 9pt \"Segoe UI\";")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, -1, 0)
        self.pushButton_5 = QPushButton(self.frame_34)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(39, 55, 70);\n"
"	padding:7px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"	font: 700 8pt \"Segoe UI\";\n"
"}\n"
"")
        self.pushButton_5.setIcon(icon5)

        self.horizontalLayout_15.addWidget(self.pushButton_5)

        self.SD_brand_name_label = QLabel(self.frame_34)
        self.SD_brand_name_label.setObjectName(u"SD_brand_name_label")
        self.SD_brand_name_label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_15.addWidget(self.SD_brand_name_label, 0, Qt.AlignLeft)


        self.verticalLayout_17.addWidget(self.frame_34, 0, Qt.AlignLeft)

        self.SD_PDF_graphicsView = QGraphicsView(self.frame_33)
        self.SD_PDF_graphicsView.setObjectName(u"SD_PDF_graphicsView")
        self.SD_PDF_graphicsView.setStyleSheet(u"/* ScrollBar Vertical */\n"
"\n"
"QScrollBar::vertical{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	width:10px;\n"
"	margin:10px 0 10px 0;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::vertical{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	height:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-top-right-radius:2px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	height:10px;\n"
"	border-bottom-left-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	background:none;\n"
"}	\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background:none;\n"
"}	\n"
"\n"
"/* ScrollBar Ho"
                        "rizontal */\n"
"\n"
"QScrollBar::horizontal{\n"
"	border:none;\n"
"	background-color:rgb(39, 55, 70);\n"
"	height:10px;\n"
"	margin:0 10px 0 10px;\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QScrollBar::handle::horizontal{\n"
"	background-color:rgb(17, 24, 31);\n"
"	border-radius:2px;\n"
"	min-height:30px;\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"	border:none;\n"
"	background-color: #151515;\n"
"	width:10px;\n"
"	border-top-left-radius:2px;\n"
"	border-bottom-left-radius:2px;\n"
"	subcontrol-position:left;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"	border:none;\n"
"	background-color:#151515;\n"
"	width:10px;\n"
"	border-top-right-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	subcontrol-position:right;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
"	background:none;\n"
"}	\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background:none;\n"
"}")
        self.SD_PDF_graphicsView.setRenderHints(QPainter.Antialiasing|QPainter.SmoothPixmapTransform)
        self.SD_PDF_graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.SD_PDF_graphicsView.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.SD_PDF_graphicsView.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)

        self.verticalLayout_17.addWidget(self.SD_PDF_graphicsView)


        self.horizontalLayout_14.addWidget(self.frame_33)


        self.verticalLayout_15.addWidget(self.frame_31)

        self.frame_35 = QFrame(self.frame_30)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 40))
        self.frame_35.setMaximumSize(QSize(16777215, 40))
        self.frame_35.setStyleSheet(u"")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.SUPPORT_BTN_4 = QPushButton(self.frame_35)
        self.SUPPORT_BTN_4.setObjectName(u"SUPPORT_BTN_4")
        self.SUPPORT_BTN_4.setGeometry(QRect(2, 8, 111, 31))
        self.SUPPORT_BTN_4.setLayoutDirection(Qt.LeftToRight)
        self.SUPPORT_BTN_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(21, 30, 38);\n"
"}\n"
"QPushButton::pressed{	\n"
"	background-color: rgb(46, 65, 84);\n"
"}")
        self.SUPPORT_BTN_4.setIcon(icon6)
        self.SOURCE_BTN_4 = QPushButton(self.frame_35)
        self.SOURCE_BTN_4.setObjectName(u"SOURCE_BTN_4")
        self.SOURCE_BTN_4.setGeometry(QRect(121, 8, 111, 31))
        self.SOURCE_BTN_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(21, 30, 38);\n"
"}\n"
"QPushButton::pressed{	\n"
"	background-color: rgb(46, 65, 84);\n"
"}")
        self.SOURCE_BTN_4.setIcon(icon7)
        self.Video_BTN3 = QPushButton(self.frame_35)
        self.Video_BTN3.setObjectName(u"Video_BTN3")
        self.Video_BTN3.setGeometry(QRect(239, 8, 121, 31))
        self.Video_BTN3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(17, 24, 31);\n"
"	padding:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(21, 30, 38);\n"
"}\n"
"QPushButton::pressed{	\n"
"	background-color: rgb(46, 65, 84);\n"
"}")
        self.Video_BTN3.setIcon(icon8)

        self.verticalLayout_15.addWidget(self.frame_35)


        self.gridLayout.addWidget(self.frame_30, 0, 1, 1, 1)

        icon17 = QIcon()
        icon17.addFile(u":/newPrefix/icons/Pdf_folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.SD_TAB, icon17, "")
        self.SC_TAB = QWidget()
        self.SC_TAB.setObjectName(u"SC_TAB")
        icon18 = QIcon()
        icon18.addFile(u":/newPrefix/icons/key.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.SC_TAB, icon18, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.body)

        self.status = QFrame(self.background)
        self.status.setObjectName(u"status")
        self.status.setMinimumSize(QSize(0, 25))
        self.status.setMaximumSize(QSize(16777215, 25))
        self.status.setStyleSheet(u"background-color: rgb(23, 32, 42);\n"
"color: rgb(145, 145, 145);\n"
"border:0;")
        self.status.setFrameShape(QFrame.StyledPanel)
        self.status.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.status)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.frame_12 = QFrame(self.status)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.pushButton_16 = QPushButton(self.frame_12)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(0, 0, 31, 24))
        icon19 = QIcon()
        icon19.addFile(u":/newPrefix/icons/clock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon19)
        self.pushButton_16.setFlat(True)
        self.time_label = QLabel(self.frame_12)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(30, 4, 211, 16))

        self.horizontalLayout_4.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.status)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.pushButton_17 = QPushButton(self.frame_13)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(10, 0, 31, 24))
        icon20 = QIcon()
        icon20.addFile(u":/newPrefix/icons/window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon20)
        self.pushButton_17.setFlat(True)
        self.system_label = QLabel(self.frame_13)
        self.system_label.setObjectName(u"system_label")
        self.system_label.setGeometry(QRect(40, 4, 281, 16))

        self.horizontalLayout_4.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.status)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(200, 16777215))
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.pushButton_18 = QPushButton(self.frame_14)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(50, 0, 31, 24))
        icon21 = QIcon()
        icon21.addFile(u":/newPrefix/icons/account.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon21)
        self.pushButton_18.setFlat(True)
        self.user_label = QLabel(self.frame_14)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setGeometry(QRect(80, 4, 121, 16))

        self.horizontalLayout_4.addWidget(self.frame_14)


        self.verticalLayout.addWidget(self.status)


        self.horizontalLayout_12.addWidget(self.background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.window_ico.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Laroussi Android Board Tool V1.0 | https://laroussigsm.net/", None))
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.exit_btn.setText("")
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u" LAROUSSI ANDROID BOARD", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" TP/ISP/H-SOLUTION & SCHEMATIC DIAGRAM", None))
        self.TP_XIAOMI_BTN.setText(QCoreApplication.translate("MainWindow", u"XIAOMI", None))
        self.TP_SAMSUNG_BTN.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.TP_HUAWEI_BTN.setText(QCoreApplication.translate("MainWindow", u"HUAWEI", None))
        self.TP_VIVO_BTN.setText(QCoreApplication.translate("MainWindow", u"VIVO", None))
        self.TP_OPPO_BTN.setText(QCoreApplication.translate("MainWindow", u"OPPO", None))
        self.TP_LENOVO_BTN.setText(QCoreApplication.translate("MainWindow", u"LENOVO", None))
        self.TP_VSMART_BTN.setText(QCoreApplication.translate("MainWindow", u"VSMART", None))
        self.TP_NOKIA_BTN.setText(QCoreApplication.translate("MainWindow", u"NOKIA", None))
        self.TP_AZUS_BTN.setText(QCoreApplication.translate("MainWindow", u"AZUS", None))
        self.TP_LG_BTN.setText(QCoreApplication.translate("MainWindow", u"LG", None))
        self.TP_MEIZU_BTN.setText(QCoreApplication.translate("MainWindow", u"MEIZU", None))
        self.TP_MOTOROLA_BTN.setText(QCoreApplication.translate("MainWindow", u"MOTOROLA", None))
        self.TP_INFINIX_BTN.setText(QCoreApplication.translate("MainWindow", u"INFINIX", None))
        self.TP_Search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Searching by model ....", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" TEST POINT LIST", None))
        self.TP_brand_name_label.setText(QCoreApplication.translate("MainWindow", u"No phone model selected yet !!", None))
        self.SUPPORT_BTN.setText(QCoreApplication.translate("MainWindow", u" Support", None))
        self.SOURCE_BTN.setText(QCoreApplication.translate("MainWindow", u" Source Code", None))
        self.Video_BTN.setText(QCoreApplication.translate("MainWindow", u" Video Tutorials ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TP_TAB), QCoreApplication.translate("MainWindow", u" TEST POINT", None))
        self.ISP_XIAOMI_BTN.setText(QCoreApplication.translate("MainWindow", u"XIAOMI", None))
        self.ISP_SAMSUNG_BTN.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.ISP_HUAWEI_BTN.setText(QCoreApplication.translate("MainWindow", u"HUAWEI", None))
        self.ISP_VIVO_BTN.setText(QCoreApplication.translate("MainWindow", u"VIVO", None))
        self.ISP_OPPO_BTN.setText(QCoreApplication.translate("MainWindow", u"OPPO", None))
        self.ISP_LENOVO_BTN.setText(QCoreApplication.translate("MainWindow", u"LENOVO", None))
        self.ISP_VSMART_BTN.setText(QCoreApplication.translate("MainWindow", u"VSMART", None))
        self.ISP_NOKIA_BTN.setText(QCoreApplication.translate("MainWindow", u"NOKIA", None))
        self.ISP_AZUS_BTN.setText(QCoreApplication.translate("MainWindow", u"AZUS", None))
        self.ISP_LG_BTN.setText(QCoreApplication.translate("MainWindow", u"LG", None))
        self.ISP_MEIZU_BTN.setText(QCoreApplication.translate("MainWindow", u"MEIZU", None))
        self.ISP_MOTOROLA_BTN.setText(QCoreApplication.translate("MainWindow", u"MOTOROLA", None))
        self.ISP_INFINIX_BTN.setText(QCoreApplication.translate("MainWindow", u"INFINIX", None))
        self.ISP_Search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Searching by model ....", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u" ISP PINOUT LIST", None))
        self.ISP_brand_name_label.setText(QCoreApplication.translate("MainWindow", u"No phone model selected yet !!", None))
        self.SUPPORT_BTN_2.setText(QCoreApplication.translate("MainWindow", u" Support", None))
        self.SOURCE_BTN_2.setText(QCoreApplication.translate("MainWindow", u" Source Code", None))
        self.Video_BTN1.setText(QCoreApplication.translate("MainWindow", u" Video Tutorials ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ISP_TAB), QCoreApplication.translate("MainWindow", u"ISP PINOUT", None))
        self.HS_XIAOMI_BTN.setText(QCoreApplication.translate("MainWindow", u"XIAOMI", None))
        self.HS_SAMSUNG_BTN.setText(QCoreApplication.translate("MainWindow", u"SAMSUNG", None))
        self.HS_HUAWEI_BTN.setText(QCoreApplication.translate("MainWindow", u"HUAWEI", None))
        self.HS_VIVO_BTN.setText(QCoreApplication.translate("MainWindow", u"VIVO", None))
        self.HS_OPPO_BTN.setText(QCoreApplication.translate("MainWindow", u"OPPO", None))
        self.HS_LENOVO_BTN.setText(QCoreApplication.translate("MainWindow", u"LENOVO", None))
        self.HS_VSMART_BTN.setText(QCoreApplication.translate("MainWindow", u"VSMART", None))
        self.HS_NOKIA_BTN.setText(QCoreApplication.translate("MainWindow", u"NOKIA", None))
        self.HS_AZUS_BTN.setText(QCoreApplication.translate("MainWindow", u"AZUS", None))
        self.HS_LG_BTN.setText(QCoreApplication.translate("MainWindow", u"LG", None))
        self.HS_MEIZU_BTN.setText(QCoreApplication.translate("MainWindow", u"MEIZU", None))
        self.HS_MOTOROLA_BTN.setText(QCoreApplication.translate("MainWindow", u"MOTOROLA", None))
        self.HS_INFINIX_BTN.setText(QCoreApplication.translate("MainWindow", u"INFINIX", None))
        self.HS_Search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Searching by model ....", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u" HARDWARE SOLUTIONS", None))
        self.HS_brand_name_label.setText(QCoreApplication.translate("MainWindow", u"No phone model selected yet !!", None))
        self.SUPPORT_BTN_3.setText(QCoreApplication.translate("MainWindow", u" Support", None))
        self.SOURCE_BTN_3.setText(QCoreApplication.translate("MainWindow", u" Source Code", None))
        self.Video_BTN2.setText(QCoreApplication.translate("MainWindow", u" Video Tutorials ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HS_TAB), QCoreApplication.translate("MainWindow", u"HARDWARE SOLUTIONS", None))
        self.SD_Search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Searching by model ....", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Huawei Schematics", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"HUAWEI Agassi2 MB Circuit schematic", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Hello.pdf", None));
        ___qtreewidgetitem4 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Samsung Schematics", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Samsung Galaxy A01 A015F Schematic", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"Hello.pdf", None));
        ___qtreewidgetitem7 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"Lenovo Schematics", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"Lenovo A278T Schematic Diagrams", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem8.child(0)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"Hello.pdf", None));
        ___qtreewidgetitem10 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"LG Schematics", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"LG ID2750 Service & Schematics", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem11.child(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"Hello.pdf", None));
        ___qtreewidgetitem13 = self.treeWidget.topLevelItem(4)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"Meizu Schematics", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem13.child(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"Meizu 16s schematics", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem14.child(0)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"Hello.pdf", None));
        ___qtreewidgetitem16 = self.treeWidget.topLevelItem(5)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"Nokia Schematic", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem16.child(0)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"Nokia lumia 510 Schematic", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem17.child(0)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"Hello.pdf", None));
        ___qtreewidgetitem19 = self.treeWidget.topLevelItem(6)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"Oppo Schematics", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem19.child(0)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"Oppo A11w (Joy 3) Schematic & Layout Diagrams", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem20.child(0)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"Hello.pdf", None));
        ___qtreewidgetitem22 = self.treeWidget.topLevelItem(7)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"Xiaomi Schematics", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem22.child(0)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"Xiaomi Redmi 8 (olive) Schematic", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem23.child(0)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"Hello.pdf", None));
        ___qtreewidgetitem25 = self.treeWidget.topLevelItem(8)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"iPhone Schematics", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem25.child(0)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"iPhone 2 N82 820-2186 Schematics Diagram", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem26.child(0)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"Hello.pdf", None));
        ___qtreewidgetitem28 = self.treeWidget.topLevelItem(9)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u"iPad Schematics", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem28.child(0)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"Apple ipad 2 K94 Chopin MLB 820-3069-A", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem29.child(0)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"Hello.pdf", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u" SCHEMATIC DIAGRAM", None))
        self.SD_brand_name_label.setText(QCoreApplication.translate("MainWindow", u"No phone model selected yet !!", None))
        self.SUPPORT_BTN_4.setText(QCoreApplication.translate("MainWindow", u" Support", None))
        self.SOURCE_BTN_4.setText(QCoreApplication.translate("MainWindow", u" Source Code", None))
        self.Video_BTN3.setText(QCoreApplication.translate("MainWindow", u" Video Tutorials ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SD_TAB), QCoreApplication.translate("MainWindow", u"SCHEMATIC DIAGRAM", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SC_TAB), QCoreApplication.translate("MainWindow", u"SERVICE CODES", None))
        self.pushButton_16.setText("")
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_17.setText("")
        self.system_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_18.setText("")
        self.user_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

