# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacemwExBx.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QVariantAnimation, QAbstractAnimation)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import resources_rc

Them_Code = 0

class PushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QVariantAnimation(
            startValue=QColor("#1A0057"),
            endValue=QColor("#6E25E6"),
            valueChanged=self._on_value_changed,
            duration=200,
        )
        self._update_stylesheet(QColor("#6E25E6"), QColor("white"))
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def _on_value_changed(self, color):
        foreground = (
            QColor("white")
            if self._animation.direction() == QAbstractAnimation.Forward
            else QColor("white")
        )
        self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background, foreground):
        self.setStyleSheet(
            """
        QPushButton{
            background-color: %s;
            color: %s;
        }
        """
            % (background.name(), foreground.name())
        )

    def enterEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)


class LineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QVariantAnimation(
            startValue=QColor("#6E25E6"),
            endValue=QColor("#101216"),
            valueChanged=self._on_value_changed,
            duration=200,
        )
        self._update_stylesheet(QColor("#101216"), QColor("white"))
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def _on_value_changed(self, color):
        foreground = (
            QColor("white")
            if self._animation.direction() == QAbstractAnimation.Forward
            else QColor("white")
        )
        self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background, foreground):
        self.setStyleSheet(
            """
        QLineEdit{
            border: 1px solid %s;
            color: %s;
        }
        """
            % (background.name(), foreground.name())
        )

    def focusInEvent(self, event) -> None:
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().focusInEvent(event)

    def focusOutEvent(self, event) -> None:
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().focusOutEvent(event)


class SpinBox(QSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QVariantAnimation(
            startValue=QColor("#6E25E6"),
            endValue=QColor("#101216"),
            valueChanged=self._on_value_changed,
            duration=200,
        )
        self._update_stylesheet(QColor("#101216"), QColor("white"))
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def _on_value_changed(self, color):
        foreground = (
            QColor("white")
            if self._animation.direction() == QAbstractAnimation.Forward
            else QColor("white")
        )
        self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background, foreground):
        self.setStyleSheet(
            """
        QSpinBox {
            border: 1px solid %s;
        }
        """
            % (background.name())
        )

    def focusInEvent(self, event) -> None:
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().focusInEvent(event)

    def focusOutEvent(self, event) -> None:
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().focusOutEvent(event)


class RadioButton(QRadioButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QVariantAnimation(
            startValue=QColor("#6E25E6"),
            endValue=QColor("#2d333d"),
            valueChanged=self._on_value_changed,
            duration=200,
        )
        self._update_stylesheet(QColor("#2d333d"), QColor("white"))
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def _on_value_changed(self, color):
        foreground = (
            QColor("white")
            if self._animation.direction() == QAbstractAnimation.Forward
            else QColor("white")
        )
        self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background, foreground):
        self.setStyleSheet(
            """
            QRadioButton::indicator::unchecked {
                background-color: %s;
            }
        """
            % (background.name())
        )

    def enterEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)


class CheckBox(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QVariantAnimation(
            startValue=QColor("#6E25E6"),
            endValue=QColor("#2d333d"),
            valueChanged=self._on_value_changed,
            duration=200,
        )
        self._update_stylesheet(QColor("#2d333d"), QColor("white"))
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def _on_value_changed(self, color):
        foreground = (
            QColor("white")
            if self._animation.direction() == QAbstractAnimation.Forward
            else QColor("white")
        )
        self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background, foreground):
        self.setStyleSheet(
            """
            QCheckBox::indicator:unchecked {
                background-color: %s;
            }
        """
            % (background.name())
        )

    def enterEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"/*-------------------- Background --------------------*/\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/*-------------------- Menu Style --------------------*/\n"
"#leftMenuContainer, #rightMenuContainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#centerSubMenuContainer, #rightSubMenuContainer, #popupNotificationContainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"/*-------------------- Header & Footer --------------------*/\n"
"#headerContainer, #footerContainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"/*-------------------- Group Box --------------------*/\n"
"QGroupBox {\n"
"    background-color: #16191d;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subc"
                        "ontrol-position: top center; /* position at the top center */\n"
"	padding: 2px;\n"
"    background-color: #6E25E6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/*-------------------- Button --------------------*/\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 5px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#click{\n"
"	background-color: #6E25E6;\n"
"	text-align: center;\n"
"	padding: 5px 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"/*-------------------- Prograss Bar --------------------*/\n"
"QProgressBar {\n"
"    border: 2px solid #101216;\n"
"    border-radius: 5px;\n"
"	background-color: #1f232a;\n"
"	text-align: center;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #6E25E6;\n"
"    width: 10px;\n"
"	margin: 2px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"/*-------------------- CheckBox --------------------*/\n"
"QCheckBox {\n"
"	background-color: rgb(45, 51, 61);\n"
"    spacing: 10px;\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"	background-color: #1f232a;\n"
""
                        "}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 17px;\n"
"    height: 17px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	background-color: #2d333d;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"	background-color: #6E25E6;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color: #6E25E6;\n"
"	image: url(:/Icon-W/resources/Icons - W/check.svg);\n"
"}\n"
"\n"
"/*-------------------- ComboBox --------------------*/\n"
"  QComboBox {\n"
"    border-radius: 5px;\n"
"    padding: 5px 20px 5px 8px;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"   background-color: #1f232a;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background-color: #1f232a;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background-color: #1f232a;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 5px;\n"
"    padding-left: 10p"
                        "x;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"	padding-right: 5px;\n"
"    width: 20px;\n"
"	image: url(:/Icon-W/resources/Icons - W/chevron-down.svg);\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"	background-color: #1f232a;\n"
"	font-size: 12px;\n"
"	border: 1px solid rgba(0, 0, 0, 10%);\n"
"	padding: 5px;\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QListView:item {\n"
"	background-color: #1f232a;\n"
"	padding: 5px 5px 5px 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QListView:item:hover {\n"
"	background-color: #6E25E6;\n"
"}\n"
"\n"
"QComboBox QListView:item:selected {\n"
"	background-color: #6E25E6;\n"
"}\n"
"\n"
"/*-------------------- LineEdit --------------------*/\n"
"QLineEdit {\n"
"	background-color: #1f232a;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	border: 1px solid #101216;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 1px solid #6E25E6;\n"
"}\n"
"\n"
"/*-------------------- SpinBox --------------------*/\n"
""
                        "QSpinBox {\n"
"	background-color: #1f232a;\n"
"	border: 1px solid #101216;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"	border: 1px solid #6E25E6;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px; \n"
"	margin-right: 3px;\n"
"	margin-top: 3px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: #2b313b;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"	image: url(:/Icon-W/resources/Icons - W/chevron-up.svg);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; \n"
"     width: 20px; \n"
"	margin-right: 3px;\n"
"	margin-bottom: 3px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: #2b313b;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"	image: url(:/Icon-W/resources/Icons - W/chevron-down.svg);\n"
"    width: 15"
                        "px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"/*-------------------- RadioBotton --------------------*/\n"
"QRadioButton {\n"
"	background-color: #1f232a;\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"	border-radius: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    background-color: #2d333d;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"	background-color: #6E25E6;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"   	background-color: #6E25E6;\n"
"	image: url(:/Icon-W/resources/Icons - W/check-circle.svg)\n"
"}\n"
"\n"
"/*-------------------- Slider --------------------*/\n"
"QSlider::groove:horizontal {\n"
"    height: 5px; \n"
"    background: #1f232a;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #6E25E6;\n"
"    width: 25px;\n"
"    margin: -3px 0; \n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"/*-------------------- Scroll Area --------------------*/\n"
""
                        "QScrollArea{\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    background: #1f232a;\n"
"    width: 8px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background: #6E25E6;\n"
"    min-height: 20px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollArea QScrollBar::add-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollArea QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"QScrollArea QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollArea QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/*-------------------- Table Widget --------------------*/\n"
"QTableWidget {\n"
"	background-color: #16191d;\n"
"	color: #fff;\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #16191d;\n"
"	margin: 10px;\n"
"}\n"
"\n"
"QTableWidget QHead"
                        "erView {\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section  {\n"
"	background-color: #1f232a;\n"
"	margin: 0.5px;\n"
"	border-style: none;\n"
"	border: 1px solid #16191d;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	border: 1px solid #16191d;\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"QTableWidget::item::focus {\n"
"	color:black;\n"
"}\n"
"\n"
"QTableWidget::item::selected {\n"
"	background-color: #6E25E6;\n"
"}\n"
"\n"
"/* QScrollBar - Vertical */\n"
"QTableWidget QScrollBar:vertical {\n"
"    background: #16191d;\n"
"    width: 8px;\n"
"	border-radius: 4px\n"
"}\n"
"QTableWidget QScrollBar::handle:vertical {\n"
"    background: #6E25E6;\n"
"    min-height: 20px;\n"
"	border-radius: 4px\n"
"}\n"
"QTableWidget QScrollBar::add-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"QTableWidget QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    width: 0px;\n"
"    heig"
                        "ht: 0px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* QScrollBar - Horizontal */\n"
"QTableWidget QScrollBar:horizontal  {\n"
"    background: #16191d;\n"
"    height: 8px;\n"
"	border-radius: 4px\n"
"}\n"
"QTableWidget QScrollBar::handle:horizontal  {\n"
"    background: #6E25E6;\n"
"    min-height: 20px;\n"
"	border-radius: 4px\n"
"}\n"
"QTableWidget QScrollBar::add-line:horizontal  {\n"
"    width: 0;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::sub-line:horizontal  {\n"
"    width: 0;\n"
"}\n"
"QTableWidget QScrollBar::up-arrow:horizontal , QScrollBar::down-arrow:horizontal  {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-page:horizontal , QScrollBar::sub-page:horizontal  {\n"
"    background: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_15 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.topContainer = QWidget(self.centralwidget)
        self.topContainer.setObjectName(u"topContainer")
        self.verticalLayout_12 = QVBoxLayout(self.topContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.topContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_3 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 5, 15, 5)
        self.headerTitleFrame = QFrame(self.headerContainer)
        self.headerTitleFrame.setObjectName(u"headerTitleFrame")
        self.headerTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.headerTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.headerTitleFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logoLbl = QLabel(self.headerTitleFrame)
        self.logoLbl.setObjectName(u"logoLbl")
        self.logoLbl.setMaximumSize(QSize(30, 30))
        self.logoLbl.setPixmap(QPixmap(u":/Logo/resources/logo.png"))
        self.logoLbl.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.logoLbl)

        self.headerTitleLbl = QLabel(self.headerTitleFrame)
        self.headerTitleLbl.setObjectName(u"headerTitleLbl")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.headerTitleLbl.setFont(font)

        self.horizontalLayout_5.addWidget(self.headerTitleLbl)


        self.horizontalLayout_3.addWidget(self.headerTitleFrame, 0, Qt.AlignLeft)

        self.centerHeaderFrame = QFrame(self.headerContainer)
        self.centerHeaderFrame.setObjectName(u"centerHeaderFrame")
        self.centerHeaderFrame.setFrameShape(QFrame.StyledPanel)
        self.centerHeaderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.centerHeaderFrame)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.userBtn = QPushButton(self.centerHeaderFrame)
        self.userBtn.setObjectName(u"userBtn")
        self.userBtn.setMinimumSize(QSize(30, 30))
        self.userBtn.setMaximumSize(QSize(30, 30))
        self.userBtn.setStyleSheet(u"background-color: #6E25E6;\n"
"text-align: center;")
        icon = QIcon()
        icon.addFile(u":/Icon-W/resources/Icons - W/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userBtn.setIcon(icon)
        self.userBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.userBtn)

        self.changeMode = QPushButton(self.centerHeaderFrame)
        self.changeMode.setObjectName(u"changeMode")
        self.changeMode.setMinimumSize(QSize(30, 30))
        self.changeMode.setMaximumSize(QSize(30, 30))
        self.changeMode.setStyleSheet(u"background-color: #6E25E6;\n"
"text-align: center;")
        icon1 = QIcon()
        icon1.addFile(u":/Icon-W/resources/Icons - W/sun.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.changeMode.setIcon(icon1)
        self.changeMode.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.changeMode)

        self.moreBtn = QPushButton(self.centerHeaderFrame)
        self.moreBtn.setObjectName(u"moreBtn")
        self.moreBtn.setMinimumSize(QSize(30, 30))
        self.moreBtn.setMaximumSize(QSize(30, 30))
        self.moreBtn.setStyleSheet(u"background-color: #6E25E6;\n"
"text-align: center;")
        icon2 = QIcon()
        icon2.addFile(u":/Icon-W/resources/Icons - W/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreBtn.setIcon(icon2)
        self.moreBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.moreBtn)


        self.horizontalLayout_3.addWidget(self.centerHeaderFrame, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.rightHeaderFrame = QFrame(self.headerContainer)
        self.rightHeaderFrame.setObjectName(u"rightHeaderFrame")
        self.rightHeaderFrame.setFrameShape(QFrame.StyledPanel)
        self.rightHeaderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.rightHeaderFrame)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.rightHeaderFrame)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setMinimumSize(QSize(30, 30))
        self.minimizeBtn.setMaximumSize(QSize(30, 30))
        self.minimizeBtn.setStyleSheet(u"background-color: #6E25E6;\n"
"text-align: center;")
        icon3 = QIcon()
        icon3.addFile(u":/Icon-W/resources/Icons - W/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon3)
        self.minimizeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.rightHeaderFrame)
        self.restoreBtn.setObjectName(u"restoreBtn")
        self.restoreBtn.setMinimumSize(QSize(30, 30))
        self.restoreBtn.setMaximumSize(QSize(30, 30))
        self.restoreBtn.setStyleSheet(u"background-color: #6E25E6;\n"
"text-align: center;")
        icon4 = QIcon()
        icon4.addFile(u":/Icon-W/resources/Icons - W/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon4)
        self.restoreBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.rightHeaderFrame)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(30, 30))
        self.closeBtn.setMaximumSize(QSize(30, 30))
        self.closeBtn.setStyleSheet(u"background-color: #6E25E6;\n"
"text-align: center;")
        icon5 = QIcon()
        icon5.addFile(u":/Icon-W/resources/Icons - W/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon5)
        self.closeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.closeBtn)


        self.horizontalLayout_3.addWidget(self.rightHeaderFrame, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.headerContainer)


        self.verticalLayout_15.addWidget(self.topContainer)

        self.centerContainer = QWidget(self.centralwidget)
        self.centerContainer.setObjectName(u"centerContainer")
        self.centerContainer.setMinimumSize(QSize(782, 486))
        self.centerContainer.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centerContainer)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centerContainer)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(55, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.leftSubMenuContainer = QWidget(self.leftMenuContainer)
        self.leftSubMenuContainer.setObjectName(u"leftSubMenuContainer")
        self.verticalLayout_5 = QVBoxLayout(self.leftSubMenuContainer)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.topFrame = QFrame(self.leftSubMenuContainer)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.topFrame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.topFrame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon6 = QIcon()
        icon6.addFile(u":/Icons - P/resources/Icons - P/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon6)
        self.menuBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.menuBtn)


        self.verticalLayout_5.addWidget(self.topFrame)

        self.centerFrame = QFrame(self.leftSubMenuContainer)
        self.centerFrame.setObjectName(u"centerFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerFrame.sizePolicy().hasHeightForWidth())
        self.centerFrame.setSizePolicy(sizePolicy)
        self.centerFrame.setLayoutDirection(Qt.LeftToRight)
        self.centerFrame.setFrameShape(QFrame.StyledPanel)
        self.centerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.centerFrame)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.centerFrame)
        self.homeBtn.setObjectName(u"homeBtn")
        sizePolicy.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy)
        self.homeBtn.setLayoutDirection(Qt.LeftToRight)
        self.homeBtn.setStyleSheet(u"background-color: #6E25E6;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/Icon-W/resources/Icons - W/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon7)
        self.homeBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.homeBtn)

        self.inboxBtn = QPushButton(self.centerFrame)
        self.inboxBtn.setObjectName(u"inboxBtn")
        icon8 = QIcon()
        icon8.addFile(u":/Icon-P/resources/Icons - P/inbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inboxBtn.setIcon(icon8)
        self.inboxBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.inboxBtn)

        self.dataBtn = QPushButton(self.centerFrame)
        self.dataBtn.setObjectName(u"dataBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dataBtn.sizePolicy().hasHeightForWidth())
        self.dataBtn.setSizePolicy(sizePolicy1)
        icon9 = QIcon()
        icon9.addFile(u":/Icon-P/resources/Icons - P/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBtn.setIcon(icon9)
        self.dataBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.dataBtn)


        self.verticalLayout_5.addWidget(self.centerFrame)

        self.verticalSpacer = QSpacerItem(20, 286, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.bottomFrame = QFrame(self.leftSubMenuContainer)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.bottomFrame)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.settingBtn = QPushButton(self.bottomFrame)
        self.settingBtn.setObjectName(u"settingBtn")
        icon10 = QIcon()
        icon10.addFile(u":/Icon-P/resources/Icons - P/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon10)
        self.settingBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_11.addWidget(self.settingBtn)

        self.infoBtn = QPushButton(self.bottomFrame)
        self.infoBtn.setObjectName(u"infoBtn")
        icon11 = QIcon()
        icon11.addFile(u":/Icon-P/resources/Icons - P/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon11)
        self.infoBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_11.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.bottomFrame)
        self.helpBtn.setObjectName(u"helpBtn")
        icon12 = QIcon()
        icon12.addFile(u":/Icon-P/resources/Icons - P/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon12)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.helpBtn)


        self.verticalLayout_5.addWidget(self.bottomFrame)


        self.verticalLayout_2.addWidget(self.leftSubMenuContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QCustomSlideMenu(self.centerContainer)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerSubMenuContainer = QWidget(self.centerMenuContainer)
        self.centerSubMenuContainer.setObjectName(u"centerSubMenuContainer")
        self.centerSubMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_14 = QVBoxLayout(self.centerSubMenuContainer)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 15)
        self.topCenterMenuTitleFrame = QFrame(self.centerSubMenuContainer)
        self.topCenterMenuTitleFrame.setObjectName(u"topCenterMenuTitleFrame")
        self.topCenterMenuTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.topCenterMenuTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topCenterMenuTitleFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.topCenterMenuTitle = QLabel(self.topCenterMenuTitleFrame)
        self.topCenterMenuTitle.setObjectName(u"topCenterMenuTitle")
        self.topCenterMenuTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.topCenterMenuTitle, 0, Qt.AlignLeft)

        self.closeCenterMenu = QPushButton(self.topCenterMenuTitleFrame)
        self.closeCenterMenu.setObjectName(u"closeCenterMenu")
        self.closeCenterMenu.setStyleSheet(u"text-align: center;")
        icon13 = QIcon()
        icon13.addFile(u":/Icon-P/resources/Icons - P/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenu.setIcon(icon13)
        self.closeCenterMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.closeCenterMenu, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.topCenterMenuTitleFrame)

        self.stackedLeftMenu = QStackedWidget(self.centerSubMenuContainer)
        self.stackedLeftMenu.setObjectName(u"stackedLeftMenu")
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.verticalLayout_8 = QVBoxLayout(self.settingPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.settingLbl = QLabel(self.settingPage)
        self.settingLbl.setObjectName(u"settingLbl")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.settingLbl.setFont(font1)
        self.settingLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.settingLbl)

        self.stackedLeftMenu.addWidget(self.settingPage)
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.verticalLayout_9 = QVBoxLayout(self.infoPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.infoLbl = QLabel(self.infoPage)
        self.infoLbl.setObjectName(u"infoLbl")
        self.infoLbl.setFont(font1)
        self.infoLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.infoLbl)

        self.stackedLeftMenu.addWidget(self.infoPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_10 = QVBoxLayout(self.helpPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.helpLbl = QLabel(self.helpPage)
        self.helpLbl.setObjectName(u"helpLbl")
        self.helpLbl.setFont(font1)
        self.helpLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.helpLbl)

        self.stackedLeftMenu.addWidget(self.helpPage)

        self.verticalLayout_14.addWidget(self.stackedLeftMenu)


        self.verticalLayout_6.addWidget(self.centerSubMenuContainer)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centerContainer)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.verticalLayout_18 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.stackedHome = QStackedWidget(self.mainBodyContainer)
        self.stackedHome.setObjectName(u"stackedHome")
        self.stackedHome.setStyleSheet(u"")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_19 = QVBoxLayout(self.homePage)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.homePage)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(10, 25, 10, 10)
        self.horizontalSlider = QSlider(self.groupBox)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_20.addWidget(self.horizontalSlider)

        self.radioButton = RadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.radioButton)

        self.spinBox = SpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy3)
        self.spinBox.setMinimumSize(QSize(0, 30))
        self.spinBox.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.spinBox)

        self.lineEdit = LineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.lineEdit)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.comboBox)

        self.checkBox = CheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.checkBox)

        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(24)

        self.verticalLayout_20.addWidget(self.progressBar)

        self.click = PushButton(self.groupBox)
        self.click.setObjectName(u"click")
        self.click.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/Icons - W/resources/Icons - W/paperclip.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.click.setIcon(icon14)
        self.click.setIconSize(QSize(24, 24))

        self.verticalLayout_20.addWidget(self.click)


        self.verticalLayout_19.addWidget(self.groupBox)

        self.stackedHome.addWidget(self.homePage)
        self.inboxPage = QWidget()
        self.inboxPage.setObjectName(u"inboxPage")
        self.inboxPage.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.inboxPage)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.inboxPage)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(10, 25, 10, 10)
        self.scrollArea = QScrollArea(self.groupBox_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 228, 696))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.lineEdit_20 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        sizePolicy3.setHeightForWidth(self.lineEdit_20.sizePolicy().hasHeightForWidth())
        self.lineEdit_20.setSizePolicy(sizePolicy3)
        self.lineEdit_20.setMinimumSize(QSize(0, 30))
        self.lineEdit_20.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_20)

        self.lineEdit_19 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        sizePolicy3.setHeightForWidth(self.lineEdit_19.sizePolicy().hasHeightForWidth())
        self.lineEdit_19.setSizePolicy(sizePolicy3)
        self.lineEdit_19.setMinimumSize(QSize(0, 30))
        self.lineEdit_19.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_19)

        self.lineEdit_18 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        sizePolicy3.setHeightForWidth(self.lineEdit_18.sizePolicy().hasHeightForWidth())
        self.lineEdit_18.setSizePolicy(sizePolicy3)
        self.lineEdit_18.setMinimumSize(QSize(0, 30))
        self.lineEdit_18.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_18)

        self.lineEdit_17 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        sizePolicy3.setHeightForWidth(self.lineEdit_17.sizePolicy().hasHeightForWidth())
        self.lineEdit_17.setSizePolicy(sizePolicy3)
        self.lineEdit_17.setMinimumSize(QSize(0, 30))
        self.lineEdit_17.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_17)

        self.lineEdit_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        sizePolicy3.setHeightForWidth(self.lineEdit_16.sizePolicy().hasHeightForWidth())
        self.lineEdit_16.setSizePolicy(sizePolicy3)
        self.lineEdit_16.setMinimumSize(QSize(0, 30))
        self.lineEdit_16.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_16)

        self.lineEdit_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy3.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy3)
        self.lineEdit_15.setMinimumSize(QSize(0, 30))
        self.lineEdit_15.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_15)

        self.lineEdit_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        sizePolicy3.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy3)
        self.lineEdit_14.setMinimumSize(QSize(0, 30))
        self.lineEdit_14.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_14)

        self.lineEdit_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy3.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy3)
        self.lineEdit_13.setMinimumSize(QSize(0, 30))
        self.lineEdit_13.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_13)

        self.lineEdit_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy3.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy3)
        self.lineEdit_12.setMinimumSize(QSize(0, 30))
        self.lineEdit_12.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_12)

        self.lineEdit_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy3.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy3)
        self.lineEdit_11.setMinimumSize(QSize(0, 30))
        self.lineEdit_11.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_11)

        self.lineEdit_10 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy3.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy3)
        self.lineEdit_10.setMinimumSize(QSize(0, 30))
        self.lineEdit_10.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_10)

        self.lineEdit_9 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy3.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy3)
        self.lineEdit_9.setMinimumSize(QSize(0, 30))
        self.lineEdit_9.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_9)

        self.lineEdit_8 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy3.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy3)
        self.lineEdit_8.setMinimumSize(QSize(0, 30))
        self.lineEdit_8.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_8)

        self.lineEdit_7 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy3.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy3)
        self.lineEdit_7.setMinimumSize(QSize(0, 30))
        self.lineEdit_7.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_7)

        self.lineEdit_6 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy3.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy3)
        self.lineEdit_6.setMinimumSize(QSize(0, 30))
        self.lineEdit_6.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_6)

        self.lineEdit_5 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy3.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy3)
        self.lineEdit_5.setMinimumSize(QSize(0, 30))
        self.lineEdit_5.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_5)

        self.lineEdit_4 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy3.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy3)
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_4)

        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy3.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy3)
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_3)

        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy3.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy3)
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.lineEdit_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_22.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.stackedHome.addWidget(self.inboxPage)
        self.dataPage = QWidget()
        self.dataPage.setObjectName(u"dataPage")
        self.verticalLayout_21 = QVBoxLayout(self.dataPage)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.dataPage)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setShowGrid(True)

        self.verticalLayout_21.addWidget(self.tableWidget)

        self.stackedHome.addWidget(self.dataPage)

        self.verticalLayout_18.addWidget(self.stackedHome)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.centerContainer)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_13 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.rightSubMenuContainer = QWidget(self.rightMenuContainer)
        self.rightSubMenuContainer.setObjectName(u"rightSubMenuContainer")
        self.rightSubMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_7 = QVBoxLayout(self.rightSubMenuContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 15)
        self.topRightMenuTitleFrame = QFrame(self.rightSubMenuContainer)
        self.topRightMenuTitleFrame.setObjectName(u"topRightMenuTitleFrame")
        self.topRightMenuTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.topRightMenuTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.topRightMenuTitleFrame)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(20, 0, 20, 0)
        self.topRightMenuTitle = QLabel(self.topRightMenuTitleFrame)
        self.topRightMenuTitle.setObjectName(u"topRightMenuTitle")
        self.topRightMenuTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.topRightMenuTitle, 0, Qt.AlignLeft)

        self.closeRightMenu = QPushButton(self.topRightMenuTitleFrame)
        self.closeRightMenu.setObjectName(u"closeRightMenu")
        self.closeRightMenu.setStyleSheet(u"text-align: center;")
        self.closeRightMenu.setIcon(icon13)
        self.closeRightMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_24.addWidget(self.closeRightMenu, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.topRightMenuTitleFrame)

        self.stackedRightMenu = QStackedWidget(self.rightSubMenuContainer)
        self.stackedRightMenu.setObjectName(u"stackedRightMenu")
        self.userPage = QWidget()
        self.userPage.setObjectName(u"userPage")
        self.verticalLayout_16 = QVBoxLayout(self.userPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.userLbl = QLabel(self.userPage)
        self.userLbl.setObjectName(u"userLbl")
        self.userLbl.setFont(font1)
        self.userLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.userLbl)

        self.stackedRightMenu.addWidget(self.userPage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.verticalLayout_17 = QVBoxLayout(self.morePage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.moreLbl = QLabel(self.morePage)
        self.moreLbl.setObjectName(u"moreLbl")
        self.moreLbl.setFont(font1)
        self.moreLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.moreLbl)

        self.stackedRightMenu.addWidget(self.morePage)

        self.verticalLayout_7.addWidget(self.stackedRightMenu)


        self.verticalLayout_13.addWidget(self.rightSubMenuContainer)


        self.horizontalLayout.addWidget(self.rightMenuContainer)


        self.verticalLayout_15.addWidget(self.centerContainer)

        self.bottomContainer = QWidget(self.centralwidget)
        self.bottomContainer.setObjectName(u"bottomContainer")
        self.verticalLayout_24 = QVBoxLayout(self.bottomContainer)
        self.verticalLayout_24.setSpacing(10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.footerContainer = QWidget(self.bottomContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_22 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(10, 10, 10, 10)
        self.footerFrame = QFrame(self.footerContainer)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setFrameShape(QFrame.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.footerFrame)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.footerText = QLabel(self.footerFrame)
        self.footerText.setObjectName(u"footerText")
        sizePolicy2.setHeightForWidth(self.footerText.sizePolicy().hasHeightForWidth())
        self.footerText.setSizePolicy(sizePolicy2)

        self.horizontalLayout_21.addWidget(self.footerText)


        self.horizontalLayout_22.addWidget(self.footerFrame)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(20, 20))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.sizeGrip, 0, Qt.AlignRight)


        self.verticalLayout_24.addWidget(self.footerContainer)


        self.verticalLayout_15.addWidget(self.bottomContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedLeftMenu.setCurrentIndex(0)
        self.stackedHome.setCurrentIndex(1)
        self.stackedRightMenu.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLbl.setText("")
        self.headerTitleLbl.setText(QCoreApplication.translate("MainWindow", u"Modern UI", None))
        self.userBtn.setText("")
        self.changeMode.setText("")
        self.moreBtn.setText("")
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.menuBtn.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
        self.inboxBtn.setText(QCoreApplication.translate("MainWindow", u"  Inbox", None))
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"  Data", None))
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"  Setting", None))
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"  Information", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"  Help", None))
        self.topCenterMenuTitle.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.closeCenterMenu.setText("")
        self.settingLbl.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.infoLbl.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.helpLbl.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Option - 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Option - 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Option - 3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Option - 4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Option - 5", None))

        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.click.setText(QCoreApplication.translate("MainWindow", u"Click Me !", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.topRightMenuTitle.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.closeRightMenu.setText("")
        self.userLbl.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.moreLbl.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.footerText.setText(QCoreApplication.translate("MainWindow", u"CopyRight ...", None))
    # retranslateUi

