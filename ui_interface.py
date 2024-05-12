# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacexBoeqq.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QVariantAnimation, QAbstractAnimation)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu

import resources_rc

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
            border: none;
            color: %s;
            text-align: center;
	        padding: 5px 5px;
	        border-radius: 10px;
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	bacground-color: transparent;\n"
"	bacground: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #ffffff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"	border-radius: 10px;\n"
"}\n"
"#leftMenuContainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 5px;\n"
"	border-radius: 5px;\n"
"}\n"
"#centerSubMenuContainer, #rightSubMenuContainer, #popupNotificationContainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 20px;\n"
"}\n"
"#headerContainer, #footerContainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 15px;\n"
"}\n"
"")
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
        font.setWeight(75)
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
        icon.addFile(u":/Icons - W/resources/Icons - W/user.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon1.addFile(u":/Icons - W/resources/Icons - W/sun.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon2.addFile(u":/Icons - W/resources/Icons - W/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon3.addFile(u":/Icons - W/resources/Icons - W/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon4.addFile(u":/Icons - W/resources/Icons - W/square.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon5.addFile(u":/Icons - W/resources/Icons - W/x.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon7.addFile(u":/Icons - W/resources/Icons - W/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon7)
        self.homeBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.homeBtn)

        self.inboxBtn = QPushButton(self.centerFrame)
        self.inboxBtn.setObjectName(u"inboxBtn")
        icon8 = QIcon()
        icon8.addFile(u":/Icons - P/resources/Icons - P/inbox.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon9.addFile(u":/Icons - P/resources/Icons - P/database.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon10.addFile(u":/Icons - P/resources/Icons - P/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon10)
        self.settingBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_11.addWidget(self.settingBtn)

        self.infoBtn = QPushButton(self.bottomFrame)
        self.infoBtn.setObjectName(u"infoBtn")
        icon11 = QIcon()
        icon11.addFile(u":/Icons - P/resources/Icons - P/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon11)
        self.infoBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_11.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.bottomFrame)
        self.helpBtn.setObjectName(u"helpBtn")
        icon12 = QIcon()
        icon12.addFile(u":/Icons - P/resources/Icons - P/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.topCenterMenuTitleFrame = QFrame(self.centerSubMenuContainer)
        self.topCenterMenuTitleFrame.setObjectName(u"topCenterMenuTitleFrame")
        self.topCenterMenuTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.topCenterMenuTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topCenterMenuTitleFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.topCenterMenuTitle = QLabel(self.topCenterMenuTitleFrame)
        self.topCenterMenuTitle.setObjectName(u"topCenterMenuTitle")
        self.topCenterMenuTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.topCenterMenuTitle, 0, Qt.AlignHCenter)


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
        font1.setWeight(75)
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

        self.closeCenterMenuBtnFrame = QFrame(self.centerSubMenuContainer)
        self.closeCenterMenuBtnFrame.setObjectName(u"closeCenterMenuBtnFrame")
        self.closeCenterMenuBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.closeCenterMenuBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.closeCenterMenuBtnFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.closeCenterMenu = QPushButton(self.closeCenterMenuBtnFrame)
        self.closeCenterMenu.setObjectName(u"closeCenterMenu")
        self.closeCenterMenu.setStyleSheet(u"text-align: center;")
        icon13 = QIcon()
        icon13.addFile(u":/Icons - P/resources/Icons - P/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenu.setIcon(icon13)
        self.closeCenterMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.closeCenterMenu, 0, Qt.AlignHCenter)


        self.verticalLayout_14.addWidget(self.closeCenterMenuBtnFrame)


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
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.click = PushButton(self.homePage)
        self.click.setObjectName(u"click")

        icon14 = QIcon()
        icon14.addFile(u":/Icons - W/resources/Icons - W/paperclip.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.click.setIcon(icon14)
        self.click.setIconSize(QSize(24, 24))

        self.verticalLayout_19.addWidget(self.click)

        self.stackedHome.addWidget(self.homePage)
        self.inboxPage = QWidget()
        self.inboxPage.setObjectName(u"inboxPage")
        self.verticalLayout = QVBoxLayout(self.inboxPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inboxLbl = QLabel(self.inboxPage)
        self.inboxLbl.setObjectName(u"inboxLbl")
        self.inboxLbl.setFont(font1)
        self.inboxLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.inboxLbl)

        self.stackedHome.addWidget(self.inboxPage)
        self.dataPage = QWidget()
        self.dataPage.setObjectName(u"dataPage")
        self.verticalLayout_21 = QVBoxLayout(self.dataPage)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.dataLbl = QLabel(self.dataPage)
        self.dataLbl.setObjectName(u"dataLbl")
        self.dataLbl.setFont(font1)
        self.dataLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.dataLbl)

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
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.topRightMenuTitleFrame = QFrame(self.rightSubMenuContainer)
        self.topRightMenuTitleFrame.setObjectName(u"topRightMenuTitleFrame")
        self.topRightMenuTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.topRightMenuTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.topRightMenuTitleFrame)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(15, 15, 15, 15)
        self.topRightMenuTitle = QLabel(self.topRightMenuTitleFrame)
        self.topRightMenuTitle.setObjectName(u"topRightMenuTitle")
        self.topRightMenuTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.topRightMenuTitle, 0, Qt.AlignHCenter)


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

        self.closeRightMenuFrame = QFrame(self.rightSubMenuContainer)
        self.closeRightMenuFrame.setObjectName(u"closeRightMenuFrame")
        self.closeRightMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.closeRightMenuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.closeRightMenuFrame)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 5)
        self.closeRightMenu = QPushButton(self.closeRightMenuFrame)
        self.closeRightMenu.setObjectName(u"closeRightMenu")
        self.closeRightMenu.setStyleSheet(u"text-align: center;")
        self.closeRightMenu.setIcon(icon13)
        self.closeRightMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_23.addWidget(self.closeRightMenu, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.closeRightMenuFrame)


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
        self.stackedHome.setCurrentIndex(0)
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
        self.settingLbl.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.infoLbl.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.helpLbl.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.closeCenterMenu.setText("")
        self.click.setText(QCoreApplication.translate("MainWindow", u"Click Me !", None))
        self.inboxLbl.setText(QCoreApplication.translate("MainWindow", u"Inbox", None))
        self.dataLbl.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.topRightMenuTitle.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.userLbl.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.moreLbl.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.closeRightMenu.setText("")
        self.footerText.setText(QCoreApplication.translate("MainWindow", u"CopyRight ...", None))
    # retranslateUi

