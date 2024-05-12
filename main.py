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
        self.ui.stackedHome.setCurrentIndex(0)
        self.them_code = 0
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
                    bacground-color: transparent;
                    bacground: transparent;
                    padding: 0;
                    margin: 0;
                    color: #000000;
                }
                #centralwidget{
                    background-color: #ffffff;
                    border-radius: 10px;
                }
                #leftMenuContainer{
                    background-color: #eaeaea;
                    background-color: rgb(234, 234, 234);
                    border-radius: 20px;
                }
                QPushButton{
                    text-align: left;
                    padding: 5px 5px;
                    border-radius: 5px;
                }
                #centerSubMenuContainer, #rightSubMenuContainer, #popupNotificationContainer{
                    background-color: #eaeaea;
                    border-radius: 20px;
                }
                #headerContainer, #footerContainer{
                    background-color: #eaeaea;
                    border-radius: 15px;
                }
            """)
            self.ui.changeMode.setIcon(QIcon('./resources/Icons - W/moon.svg'))
            self.them_code = 1

        elif self.them_code == 1:
            self.ui.centralwidget.setStyleSheet("""
                *{
                    border: none;
                    bacground-color: transparent;
                    bacground: transparent;
                    padding: 0;
                    margin: 0;
                    color: #ffffff;
                }
                #centralwidget{
                    background-color: #1f232a;
                    border-radius: 10px;
                }
                #leftMenuContainer{
                    background-color: #16191d;
                    border-radius: 20px;
                }
                QPushButton{
                    text-align: left;
                    padding: 5px 5px;
                    border-radius: 5px;
                }
                #centerSubMenuContainer, #rightSubMenuContainer, #popupNotificationContainer{
                    background-color: #16191d;
                    border-radius: 20px;
                }
                #headerContainer, #footerContainer{
                    background-color: #16191d;
                    border-radius: 15px;
                }
            """)
            self.ui.changeMode.setIcon(QIcon('./resources/Icons - W/sun.svg'))
            self.them_code = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())