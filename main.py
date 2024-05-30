import os
import sys

from ui_interface import *

from Custom_Widgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.them_code = Them_Code
        self.ui.stackedHome.setCurrentIndex(0)
        self.click_event()

    def click_event(self):
        self.ui.homeBtn.clicked.connect(self.set_home_page)
        self.ui.inboxBtn.clicked.connect(self.set_Inbox_page)
        self.ui.dataBtn.clicked.connect(self.set_data_page)

        self.ui.settingBtn.clicked.connect(self.set_setting_page)
        self.ui.infoBtn.clicked.connect(self.set_info_page)
        self.ui.helpBtn.clicked.connect(self.set_help_page)

        self.ui.closeCenterMenu.clicked.connect(self.close_center_menu)

        self.ui.userBtn.clicked.connect(self.set_user_page)
        self.ui.moreBtn.clicked.connect(self.set_more_page)

        self.ui.closeRightMenu.clicked.connect(lambda : self.ui.rightMenuContainer.collapseMenu())

        self.ui.changeMode.clicked.connect(self.change_mode)

    def set_home_page(self):
        if self.them_code == 0:
            self.ui.homeBtn.setStyleSheet('background-color: #6E25E6;')
        elif self.them_code == 1:
            self.ui.homeBtn.setStyleSheet('background-color: #6E25E6;color: #ffffff')
        self.ui.homeBtn.setIcon(QIcon('./resources/Icons - W/home.svg'))
        self.ui.stackedHome.setCurrentIndex(0)

        self.ui.inboxBtn.setStyleSheet('background-color: transparent;')
        self.ui.dataBtn.setStyleSheet('background-color: transparent;')

        self.ui.inboxBtn.setIcon(QIcon('./resources/Icons - P/inbox.svg'))
        self.ui.dataBtn.setIcon(QIcon('./resources/Icons - P/database.svg'))

    def set_Inbox_page(self):
        if self.them_code == 0:
            self.ui.inboxBtn.setStyleSheet('background-color: #6E25E6;')
        elif self.them_code == 1:
            self.ui.inboxBtn.setStyleSheet('background-color: #6E25E6;color: #ffffff')
        self.ui.inboxBtn.setIcon(QIcon('./resources/Icons - W/inbox.svg'))
        self.ui.stackedHome.setCurrentIndex(1)

        self.ui.homeBtn.setStyleSheet('background-color: transparent;')
        self.ui.dataBtn.setStyleSheet('background-color: transparent;')

        self.ui.homeBtn.setIcon(QIcon('./resources/Icons - P/home.svg'))
        self.ui.dataBtn.setIcon(QIcon('./resources/Icons - P/database.svg'))

    def set_data_page(self):
        if self.them_code == 0:
            self.ui.dataBtn.setStyleSheet('background-color: #6E25E6;')
        elif self.them_code == 1:
            self.ui.dataBtn.setStyleSheet('background-color: #6E25E6;color: #ffffff')
        self.ui.dataBtn.setIcon(QIcon('./resources/Icons - W/database.svg'))
        self.ui.stackedHome.setCurrentIndex(2)

        self.ui.homeBtn.setStyleSheet('background-color: transparent;')
        self.ui.inboxBtn.setStyleSheet('background-color: transparent;')

        self.ui.homeBtn.setIcon(QIcon('./resources/Icons - P/home.svg'))
        self.ui.inboxBtn.setIcon(QIcon('./resources/Icons - P/inbox.svg'))

    def set_setting_page(self):
        self.ui.centerMenuContainer.expandMenu()
        if self.them_code == 0:
            self.ui.settingBtn.setStyleSheet('background-color: #6E25E6;')
        elif self.them_code == 1:
            self.ui.settingBtn.setStyleSheet('background-color: #6E25E6;color: #ffffff')
        self.ui.settingBtn.setIcon(QIcon('./resources/Icons - W/settings.svg'))
        self.ui.stackedLeftMenu.setCurrentIndex(0)

        self.ui.infoBtn.setStyleSheet('background-color: transparent;')
        self.ui.helpBtn.setStyleSheet('background-color: transparent;')

        self.ui.infoBtn.setIcon(QIcon('./resources/Icons - P/info.svg'))
        self.ui.helpBtn.setIcon(QIcon('./resources/Icons - P/help-circle.svg'))

    def set_info_page(self):
        self.ui.centerMenuContainer.expandMenu()
        if self.them_code == 0:
            self.ui.infoBtn.setStyleSheet('background-color: #6E25E6;')
        elif self.them_code == 1:
            self.ui.infoBtn.setStyleSheet('background-color: #6E25E6;color: #ffffff')
        self.ui.infoBtn.setIcon(QIcon('./resources/Icons - W/info.svg'))
        self.ui.stackedLeftMenu.setCurrentIndex(1)

        self.ui.settingBtn.setStyleSheet('background-color: transparent;')
        self.ui.helpBtn.setStyleSheet('background-color: transparent;')

        self.ui.settingBtn.setIcon(QIcon('./resources/Icons - P/settings.svg'))
        self.ui.helpBtn.setIcon(QIcon('./resources/Icons - P/help-circle.svg'))

    def set_help_page(self):
        self.ui.centerMenuContainer.expandMenu()
        if self.them_code == 0:
            self.ui.helpBtn.setStyleSheet('background-color: #6E25E6;')
        elif self.them_code == 1:
            self.ui.helpBtn.setStyleSheet('background-color: #6E25E6;color: #ffffff')
        self.ui.helpBtn.setIcon(QIcon('./resources/Icons - W/help-circle.svg'))
        self.ui.stackedLeftMenu.setCurrentIndex(2)

        self.ui.infoBtn.setStyleSheet('background-color: transparent;')
        self.ui.settingBtn.setStyleSheet('background-color: transparent;')

        self.ui.infoBtn.setIcon(QIcon('./resources/Icons - P/info.svg'))
        self.ui.settingBtn.setIcon(QIcon('./resources/Icons - P/settings.svg'))

    def close_center_menu(self):
        self.ui.centerMenuContainer.collapseMenu()

        self.ui.settingBtn.setStyleSheet('background-color: transparent;')
        self.ui.infoBtn.setStyleSheet('background-color: transparent;')
        self.ui.helpBtn.setStyleSheet('background-color: transparent;')

        self.ui.settingBtn.setIcon(QIcon('./resources/Icons - P/settings.svg'))
        self.ui.infoBtn.setIcon(QIcon('./resources/Icons - P/info.svg'))
        self.ui.helpBtn.setIcon(QIcon('./resources/Icons - P/help-circle.svg'))

    def set_user_page(self):
        self.ui.rightMenuContainer.expandMenu()
        self.ui.stackedRightMenu.setCurrentIndex(0)

    def set_more_page(self):
        self.ui.rightMenuContainer.expandMenu()
        self.ui.stackedRightMenu.setCurrentIndex(1)

    def change_mode(self):
        if self.them_code == 0:
            self.ui.centralwidget.setStyleSheet("""
                            *{
                                border: none;
                                padding: 0;
                                margin: 0;
                                color: #000000;
                            }

                            /*-------------------- Background --------------------*/
                            #centralwidget{
                                background-color: #ffffff;
                                border-radius: 5px;
                            }

                            /*-------------------- Menu Style --------------------*/
                            #leftMenuContainer, #rightMenuContainer{
                                background-color: #eaeaea;
                                border-radius: 20px;
                            }

                            #centerSubMenuContainer, #rightSubMenuContainer, #popupNotificationContainer{
                                background-color: #eaeaea;
                                border-radius: 10px;
                            }

                            /*-------------------- Header & Footer --------------------*/
                            #headerContainer, #footerContainer{
                                background-color: #eaeaea;
                                border-radius: 15px;
                            }

                            /*-------------------- Group Box --------------------*/
                            QGroupBox {
                                background-color: #eaeaea;
                                border-radius: 5px;
                                margin-top: 1ex; /* leave space at the top for the title */
                            }

                            QGroupBox::title {
                                subcontrol-origin: margin;
                                subcontrol-position: top center; /* position at the top center */
                                padding: 2px;
                                color: #fff;
                                background-color: #6E25E6;
                                border-radius: 5px;
                            }

                            /*-------------------- Button --------------------*/
                            QPushButton{
                                text-align: left;
                                padding: 5px 5px;
                                border-radius: 5px;
                            }

                            #click{
                                background-color: #6E25E6;
                                text-align: center;
                                padding: 5px 5px;
                                border-radius: 10px;
                            }

                            /*-------------------- Prograss Bar --------------------*/
                            QProgressBar {
                                border: 2px solid #101216;
                                border-radius: 5px;
                                background-color: #ffffff;
                                text-align: center;
                                border-radius: 5px;
                            }

                            QProgressBar::chunk {
                                background-color: #6E25E6;
                                width: 10px;
                                margin: 2px;
                                border-radius: 3px;
                            }

                            /*-------------------- CheckBox --------------------*/
                            QCheckBox {
                                background-color: rgb(45, 51, 61);
                                spacing: 10px;
                                padding: 5px;
                                border-radius: 5px;
                                background-color: #ffffff;
                            }

                            QCheckBox::indicator {
                                width: 17px;
                                height: 17px;
                                border-radius: 5px;
                            }

                            QCheckBox::indicator:unchecked {
                                background-color: #eaeaea;
                            }

                            QCheckBox::indicator:unchecked:hover {
                                background-color: #6E25E6;
                            }

                            QCheckBox::indicator:checked {
                                background-color: #6E25E6;
                                image: url(:/Icon-W/resources/Icons - W/check.svg);
                            }

                            /*-------------------- ComboBox --------------------*/
                              QComboBox {
                                border-radius: 5px;
                                padding: 5px 20px 5px 8px;
                            }

                            QComboBox:editable {
                               background-color: #ffffff;
                            }

                            QComboBox:!editable, QComboBox::drop-down:editable {
                                 background-color: #ffffff;
                            }

                            /* QComboBox gets the "on" state when the popup is open */
                            QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                                background-color: #ffffff;
                            }

                            QComboBox:on { /* shift the text when the popup opens */
                                padding-top: 5px;
                                padding-left: 10px;
                            }

                            QComboBox::drop-down {
                                subcontrol-origin: padding;
                                subcontrol-position: top right;
                                padding-right: 5px;
                                width: 20px;
                                image: url(:/Icon-W/resources/Icons - W/chevron-down.svg);
                            }

                            QComboBox QListView {
                                background-color: #ffffff;
                                font-size: 12px;
                                border: 1px solid rgba(0, 0, 0, 10%);
                                padding: 5px;
                                outline: 0px;
                            }

                            QComboBox QListView:item {
                                background-color: #ffffff;
                                padding: 5px 5px 5px 10px;
                                border-radius: 5px;
                            }

                            QComboBox QListView:item:hover {
                                background-color: #6E25E6;
                            }

                            QComboBox QListView:item:selected {
                                background-color: #6E25E6;
                            }

                            /*-------------------- LineEdit --------------------*/
                            QLineEdit {
                                background-color: #ffffff;
                                border-radius: 5px;
                                padding: 5px;
                                border: 1px solid #101216;
                            }

                            QLineEdit:focus {
                                border: 1px solid #6E25E6;
                            }

                            /*-------------------- SpinBox --------------------*/
                            QSpinBox {
                                background-color: #ffffff;
                                border: 1px solid #101216;
                                border-radius: 5px;
                                padding: 5px;
                            }

                            QSpinBox:focus {
                                border: 1px solid #6E25E6;
                            }

                            QSpinBox::up-button {
                                subcontrol-origin: border;
                                subcontrol-position: top right;
                                width: 20px; 
                                margin-right: 3px;
                                margin-top: 3px;
                                border-radius: 5px;
                            }

                            QSpinBox::up-button:pressed {
                                background-color: #eaeaea;
                            }

                            QSpinBox::up-arrow {
                                image: url(:/Icon-B/resources/Icons - B/chevron-up.svg);
                                width: 15px;
                                height: 15px;
                            }

                            QSpinBox::down-button {
                                subcontrol-origin: border;
                                subcontrol-position: bottom right; 
                                 width: 20px; 
                                margin-right: 3px;
                                margin-bottom: 3px;
                                border-radius: 5px;
                            }

                            QSpinBox::down-button:pressed {
                                background-color: #eaeaea;
                            }

                            QSpinBox::down-arrow {
                                image: url(:/Icon-B/resources/Icons - B/chevron-down.svg);
                                width: 15px;
                                height: 15px;
                            }

                            /*-------------------- RadioBotton --------------------*/
                            QRadioButton {
                                background-color: #ffffff;
                                padding: 5px;
                                border-radius: 5px;
                            }

                            QRadioButton::indicator {
                                width: 18px;
                                height: 18px;
                                border-radius: 9px;
                            }

                            QRadioButton::indicator::unchecked {
                                background-color: #eaeaea;
                            }

                            QRadioButton::indicator:unchecked:hover {
                                background-color: #6E25E6;
                            }

                            QRadioButton::indicator::checked {
                                background-color: #6E25E6;
                                image: url(:/Icon-W/resources/Icons - W/check-circle.svg)
                            }

                            /*-------------------- Slider --------------------*/
                            QSlider::groove:horizontal {
                                height: 5px; 
                                background: #ffffff;
                                margin: 2px 0;
                            }

                            QSlider::handle:horizontal {
                                background: #6E25E6;
                                width: 25px;
                                margin: -3px 0; 
                                border-radius: 2px;
                            }

                            /*-------------------- Scroll Area --------------------*/
                            QScrollArea{
                                background-color: #eaeaea;
                            }

                            QScrollArea QScrollBar:vertical {
                                background: #ffffff;
                                width: 8px;
                                border-radius: 4px
                            }
                            QScrollArea QScrollBar::handle:vertical {
                                background: #6E25E6;
                                min-height: 20px;
                                border-radius: 4px
                            }
                            QScrollArea QScrollBar::add-line:vertical {
                                height: 0;
                            }

                            QScrollArea QScrollBar::sub-line:vertical {
                                height: 0;
                            }
                            QScrollArea QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                                width: 0px;
                                height: 0px;
                            }

                            QScrollArea QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                background: none;
                            }

                            /*-------------------- Table Widget --------------------*/
                            QTableWidget {
                                background-color: #eaeaea;
                                color: #000000;
                                padding: 5px;
                                border-radius: 5px;
                            }

                            QTableWidget QTableCornerButton::section {
                                background-color: #eaeaea;
                                margin: 10px;
                            }

                            QTableWidget QHeaderView {
                                background-color: #eaeaea;
                            }

                            QTableWidget QHeaderView::section  {
                                background-color: #ffffff;
                                margin: 0.5px;
                                border-style: none;
                                border: 1px solid #eaeaea;
                                padding-left: 5px;
                            }

                            QTableWidget::item {
                                border: 1px solid #eaeaea;
                                background-color: #ffffff;
                            }

                            QTableWidget::item::focus {
                                color: #ffffff;
                            }

                            QTableWidget::item::selected {
                                background-color: #6E25E6;
                            }

                            /* QScrollBar - Vertical */
                            QTableWidget QScrollBar:vertical {
                                background: #eaeaea;
                                width: 8px;
                                border-radius: 4px
                            }
                            QTableWidget QScrollBar::handle:vertical {
                                background: #6E25E6;
                                min-height: 20px;
                                border-radius: 4px
                            }
                            QTableWidget QScrollBar::add-line:vertical {
                                height: 0;
                            }

                            QTableWidget QScrollBar::sub-line:vertical {
                                height: 0;
                            }
                            QTableWidget QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                                width: 0px;
                                height: 0px;
                            }

                            QTableWidget QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                background: none;
                            }

                            /* QScrollBar - Horizontal */
                            QTableWidget QScrollBar:horizontal  {
                                background: #eaeaea;
                                height: 8px;
                                border-radius: 4px
                            }
                            QTableWidget QScrollBar::handle:horizontal  {
                                background: #6E25E6;
                                min-height: 20px;
                                border-radius: 4px
                            }
                            QTableWidget QScrollBar::add-line:horizontal  {
                                width: 0;
                            }

                            QTableWidget QScrollBar::sub-line:horizontal  {
                                width: 0;
                            }
                            QTableWidget QScrollBar::up-arrow:horizontal , QScrollBar::down-arrow:horizontal  {
                                width: 0px;
                                height: 0px;
                            }

                            QTableWidget QScrollBar::add-page:horizontal , QScrollBar::sub-page:horizontal  {
                                background: none;
                            }
                        """)
            self.ui.changeMode.setIcon(QIcon('./resources/Icons - W/moon.svg'))
            self.them_code = 1

        elif self.them_code == 1:
            self.ui.centralwidget.setStyleSheet("""
                *{
                    border: none;
                    padding: 0;
                    margin: 0;
                    color: #ffffff;
                }
                
                /*-------------------- Background --------------------*/
                #centralwidget{
                    background-color: #1f232a;
                    border-radius: 5px;
                }
                
                /*-------------------- Menu Style --------------------*/
                #leftMenuContainer, #rightMenuContainer{
                    background-color: #16191d;
                    border-radius: 20px;
                }
                
                #centerSubMenuContainer, #rightSubMenuContainer, #popupNotificationContainer{
                    background-color: #16191d;
                    border-radius: 10px;
                }
                
                /*-------------------- Header & Footer --------------------*/
                #headerContainer, #footerContainer{
                    background-color: #16191d;
                    border-radius: 15px;
                }
                
                /*-------------------- Group Box --------------------*/
                QGroupBox {
                    background-color: #16191d;
                    border-radius: 5px;
                    margin-top: 1ex; /* leave space at the top for the title */
                }
                
                QGroupBox::title {
                    subcontrol-origin: margin;
                    subcontrol-position: top center; /* position at the top center */
                    padding: 2px;
                    background-color: #6E25E6;
                    border-radius: 5px;
                }
                
                /*-------------------- Button --------------------*/
                QPushButton{
                    text-align: left;
                    padding: 5px 5px;
                    border-radius: 5px;
                }
                
                #click{
                    background-color: #6E25E6;
                    text-align: center;
                    padding: 5px 5px;
                    border-radius: 10px;
                }
                
                /*-------------------- Prograss Bar --------------------*/
                QProgressBar {
                    border: 2px solid #101216;
                    border-radius: 5px;
                    background-color: #1f232a;
                    text-align: center;
                    border-radius: 5px;
                }
                
                QProgressBar::chunk {
                    background-color: #6E25E6;
                    width: 10px;
                    margin: 2px;
                    border-radius: 3px;
                }
                
                /*-------------------- CheckBox --------------------*/
                QCheckBox {
                    background-color: rgb(45, 51, 61);
                    spacing: 10px;
                    padding: 5px;
                    border-radius: 5px;
                    background-color: #1f232a;
                }
                
                QCheckBox::indicator {
                    width: 17px;
                    height: 17px;
                    border-radius: 5px;
                }
                
                QCheckBox::indicator:unchecked {
                    background-color: #2d333d;
                }
                
                QCheckBox::indicator:unchecked:hover {
                    background-color: #6E25E6;
                }
                
                QCheckBox::indicator:checked {
                    background-color: #6E25E6;
                    image: url(:/Icon-W/resources/Icons - W/check.svg);
                }
                
                /*-------------------- ComboBox --------------------*/
                  QComboBox {
                    border-radius: 5px;
                    padding: 5px 20px 5px 8px;
                }
                
                QComboBox:editable {
                   background-color: #1f232a;
                }
                
                QComboBox:!editable, QComboBox::drop-down:editable {
                     background-color: #1f232a;
                }
                
                /* QComboBox gets the "on" state when the popup is open */
                QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                    background-color: #1f232a;
                }
                
                QComboBox:on { /* shift the text when the popup opens */
                    padding-top: 5px;
                    padding-left: 10px;
                }
                
                QComboBox::drop-down {
                    subcontrol-origin: padding;
                    subcontrol-position: top right;
                    padding-right: 5px;
                    width: 20px;
                    image: url(:/Icon-W/resources/Icons - W/chevron-down.svg);
                }
                
                QComboBox QListView {
                    background-color: #1f232a;
                    font-size: 12px;
                    border: 1px solid rgba(0, 0, 0, 10%);
                    padding: 5px;
                    outline: 0px;
                }
                
                QComboBox QListView:item {
                    background-color: #1f232a;
                    padding: 5px 5px 5px 10px;
                    border-radius: 5px;
                }
                
                QComboBox QListView:item:hover {
                    background-color: #6E25E6;
                }
                
                QComboBox QListView:item:selected {
                    background-color: #6E25E6;
                }
                
                /*-------------------- LineEdit --------------------*/
                QLineEdit {
                    background-color: #1f232a;
                    border-radius: 5px;
                    padding: 5px;
                    border: 1px solid #101216;
                }
                
                QLineEdit:focus {
                    border: 1px solid #6E25E6;
                }
                
                /*-------------------- SpinBox --------------------*/
                QSpinBox {
                    background-color: #1f232a;
                    border: 1px solid #101216;
                    border-radius: 5px;
                    padding: 5px;
                }
                
                QSpinBox:focus {
                    border: 1px solid #6E25E6;
                }
                
                QSpinBox::up-button {
                    subcontrol-origin: border;
                    subcontrol-position: top right;
                    width: 20px; 
                    margin-right: 3px;
                    margin-top: 3px;
                    border-radius: 5px;
                }
                
                QSpinBox::up-button:pressed {
                    background-color: #2b313b;
                }
                
                QSpinBox::up-arrow {
                    image: url(:/Icon-W/resources/Icons - W/chevron-up.svg);
                    width: 15px;
                    height: 15px;
                }
                
                QSpinBox::down-button {
                    subcontrol-origin: border;
                    subcontrol-position: bottom right; 
                     width: 20px; 
                    margin-right: 3px;
                    margin-bottom: 3px;
                    border-radius: 5px;
                }
                
                QSpinBox::down-button:pressed {
                    background-color: #2b313b;
                }
                
                QSpinBox::down-arrow {
                    image: url(:/Icon-W/resources/Icons - W/chevron-down.svg);
                    width: 15px;
                    height: 15px;
                }
                
                /*-------------------- RadioBotton --------------------*/
                QRadioButton {
                    background-color: #1f232a;
                    padding: 5px;
                    border-radius: 5px;
                }
                
                QRadioButton::indicator {
                    width: 18px;
                    height: 18px;
                    border-radius: 9px;
                }
                
                QRadioButton::indicator::unchecked {
                    background-color: #2d333d;
                }
                
                QRadioButton::indicator:unchecked:hover {
                    background-color: #6E25E6;
                }
                
                QRadioButton::indicator::checked {
                    background-color: #6E25E6;
                    image: url(:/Icon-W/resources/Icons - W/check-circle.svg)
                }
                
                /*-------------------- Slider --------------------*/
                QSlider::groove:horizontal {
                    height: 5px; 
                    background: #1f232a;
                    margin: 2px 0;
                }
                
                QSlider::handle:horizontal {
                    background: #6E25E6;
                    width: 25px;
                    margin: -3px 0; 
                    border-radius: 2px;
                }
                
                /*-------------------- Scroll Area --------------------*/
                QScrollArea{
                    background-color: #16191d;
                }
                
                QScrollArea QScrollBar:vertical {
                    background: #1f232a;
                    width: 8px;
                    border-radius: 4px
                }
                QScrollArea QScrollBar::handle:vertical {
                    background: #6E25E6;
                    min-height: 20px;
                    border-radius: 4px
                }
                QScrollArea QScrollBar::add-line:vertical {
                    height: 0;
                }
                
                QScrollArea QScrollBar::sub-line:vertical {
                    height: 0;
                }
                QScrollArea QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                    width: 0px;
                    height: 0px;
                }
                
                QScrollArea QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: none;
                }
                
                /*-------------------- Table Widget --------------------*/
                QTableWidget {
                    background-color: #16191d;
                    color: #fff;
                    padding: 5px;
                    border-radius: 5px;
                }
                
                QTableWidget QTableCornerButton::section {
                    background-color: #16191d;
                    margin: 10px;
                }
                
                QTableWidget QHeaderView {
                    background-color: #16191d;
                }
                
                QTableWidget QHeaderView::section  {
                    background-color: #1f232a;
                    margin: 0.5px;
                    border-style: none;
                    border: 1px solid #16191d;
                    padding-left: 5px;
                }
                
                QTableWidget::item {
                    border: 1px solid #16191d;
                    background-color: #1f232a;
                }
                
                QTableWidget::item::focus {
                    color:black;
                }
                
                QTableWidget::item::selected {
                    background-color: #6E25E6;
                }
                
                /* QScrollBar - Vertical */
                QTableWidget QScrollBar:vertical {
                    background: #16191d;
                    width: 8px;
                    border-radius: 4px
                }
                QTableWidget QScrollBar::handle:vertical {
                    background: #6E25E6;
                    min-height: 20px;
                    border-radius: 4px
                }
                QTableWidget QScrollBar::add-line:vertical {
                    height: 0;
                }
                
                QTableWidget QScrollBar::sub-line:vertical {
                    height: 0;
                }
                QTableWidget QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                    width: 0px;
                    height: 0px;
                }
                
                QTableWidget QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: none;
                }
                
                /* QScrollBar - Horizontal */
                QTableWidget QScrollBar:horizontal  {
                    background: #16191d;
                    height: 8px;
                    border-radius: 4px
                }
                QTableWidget QScrollBar::handle:horizontal  {
                    background: #6E25E6;
                    min-height: 20px;
                    border-radius: 4px
                }
                QTableWidget QScrollBar::add-line:horizontal  {
                    width: 0;
                }
                
                QTableWidget QScrollBar::sub-line:horizontal  {
                    width: 0;
                }
                QTableWidget QScrollBar::up-arrow:horizontal , QScrollBar::down-arrow:horizontal  {
                    width: 0px;
                    height: 0px;
                }
                
                QTableWidget QScrollBar::add-page:horizontal , QScrollBar::sub-page:horizontal  {
                    background: none;
                }
            """)
            self.ui.changeMode.setIcon(QIcon('./resources/Icons - W/sun.svg'))
            self.them_code = 0
            color1 = "#6E25E6"
            color2 = "#2d333d"

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())