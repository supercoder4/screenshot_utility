import os
import sys
from datetime import datetime

from PySide2 import QtWidgets, QtGui
import pyautogui

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    """
    CREATES A SYSTEM TRAY ICON AND ADDS MENU
    """

    base_path = 'C:/Screenshots/'
    

    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'Capture Screenshot')
        menu = QtWidgets.QMenu(parent)

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        """
        Triggers an event on click or double click on tray icon
        """
        # if reason == self.DoubleClick:
        #     self.open_notepad()
        if reason == self.Trigger:
            self.take_screenshot()

    def take_screenshot(self):
        """
        takes screenshot and save it in C drive based on date and time
        """
        today = datetime.now()
        current_date = today.strftime('%a %b %d %Y')
        current_time = today.strftime('%H.%M.%S.%f')

        path = os.path.join(self.base_path,current_date)
        if not os.path.isdir(path):
            os.mkdir(path)

        screenshot = pyautogui.screenshot()
        screenshot.save(path + '/' + current_time + '.png')
       
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    icon_image_path = 'write_icon_image_path_here'
    tray_icon = SystemTrayIcon(QtGui.QIcon(icon_image_path), w)
    tray_icon.show()
    tray_icon.showMessage('Screenshot Utility', 'running in the background')
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()