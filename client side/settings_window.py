from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from detection_window import DetectionWindow

class SettingsWindow(QMainWindow):
    def __init__(self, token): #constructor to load the UI
        super(SettingsWindow, self).__init__() #tells that the settingswindow class is a subclass of qmainwindow class
        loadUi('UI/settings_window.ui', self) #path of the settings ui class

        self.token =token

        self.detection_window= DetectionWindow()

        #mapping the button
        self.pushButton.clicked.connect(self.go_to_detection)

        self.popup=QMessageBox()
        self.popup.setWindowTitle("Failed")
        self.popup.setText("Fields must not be empty.")

    #method to display settings window
    def displayInfo(self): #this will be called from the login window and the settings window will be displayed
        self.show() 

    def go_to_detection(self):
        #here we check if detection window is visible
        if self.location_input.text() == '' or self.sendTo_input.text() == '':
            self.popup.exec_()
        else:
                if self.detection_window.isVisible():
                    print('Detection window is already open!')
                else:
                    self.detection_window.create_detection_instance(self.token, self.location_input.text(), self.sendTo_input.text())
                    self.detection_window.start_detection()

    def closeEvent(self, event):
        #check if the window is open the we close it
        if self.detection_window.isVisible():
            self.detection_window.detection.running = False
            self.detection_window.close()
            event.accept()